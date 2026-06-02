"""
DeliveryRoutingService.py - Coordinates all delivery routing logic.
Owns the hash map, distance table, and trucks. Manages package loading,
the nearest neighbor routing algorithm, and the simulation that powers
the status lookup interface.
"""

import csv
from datetime import time

from DistanceTable import DistanceTable
from HashMap import HashMap
from Package import Package
from Truck import Truck


class DeliveryRoutingService:
    def __init__(self):
        self.distance_table = DistanceTable()
        self.hash_map = HashMap()
        # Trucks list is populated in run_service on each query
        self.trucks = []

    def load_packages_to_hashmap(self):
        """
        Reads all packages from the CSV and inserts them into the hash map.
        Each package starts with "at hub" status and no delivery time.
        Time complexity: O(n) where n is the number of packages
        """
        with open("WGUPS Package File.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_to_int = int(row["PackageID"])
                package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"],
                                  row["Weight KILO"], row["Delivery Deadline"], row["Notes"], "at hub")
                self.hash_map.put(id_to_int, package)

    def load_truck(self, truck, package_ids):
        """
        Loads a list of packages onto a truck by looking each one up in the
        hash map. Sets status to "en route" and records the truck's current
        departure time on each package so the UI can determine status at
        any queried time.
        Time complexity: O(n) where n is the number of package IDs
        """
        for j in package_ids:
            package = self.hash_map.get(j)
            truck.load_package(package)
            package.status = "en route"
            package.departure_time = truck.current_time
        return truck.packages

    def go_back_to_hub(self, truck):
        """
        Drives the truck from its last delivery back to the hub.
        Used after truck 2 finishes its route so the driver can take truck 3.
        Updates the truck's distance and time to reflect the return trip.
        """
        address1 = truck.current_address
        address2 = self.distance_table.addresses[0]
        distance = self.distance_table.get_distance(address1, address2)
        truck.add_distance(distance)
        truck.current_address = address2

    def nearest_neighbor(self, truck, query_time):
        """
        Routes a truck through its package list using the nearest neighbor algorithm.
        At each step, calculates the distance from the truck's current location to
        every remaining package, then drives to the closest one.
        Stops early if the truck's time reaches query_time — used for status snapshots.
        Time complexity: O(n^2) where n is the number of packages on the truck —
        each delivery requires recalculating distances to all remaining packages
        """
        while len(truck.packages) > 0:
            distances = self.__get_distances(truck)
            distance, package_address, package_id = distances[0]

            # Handle package 9's delayed address correction
            if package_id == 9:
                if truck.current_time > time(10, 20, 00):
                    # Address is now known — update and recalculate distance
                    package_address = "410 S State St"
                    package = self.hash_map.get(package_id)
                    package.address = package_address
                    distance = self.distance_table.get_distance(truck.current_address, package.address)
                elif len(truck.packages) > 1:
                    # Too early to deliver package 9 — skip to the next nearest
                    distance, package_address, package_id = distances[1]
                else:
                    # Package 9 is the last package but address isn't available yet.
                    # Reset to "at hub" so truck 3 picks it up after 10:20 AM.
                    self.hash_map.get(package_id).status = "at hub"
                    truck.packages.pop()
                    continue

            # Advance the truck's time and distance for this leg of the route
            truck.add_distance(distance)

            # If the truck's time has reached or passed the query time, undo
            # this leg and stop — the snapshot is taken at this point in the route
            if truck.current_time >= query_time:
                truck.add_distance(-distance)
                break
            else:
                # Deliver the package: update location, record delivery time and status
                package = self.hash_map.get(package_id)
                truck.current_address = package_address
                package.delivery_time = truck.current_time
                package.status = "delivered"
                truck.packages.remove(package)

    def __get_distances(self, truck):
        """
        Builds a sorted list of (distance, address, package_id) tuples for
        every package currently on the truck, measured from the truck's
        current address. Sorting puts the nearest package first at index 0.
        Time complexity: O(n log n) where n is packages remaining on the truck
        """
        distances = []
        for i in truck.packages:
            address1 = truck.current_address
            address2 = i.address
            distance = self.distance_table.get_distance(address1, address2)
            package_tuple = (distance, address2, i.package_id)
            distances.append(package_tuple)
        distances.sort()
        return distances

    def run_service(self, at_time):
        """
        Simulates the full delivery day up to at_time and updates each
        package's status accordingly. Called on every user query.

        Delivery sequence:
          Truck 2 departs at 8:00 AM (holds all truck-2-only packages and
          packages with early deadlines).
          Truck 1 departs at 9:05 AM (holds delayed packages that arrive
          at the depot at 9:05 AM).
          Truck 3 departs after truck 2's driver returns to the hub
          (picks up all remaining packages including package 9 if delayed).
        """

        truck2 = Truck(2, 8, 0, 0)
        truck2_packages = [3, 13, 14, 15, 16, 18, 19, 20, 21, 36, 38, 7, 29, 30, 34, 37]
        truck1 = Truck(1, 9, 5, 0)
        truck1_packages = [6, 25, 28, 32, 31, 22, 40, 4, 1, 24, 10, 8, 9, 11]
        truck3 = Truck(3, 0, 0, 0)
        truck3_packages = [2, 12, 23, 33, 5, 35, 26, 17, 27, 39]

        self.trucks = [truck1, truck2, truck3]

        # Reset the hash map so stale package states from prior queries are cleared
        self.hash_map = HashMap()
        self.load_packages_to_hashmap()

        # Only run a truck if at_time is on or after its departure time
        if at_time >= truck1.current_time:
            self.load_truck(truck1, truck1_packages)
            self.nearest_neighbor(truck1, at_time)

        if at_time >= truck2.current_time:
            self.load_truck(truck2, truck2_packages)
            self.nearest_neighbor(truck2, at_time)

            # Truck 3 only departs after truck 2's driver returns to the hub.
            # Only launch truck 3 if truck 2 finished all its deliveries.
            if len(truck2.packages) == 0:
                self.go_back_to_hub(truck2)
                truck3.current_time = truck2.current_time
                self.load_truck(truck3, truck3_packages)
                self.nearest_neighbor(truck3, at_time)
