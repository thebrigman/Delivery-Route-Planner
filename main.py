import csv
from datetime import time

from DeliveryRoutingService import DeliveryRoutingService
from Truck import Truck


truck1 = Truck(2, 8, 0, 0)
truck1_packages = [3, 13, 14, 15, 16, 18, 19, 20, 21, 36, 38, 11, 23, 29]
truck2 = Truck(3, 9, 5, 0)
truck2_packages = [6, 25, 28, 32, 31, 22, 40, 4, 1, 24, 2, 7, 10, 8, 9]

truck3 = Truck(1, 8, 0, 0)
truck3_packages = [5, 12, 17, 26, 27, 33, 35, 39, 34, 37]
trucks = [truck1, truck2, truck3]
service = DeliveryRoutingService(trucks)
service.add_packages_to_map()


# -------------------------
# package27 = service.hash_map.get(27)
# print(package27.get_street())
# print(service.distance_table.addresses)

# -------------------------


# service.go_back_to_hub(truck2)
service.load_truck(truck1, truck1_packages)
service.load_truck(truck2, truck2_packages)
service.load_truck(truck3, truck3_packages)
service.nearest_neighbor(truck1)
service.nearest_neighbor(truck2)
service.nearest_neighbor(truck3)
print(f"Truck1:\nTotal pakcages: {len(truck1_packages)}\n{truck1}")
print(f"Truck2:\nTotal pakcages: {len(truck2_packages)}\n{truck2}")
print(f"Truck3:\nTotal pakcages: {len(truck3_packages)}\n{truck3}")


print(f"total distance: {truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled}")
count = 0
for row in service.hash_map.get_map():
    for column in row:
        if column.status == "delivered":
            count += 1
            # print(f"{column.ID}: {column.status} {column.delivery_time}")
print(f"total delivered: {count}")

