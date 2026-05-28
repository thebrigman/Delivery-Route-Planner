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
                # -----------test
                self.__test_EOD_and_delay_time_and_package_9(package, truck)
                # --------test
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

    def run_service(self, at_time):
        truck2 = Truck(2, 8, 0, 0)
        truck2_packages = [3, 13, 14, 15, 16, 18, 19, 20, 21, 36, 38, 7, 29, 30, 34, 37]
        truck1 = Truck(1, 9, 5, 0)
        truck1_packages = [6, 25, 28, 32, 31, 22, 40, 4, 1, 24, 10, 8, 9, 11]

        truck3 = Truck(3, 0, 0, 0)
        truck3_packages = [2, 12, 23, 33, 5, 35, 26, 17, 27, 39]

        self.trucks = [truck1, truck2, truck3]
        self.add_packages_to_map()

        self.load_truck(truck1, truck1_packages)
        self.load_truck(truck2, truck2_packages)
        self.nearest_neighbor(truck1, at_time)
        self.nearest_neighbor(truck2, at_time)

        self.go_back_to_hub(truck2)
        truck3.current_time = truck2.current_time

        self.load_truck(truck3, truck3_packages)

        self.nearest_neighbor(truck3, at_time)
        # print(f"Truck1:\nTotal pakcages: {len(truck1_packages)}\n{truck1}")
        # print(f"Truck2:\nTotal pakcages: {len(truck2_packages)}\n{truck2}")
        # print(f"Truck3:\nTotal pakcages: {len(truck3_packages)}\n{truck3}")
        # for row in self.hash_map.table:
        #     for package in row:
        #         print(package)
        #
        # # print(f"\ntotal delivered: {len(truck1_packages) + len(truck2_packages) + len(truck3_packages)}")
        # print(f"total milage: {truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled}")

    def __test_EOD_and_delay_time_and_package_9(self, package, truck):
        if package.deadline != "EOD":

            if package.deadline == "10:30 AM":
                eod_time_1030 = time(10, 30, 00)
                if truck.current_time > eod_time_1030:
                    print("\033[31mMISSED DEADLINE \033[0m")
                    print(f"TruckID: {truck.truck_id} packageID: {package.package_id} truck time: {truck.current_time} Deadline: {package.deadline}")

            if package.deadline == "9:00 AM":
                eod_time_900 = time(9, 00, 00)
                if truck.current_time > eod_time_900:
                    print("\033[31mMISSED DEADLINE \033[0m")
                    print(f"TruckID: {truck.package_id} packageID: {package.ID} truck time: {truck.current_time} Deadline: {package.deadline}")

        if package.notes == "Delayed on flight---will not arrive to depot until 9:05 am":
            delay_time = time(9, 5,00)
            if truck.current_time < delay_time:
                print("\033[31mDELAYED to 9:05\033[0m")
                print("\033[31mDELIVERED TOO EARLY\033[0m")

        if package.package_id == 9 and truck.current_time < time(10, 20, 00):
            print("\033[31m9 cannot be delivered until after 10:20 \033[0m")

        if package.status == "delivered":
            print("\033[31mPACKAGE ALREADY DELIVERED\033[0m")
            print(f"Package ID: {package.package_id}")

    # def load_truck(self,):
    #     with open("truck1.csv", newline="") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             id_to_int = int(row["PackageID"])
    #             self.truck.load_package_id(id_to_int)
    #     return self.truck.packages

