import csv
import math

from DistanceTable import DistanceTable
from HashMap import HashMap
from Package import Package
from Truck import Truck

class DeliveryRoutingService:

    def __init__(self):
        self.hash_map = HashMap()
        self.truck1 = Truck()
        self.truck2 = Truck()
        self.truck3 = Truck()
        self.distance_table = DistanceTable()
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

    def load_truck1(self):
        with open("truck1.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_to_int = int(row["PackageID"])
                self.truck1.load_package_id(id_to_int)
        return self.truck1.packages

    def get_time_in_minutes(self, speed, distance):
        time = distance/speed
        time = time * 60
        return time

    def print_map(self):
        for i in self.hash_map.keys():
            print(self.hash_map.get(i))

    def nearest_neighbor(self):
        id_distance = []
        for i, row in enumerate(self.hash_map.get_map()):
            address1 = self.distance_table.addresses[0]
            for j in row:
                print(f"{i},{j.get_street()}")
                address2 = j.get_street()
                distance = self.distance_table.get_distance(address1, address2)
                id_distance = [distance, j.get_street()]
                self.distances.append(id_distance)
                self.distances.sort()
        return self.distances

