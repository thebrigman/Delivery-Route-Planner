import csv
from datetime import time

from DistanceTable import DistanceTable
from HashMap import HashMap
from Package import Package
from Truck import Truck

hash_map = HashMap()
distance_table = DistanceTable()
truck1 = Truck(9,00,00)

def add_packages_to_map():
    with open("WGUPS Package File.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            id_to_int = int(row["PackageID"])
            package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"],
                              row["Weight KILO"], row["Delivery Deadline"], None)
            hash_map.put(id_to_int, package)

add_packages_to_map()


package1 = hash_map.get(6)
package2 = hash_map.get(3)

truck1.load_package(package1)
truck1.load_package(package2)

distance = distance_table.get_distance(package1.get_street(), package2.get_street())

truck1.add_distance(distance)

print(truck1.distance_traveled)
print()
print(truck1.t)
# print(f"{truck.}")
print()

# t = time(8, 00, 0)   # 2:30:00 PM
# t = t.strftime("%H:%M:%S")  # "14:30:00"
# print(t)


# print(truck.print_packages())
# item = hash_map.get(1)
# print(item)
#
# print(distance_table.addresses)
#
# address1 = hash_map.get(13).get_street()
# address2 = hash_map.get(12).get_street()
# print(distance_table.get_distance(address1, address2))
