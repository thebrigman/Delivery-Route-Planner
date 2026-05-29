from datetime import time

from Color import Color


class WGUPSUserInterface:
    def __init__(self, service):
        self.service = service

    def user_interface(self):
        user_input = ""

        while user_input != 3:
            while True:
                try:
                    welcome = "--------------------------\nWelcome to WGUPS\n--------------------------\n"
                    options = welcome + "1. View all packages at a specific time frame\n2. Look up a single package\n3. Exit\n"
                    user_input = int(input(options))
                    break
                except ValueError:
                    print("That's not a valid input")

            if user_input == 1:
                at_time = self.__get_time_from_user()
                self.service.run_service(at_time)
                for row in self.service.hash_map.table:
                    for package in row:
                        print(package)
                total_distance = self.service.trucks[0].distance_traveled + self.service.trucks[1].distance_traveled + self.service.trucks[2].distance_traveled
                print(f"Truck 1 mileage: {Color.LIME}{self.service.trucks[0].distance_traveled:.1f}{Color.RESET} Truck 2 mileage: {Color.LIME}{self.service.trucks[1].distance_traveled:.1f}{Color.RESET} Truck 3 mileage: {Color.LIME}{self.service.trucks[2].distance_traveled:.1f}{Color.RESET} Total milage: {Color.LIME}{total_distance:.1f}{Color.RESET}")

            if user_input == 2:
                at_time = self.__get_time_from_user()
                self.service.run_service(at_time)
                package = self.__query_single_package()
                print(package)

    def __query_single_package(self):
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

        package = self.service.hash_map.get(input_package_id)
        return package

    def __get_time_from_user(self) -> time:
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