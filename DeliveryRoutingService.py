import csv
from datetime import time

from DistanceTable import DistanceTable
from HashMap import HashMap
from Package import Package

class DeliveryRoutingService:
    def __init__(self, trucks):
        self.distance_table = DistanceTable()
        self.hash_map = HashMap()
        self.trucks = trucks

    def add_packages_to_map(self):
        with open("WGUPS Package File.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_to_int = int(row["PackageID"])
                package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"],
                                    row["Weight KILO"], row["Delivery Deadline"], row["Notes"], "at hub")
                self.hash_map.put(id_to_int, package)

    def load_truck(self, truck, package_ids):
        for j in package_ids:
            package = self.hash_map.get(j)
            truck.load_package(package)
            package.status = "en route"
        return truck.packages

    def go_back_to_hub(self, truck):
        address1 = truck.current_address
        address2 = self.distance_table.addresses[0]
        distance = self.distance_table.get_distance(address1, address2)
        truck.add_distance(distance)
        truck.current_address = address2

    def nearest_neighbor(self, truck):
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

            package = self.hash_map.get(package_id)
            truck.current_address = address2
            truck.add_distance(distance)
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

    #   get_remaining_undelivered_packages line 87 — for column in row will crash if a bucket is None. With exactly 40 packages loaded you won't hit this in practice, but it's a gap. You solved this same problem before in HashMap.get — same fix
    #   applies here.
    def get_remaining_undelivered_packages(self):
        undelivered_packages = []

        for row in self.hash_map.table:
            for column in row:
                if column.status == "at hub":
                    undelivered_packages.append(column.package_id)
        return undelivered_packages



