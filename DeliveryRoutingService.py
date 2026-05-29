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
        self.trucks = []

    # loads packages from csv file to the hashmap
    # time complexity O(N)
    def load_packages_to_hashmap(self):
        with open("WGUPS Package File.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_to_int = int(row["PackageID"])
                package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"],
                                    row["Weight KILO"], row["Delivery Deadline"], row["Notes"], "at hub")
                self.hash_map.put(id_to_int, package)

    def load_truck(self, truck, package_ids):
        """
        Loads a list of packages onto a truck.

        Time Complexity: O(n) where n is the number of package IDs

        :param truck: The truck object to load packages onto
        :param package_ids: A list of package IDs to retrieve and load
        :return: The updated list of packages on the truck
        """
        for j in package_ids:
            package = self.hash_map.get(j)
            truck.load_package(package)
            package.status = "en route"
            package.departure_time = truck.current_time
        return truck.packages

    def go_back_to_hub(self, truck):
        address1 = truck.current_address
        address2 = self.distance_table.addresses[0]
        distance = self.distance_table.get_distance(address1, address2)
        truck.add_distance(distance)
        truck.current_address = address2

    def nearest_neighbor(self, truck, at_time):
        while len(truck.packages) > 0:
            distances = self.__get_distances(truck)
            distance, address2, package_id = distances[0]

            if package_id == 9:
                if truck.current_time > time(10, 20, 00):
                    address2 = "410 S State St"
                    package = self.hash_map.get(package_id)
                    package.address = address2
                    distance = self.distance_table.get_distance(truck.current_address, package.address)
                elif len(truck.packages) > 1:
                    distance, address2, package_id = distances[1]
                else:
                    self.hash_map.get(package_id).status = "at hub"
                    truck.packages.pop()
                    continue

            truck.add_distance(distance)
            if truck.current_time >= at_time:
                truck.add_distance(-distance)
                break
            else:

                package = self.hash_map.get(package_id)
                truck.current_address = address2
                package.delivery_time = truck.current_time
                package.status = "delivered"
                truck.packages.remove(package)

        return truck.packages

    def __get_distances(self, truck):
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
        truck2 = Truck(2, 8, 0, 0)
        truck2_packages = [3, 13, 14, 15, 16, 18, 19, 20, 21, 36, 38, 7, 29, 30, 34, 37]
        truck1 = Truck(1, 9, 5, 0)
        truck1_packages = [6, 25, 28, 32, 31, 22, 40, 4, 1, 24, 10, 8, 9, 11]

        truck3 = Truck(3, 0, 0, 0)
        truck3_packages = [2, 12, 23, 33, 5, 35, 26, 17, 27, 39]

        self.trucks = [truck1, truck2, truck3]
        self.hash_map = HashMap()
        self.load_packages_to_hashmap()

        if at_time >= truck1.current_time:
            self.load_truck(truck1, truck1_packages)
            self.nearest_neighbor(truck1, at_time)
        if at_time >= truck2.current_time:
            self.load_truck(truck2, truck2_packages)
            self.nearest_neighbor(truck2, at_time)

            if len(truck2.packages) == 0:
                self.go_back_to_hub(truck2)
                truck3.current_time = truck2.current_time
                self.load_truck(truck3, truck3_packages)
                self.nearest_neighbor(truck3, at_time)


