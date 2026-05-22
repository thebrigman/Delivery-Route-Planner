import csv

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
                                    row["Weight KILO"], row["Delivery Deadline"], "at hub")
                self.hash_map.put(id_to_int, package)

    def load_truck(self, truck, package_ids):
        for j in package_ids:
            package = self.hash_map.get(j)
            truck.load_package(package)
            package.status = "en route"
        return truck.packages

    def get_time_in_minutes(self, speed, distance):
        time = distance/speed
        time = time * 60
        return time

    def nearest_neighbor(self, truck):

        while len(truck.packages) > 0:
            distances = self.__get_distances(truck)
            distance, address2, package_id = distances[0]
            truck.current_address = address2
            truck.add_distance(distance)
            package = self.hash_map.get(package_id)
            package.status = "delivered"
            truck.packages.remove(package)
            package.delivery_time = truck.current_time

            print(f"current address: {truck.current_address} distance: {distance} total distance: {truck.distance_traveled} time: {truck.current_time}")

        return truck.packages

    def __get_distances(self, truck):
        distances = []

        for i in truck.packages:
            address1 = truck.current_address
            address2 = i.street
            distance = self.distance_table.get_distance(address1, address2)
            package_tuple = (distance, address2, i.ID)
            distances.append(package_tuple)
        distances.sort()

        return distances

    # def load_truck(self,):
    #     with open("truck1.csv", newline="") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             id_to_int = int(row["PackageID"])
    #             self.truck.load_package_id(id_to_int)
    #     return self.truck.packages



