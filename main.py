import csv
from datetime import time

from DeliveryRoutingService import DeliveryRoutingService
from Truck import Truck

truck1 = Truck(1, 8, 0, 0)
truck1_packages = []
truck2 = Truck(2, 8, 0, 0)
truck2_packages = [20, 21, 13, 15, 19, 3, 36, 39]
truck3 = Truck(3, 8, 0, 0)
truck3_packages = []
trucks = [truck1, truck2, truck3]
service = DeliveryRoutingService(trucks)

service.add_packages_to_map()

service.load_truck(truck2, truck2_packages)
print(truck2)
print(service.nearest_neighbor(truck2))
print(truck2)

for row in service.hash_map.get_map():
    for column in row:
        if column.status == "delivered":
            print(f"{column.ID}: {column.status} {column.delivery_time}")


