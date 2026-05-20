import csv
from datetime import time

from DeliveryRoutingService import DeliveryRoutingService

service = DeliveryRoutingService()
service.add_packages_to_map()

# print(service.get_time_in_minutes(18, 7.2))
# address1 = service.hash_map.get(6).get_street()
# address2 = service.hash_map.get(25).get_street()
# distance = service.distance_table.get_distance(service.hash_map.get(6).get_street(), service.hash_map.get(25).get_street())
# minutes = service.get_time_in_minutes(18, distance)
# print(f"[address1: {address1}\n address2: {address2}\n distance: {distance}\n minutes: {minutes}]")
#
# map = service.hash_map.get_map()
# print(service.load_truck1())
#
# print(service.truck1)

# total_distance = 0
# for i in service.truck1.packages:
#     address1 = service.hash_map.get(i).get_street()
#
#     distance = service.distance_table.get_distance(service.distance_table.addresses[0], address1)
#     total_distance = total_distance + distance
#     print(f"{service.distance_table.addresses[0]} to {address1} = {distance}")
# time = service.get_time_in_minutes(18, total_distance)
# print(f"Total distance: {total_distance} total time: {time}")

# print(service.hash_map.get(1))
# print(service.print_map())
# print(service.nearest_neighbor())
# package1 = hash_map.get(1)
# package2 = hash_map.get(3)
#
# truck1.load_package(package1)
# truck1.load_package(package2)
#
# distance = distance_table.get_distance(package1.get_street(), package2.get_street())
# truck1.set_current_address(truck1.get_package_by_id(package2.get_id()).get_street())
# truck1.add_distance(distance)
#
# print(truck1.distance_traveled)
# print()
# # print(truck1)
# print(f"{truck1}")
# print(distance_table)



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
