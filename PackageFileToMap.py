import csv

from HashMap import HashMap
from Package import Package


class PackageFileToMap:
    def __init__(self):
        self.map = HashMap()

    def add_packages_to_map(self):
        with open("WGUPS Package File.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_to_int = int(row["PackageID"])
                package = Package(int(row["PackageID"]), row["Address"], row["City"], row["State"], row["Zip"],
                                    row["Weight KILO"], row["Delivery Deadline"], row["Notes"], "at hub")
                self.map.put(id_to_int, package)