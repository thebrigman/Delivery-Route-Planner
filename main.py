import csv

from DistanceTable import DistanceTable
from HashMap import HashMap
from Package import Package

hash_map = HashMap()
def add_packages_to_map():
    with open("WGUPS Package File.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:

            id_to_int = int(row["PackageID"])
            package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"], row["Weight KILO"], row["Delivery Deadline"], None)
            hash_map.put(id_to_int, package)


add_packages_to_map()
item = hash_map.get(1)
print(item)

for i in hash_map.get_map():
    for j in i:
        print(j.get_street())


distance_table = DistanceTable()
distance_table.load_addresses()
print(distance_table.addresses)
distance_table.load_grid()

for i, val in enumerate(distance_table.addresses):
    print(f"{distance_table.grid[i]}\n")
the_index = distance_table.addresses.index("1060 Dalton Ave S")
print(f"Index: {the_index}")
# for i, val in enumerate(addresses):
#     distance = 0
#     if val == "Western Governors University\n4001 South 700 East,\nSalt Lake City, UT 84107":
#         distance = i
#     if val == "South Salt Lake Public Works\n 195 W Oakland Ave":
#         if distance is not None:
#             print(f"distance to '{addresses[i]}' from '{addresses[distance]}' is {grid[distance][i]} miles")
