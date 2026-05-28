from datetime import time

from Color import Color
from DeliveryRoutingService import DeliveryRoutingService
from Truck import Truck
from WGUPSUserInterface import WGUPSUserInterface
at_time = time(9, 15 ,00)

service = DeliveryRoutingService()
ui = WGUPSUserInterface(service)

ui.user_interface()

# truck2 = Truck(2, 8, 0, 0)
# truck2_packages = [3, 13, 14, 15, 16, 18, 19, 20, 21, 36, 38, 7, 29, 30, 34, 37]
# truck1 = Truck(1, 9, 5, 0)
# truck1_packages = [6, 25, 28, 32, 31, 22, 40, 4, 1, 24, 10, 8, 9, 11]
#
# truck3 = Truck(3, 0, 0, 0)
# truck3_packages = [2, 12, 23, 33, 5, 35, 26, 17, 27, 39]
#
# trucks = [truck1, truck2, truck3]
# service = DeliveryRoutingService(trucks)
# service.add_packages_to_map()
#
# service.load_truck(truck1, truck1_packages)
# service.load_truck(truck2, truck2_packages)
# service.nearest_neighbor(truck1, at_time)
# service.nearest_neighbor(truck2, at_time)
#
# service.go_back_to_hub(truck2)
# truck3.current_time = truck2.current_time
#
# service.load_truck(truck3, truck3_packages)
#
# service.nearest_neighbor(truck3, at_time)
# print(f"Truck1:\nTotal pakcages: {len(truck1_packages)}\n{truck1}")
# print(f"Truck2:\nTotal pakcages: {len(truck2_packages)}\n{truck2}")
# print(f"Truck3:\nTotal pakcages: {len(truck3_packages)}\n{truck3}")
# for row in service.hash_map.table:
#     for package in row:
#         print(package)
#
#
# # print(f"\ntotal delivered: {len(truck1_packages) + len(truck2_packages) + len(truck3_packages)}")
# print(f"total milage: {truck1.distance_traveled + truck2.distance_traveled + truck3.distance_traveled}")

# a_package = service.hash_map.get(22)
#
# print(a_package.departure_time.strftime("%I:%M %p"))
# start = time(9, 25)
# end = time(11, 25)
# for row in service.hash_map.table:
#     for column in row:
#
#         if start < column.delivery_time < end:
#             print(column)
#
# ui = WGUPSUserInterface(service)
#
# ui.user_interface()






