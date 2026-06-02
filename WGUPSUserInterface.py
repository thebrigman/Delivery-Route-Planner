"""
WGUPSUserInterface.py - Command-line interface for the WGUPS Routing Program.
Allows the user to query package delivery status at any time of day and
view total mileage for all trucks. Delegates all routing logic to
DeliveryRoutingService.
"""

from datetime import time

from Color import Color


class WGUPSUserInterface:
    def __init__(self, service):
        # Holds a reference to the service that runs the delivery simulation
        self.service = service

    def user_interface(self):
        """
        Main menu loop. Runs until the user selects Exit (option 3).
        Validates input and re-prompts on invalid entries.
        """
        user_input = ""
        while user_input != 3:
            # Inner loop ensures only valid integer input is accepted
            while True:
                try:
                    welcome = "--------------------------\nWelcome to WGUPS\n--------------------------\n"
                    options = welcome + "1. View all packages at a specific time frame\n2. Look up a single package\n3. Exit\n"
                    user_input = int(input(options))
                    break
                except ValueError:
                    print("That's not a valid input")

            if user_input == 1:
                # Get the query time, run the simulation up to that time,
                # then print all 40 packages with their status at that moment
                at_time = self.__get_time_from_user()
                self.service.run_service(at_time)
                for row in self.service.hash_map.table:
                    for package in row:
                        print(package)
                # Display per-truck and combined mileage
                total_distance = (self.service.trucks[0].distance_traveled +
                                  self.service.trucks[1].distance_traveled +
                                  self.service.trucks[2].distance_traveled)
                print(f"Truck 1 mileage: {Color.LIME}{self.service.trucks[0].distance_traveled:.1f}{Color.RESET} "
                      f"Truck 2 mileage: {Color.LIME}{self.service.trucks[1].distance_traveled:.1f}{Color.RESET} "
                      f"Truck 3 mileage: {Color.LIME}{self.service.trucks[2].distance_traveled:.1f}{Color.RESET} "
                      f"Total mileage: {Color.LIME}{total_distance:.1f}{Color.RESET}")

            if user_input == 2:
                # Get the query time, run the simulation, then prompt for a
                # specific package ID and display that package's status
                at_time = self.__get_time_from_user()
                self.service.run_service(at_time)
                package = self.__query_single_package()
                print(package)

    def __query_single_package(self):
        """
        Prompts the user for a package ID and returns the corresponding package.
        Validates that the ID is within the valid range before looking it up.
        """
        while True:
            try:
                input_package_id = int(input("Enter package ID: "))
                table_size = self.service.hash_map.capacity()

                if input_package_id < 1 or input_package_id > table_size:
                    print(f"Please enter a package ID from 1 - {table_size}")
                else:
                    break
            except ValueError:
                print("That's not a valid input")

        package = self.service.hash_map.get(input_package_id)
        return package

    def __get_time_from_user(self) -> time:
        """
        Prompts the user to enter a time in "hour:minute AM/PM" format.
        Validates the hour (1-12), minute (0-59), and AM/PM fields.
        Converts to 24-hour format for internal use with datetime.time.
        """
        while True:
            try:
                time_input = input("Enter time (hour:min AM/PM): ")
                hour, rest = time_input.split(":")
                minute, am_pm = rest.split()
                hour, minute, am_pm = (int(hour), int(minute), am_pm.lower())

                if hour < 1 or hour > 12 or minute > 59 or (am_pm != "am" and am_pm != "pm"):
                    print("Hour must be between 1 and 12")
                    print("Minute must be less than 60")
                    print("AM/PM must be 'AM' or 'PM'")
                else:
                    break
            except ValueError:
                print("That's not a valid input")

        # Convert PM hours to 24-hour format (12 PM stays as 12, 1 PM becomes 13, etc.)
        if am_pm == "pm" and hour < 12:
            hour = hour + 12

        input_time = time(hour, minute)
        return input_time
