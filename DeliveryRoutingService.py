import csv
from datetime import time
from typing import Any

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

    def get_time_in_minutes(self, speed, distance):
        time = distance/speed
        time = time * 60
        return time

    def nearest_neighbor(self, truck):

        while len(truck.packages) > 0:

            distances = self.__get_distances(truck)
            distance, address2, package_id = distances[0]

            if package_id == 9:
                if truck.current_time > time(10, 20, 00):
                    address2 = "410 S State St"
                    package = self.hash_map.get(package_id)
                    package.street = address2
                    distance = self.distance_table.get_distance(truck.current_address, package.street)
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

            # TEST---------------------------------------------------
            self.__test_EOD_and_delay_time_and_package_9(package, truck)
            # -----------------------------------------------------
            package.status = "delivered"
            truck.packages.remove(package)

            print(f"\n---------\nTruckID: {truck.ID}\nID {package.ID}, current address: {truck.current_address} distance: {distance} total distance: {truck.distance_traveled} time: {truck.current_time} deadline: {package.deadline}\nnotes: {package.notes}\n----------")

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
    def get_remaining_undelivered_packages(self):
        undelivered_packages = []
        for row in self.hash_map.get_map():
            for column in row:
                if column.status == "at hub":
                    undelivered_packages.append(column.ID)
                    print(f"{column.ID}: {column.status} {column.delivery_time}")
        return undelivered_packages

    def __test_EOD_and_delay_time_and_package_9(self, package: Any | None, truck):
        if package.deadline != "EOD":

            if package.deadline == "10:30 AM":
                eod_time_1030 = time(10, 30, 00)
                if truck.current_time > eod_time_1030:
                    print("\033[31mMISSED DEADLINE \033[0m")
                    print(f"TruckID: {truck.ID} packageID: {package.ID} truck time: {truck.current_time} Deadline: {package.deadline}")

            if package.deadline == "9:00 AM":
                eod_time_900 = time(9, 00, 00)
                if truck.current_time > eod_time_900:
                    print("\033[31mMISSED DEADLINE \033[0m")
                    print(f"TruckID: {truck.ID} packageID: {package.ID} truck time: {truck.current_time} Deadline: {package.deadline}")

        if package.notes == "Delayed on flight---will not arrive to depot until 9:05 am":
            delay_time = time(9, 5,00)
            if truck.current_time < delay_time:
                print("\033[31mDELAYED to 9:05\033[0m")
                print("\033[31mDELIVERED TOO EARLY\033[0m")

        if package.ID == 9 and truck.current_time < time(10, 20, 00):
            print("\033[31m9 cannot be delivered until after 10:20 \033[0m")

        if package.status == "delivered":
            print("\033[31mPACKAGE ALREADY DELIVERED\033[0m")
            print(f"Package ID: {package.ID}")

    # def load_truck(self,):
    #     with open("truck1.csv", newline="") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             id_to_int = int(row["PackageID"])
    #             self.truck.load_package_id(id_to_int)
    #     return self.truck.packages



