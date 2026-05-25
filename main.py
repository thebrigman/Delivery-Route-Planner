import csv
from datetime import time

from DeliveryRoutingService import DeliveryRoutingService
from Truck import Truck


truck2 = Truck(2, 8, 0, 0)
truck2_packages = [3, 13, 14, 15, 16, 18, 19, 20, 21, 36, 38, 7, 29, 30, 34, 37]
truck1 = Truck(1, 9, 5, 0)
truck1_packages = [6, 25, 28, 32, 31, 22, 40, 4, 1, 24, 10, 8, 9, 11]

truck3 = Truck(3, 0, 0, 0)
# truck3_packages = [5, 12, 17, 26, 27, 33, 35, 39, 2, 23]
trucks = [truck1, truck2, truck3]
service = DeliveryRoutingService(trucks)
service.add_packages_to_map()


# -------------------------
# package27 = service.hash_map.get(27)
# print(package27.get_street())
# print(service.distance_table.addresses)

# -------------------------



service.load_truck(truck1, truck1_packages)
service.load_truck(truck2, truck2_packages)
service.nearest_neighbor(truck1)
service.nearest_neighbor(truck2)


service.go_back_to_hub(truck2)
truck3.current_time = truck2.current_time
truck3_packages = service.get_remaining_undelivered_packages()

service.load_truck(truck3, truck3_packages)

service.nearest_neighbor(truck3)
print(f"Truck1:\nTotal pakcages: {len(truck1_packages)}\n{truck1}")
print(f"Truck2:\nTotal pakcages: {len(truck2_packages)}\n{truck2}")
print(f"Truck3:\nTotal pakcages: {len(truck3_packages)}\n{truck3}")


print(f"total milage: {truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled}")


count = 0
for row in service.hash_map.get_map():
    for column in row:
        # print(f"{column.ID}: {column.status} {column.delivery_time}")
        if column.status == "delivered":
            count += 1
            # print(f"{column.ID}: {column.status} {column.delivery_time}")
print(f"total delivered: {count}")

