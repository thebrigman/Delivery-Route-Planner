from datetime import time

from Color import Color
from DistanceTable import DistanceTable


class WGUPSUserInterface:
    def __init__(self, service):
        self.service = service

    def user_interface(self):
        user_input = ""

        while user_input != 4:
            options = "1. View all packages at a specific time frame\n2. Look up a single package\n4. Exit\n"
            user_input = int(input(options))

            if user_input == 1:
                at_time = self.__get_time()
                self.service.run_service(at_time)
                for row in self.service.hash_map.table:
                    for package in row:
                        print(package)
                total_distance = self.service.trucks[0].distance_traveled + self.service.trucks[1].distance_traveled + self.service.trucks[2].distance_traveled
                print(f"Truck 1 mileage: {self.service.trucks[0].distance_traveled} Truck 2 mileage: {self.service.trucks[1].distance_traveled} Truck 3 mileage: {self.service.trucks[2].distance_traveled} Total milage: {total_distance}")

                # self.__get_package_info_by_time()
            if user_input == 2:
                at_time = self.__get_time()
                self.service.run_service(at_time)
                # self.__get_single_package()

    def __get_total_mileage(self):
        truck1_distance = self.service.trucks[0].distance_traveled
        truck2_distance = self.service.trucks[1].distance_traveled
        truck3_distance = self.service.trucks[2].distance_traveled
        total_distance = truck1_distance + truck2_distance + truck3_distance
        print(f"Truck 1 total distance: {Color.BLUE}{truck1_distance:.1f}{Color.RESET}\n"
              f"Truck 2 total distance: {Color.BLUE}{truck2_distance:.1f}{Color.RESET}\n"
              f"Truck 3 total distance: {Color.BLUE}{truck3_distance:.1f}{Color.RESET}\n"
              f"Total distance: {Color.GREEN}{total_distance:.1f}{Color.RESET}")

    def __get_single_package(self):
        while True:
            try:
                input_package_id = int(input("Enter package ID:"))
                table_size = self.service.hash_map.capacity()

                if input_package_id > table_size:
                    print(f"Please enter a package id from 1 - {table_size}")
                else:
                    break
            except ValueError:
                print("That's not a valid input")

        input_time = self.__get_time()
        package = self.service.hash_map.get(input_package_id)
        self.__fetch_package_info(input_time, package)

    def __get_package_info_by_time(self):
        input_time = self.__get_time()

        for row in self.service.hash_map.table:
            for package in row:
                self.__fetch_package_info(input_time, package)

    def __get_time(self) -> time:
        while True:
            try:
                hour, minute, am_pm = input("Enter time (hour min AM/PM):").split()
                hour, minute, am_pm = (int(hour), int(minute), am_pm.lower())

                if hour < 1 or hour > 12 or minute > 59 or (am_pm != "am" and am_pm != "pm"):
                    print("Hour must be less than or equal to 12")
                    print("Minute must be less than 60")
                    print("AM/PM must be 'AM' or 'PM'")
                else:
                    break
            except ValueError:
                print("That's not a valid input")

        if am_pm.lower() == "pm" and hour < 12:
            hour = hour + 12

        input_time = time(hour, minute)
        return input_time

    def __fetch_package_info(self, input_time: time, package):

        at_hub, en_route, delivered = (f"{Color.YELLOW}at hub{Color.RESET}", f"{Color.BLUE}en route{Color.RESET}",
                                       f"{Color.GREEN}delivered{Color.RESET}")
        if package.departure_time < input_time < package.delivery_time:
            print(f"{package} Departure time: {Color.BLUE}{package.departure_time}{Color.RESET} Status: {en_route}")
        elif input_time >= package.delivery_time:
            delivery_time = package.delivery_time.strftime("%I:%M %p")
            print(f"{package} Departure time: {Color.BLUE}{package.departure_time}{Color.RESET} Status: {delivered} Delivery time: {Color.GREEN}{delivery_time}{Color.RESET}")
        else:
            print(f"{package} status: {at_hub}")

    # def __update_package_9(self, input_time: time):
    #     if input_time < time(10, 19):
    #         package_9 = self.service.hash_map.get(9)
    #         package_9.address = "300 S State St"
    #     else:
    #         package_9 = self.service.hash_map.get(9)
    #         package_9.address = "410 S State St"