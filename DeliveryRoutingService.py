import csv

from DistanceTable import DistanceTable
from HashMap import HashMap
from Package import Package


class DeliveryRoutingService:
    def __init__(self, trucks):
        self.distance_table = DistanceTable()
        self.hash_map = HashMap()
        self.trucks = trucks
        self.distances = []
        self.visited = []
        self.current = 0

    def add_packages_to_map(self):
        with open("WGUPS Package File.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_to_int = int(row["PackageID"])
                package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"],
                                    row["Weight KILO"], row["Delivery Deadline"], None)
                self.hash_map.put(id_to_int, package)

    # def load_truck(self,):
    #     with open("truck1.csv", newline="") as f:
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             id_to_int = int(row["PackageID"])
    #             self.truck.load_package_id(id_to_int)
    #     return self.truck.packages

    def load_truck(self, truck, package_ids):
        for j in package_ids:
            truck.load_package(self.hash_map.get(j))
        return truck.packages

    def get_time_in_minutes(self, speed, distance):
        time = distance/speed
        time = time * 60
        return time

    def print_map(self):
        for row in self.hash_map.get_map():
            for j, val in enumerate(row):
                print(row[j])

    def nearest_neighbor(self, truck):
        distances = []
        packages = truck.packages
        address1 = truck.current_address
        # testing
        visited = []
        times = []
        # testing

        for i in packages:
            address2 = i.street
            distance = self.distance_table.get_distance(address1, address2)
            address_distance_package_id = [distance,  address2, i.ID]
            distances.append(address_distance_package_id)
        distances.sort()

        for num, i in enumerate(distances):
            truck.add_distance(i[0])
            truck.set_current_address(i[1])
            self.hash_map.get(i[2]).status = "delivered"
            print(truck.packages[num])

            print(self.hash_map.get(i[2]).status)


            # testing
            visited.append(truck.current_address)
            times.append(truck.get_time_as_string())

        print(f"total distance: {truck.distance_traveled} Truck time: {truck.current_time}")
        print(visited)
        print(times)
        return distances

    def get_addresses(self):
        return self.distance_table.addresses

    def get_grid(self):
        return self.distance_table.grid

