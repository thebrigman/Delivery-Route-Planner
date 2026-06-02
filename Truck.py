"""
Truck.py - Represents a WGUPS delivery truck.
Tracks the truck's current state during a delivery run: which packages
are loaded, current location, total distance traveled, and current time.
Time is calculated from distance — no separate clock is needed.
"""

from datetime import datetime, time, timedelta


class Truck:

    def __init__(self, id, hour=0, minute=0, second=0):
        self.truck_id = id
        # Trucks travel at a constant 18 mph per project requirements
        self.mph = 18
        # List of Package objects currently loaded on this truck
        self.packages = []
        self.distance_traveled = 0
        # Departure time is set at construction; truck 3 has its time set
        # dynamically after truck 2's driver returns to the hub
        self.current_time = time(hour, minute, second)
        # All trucks start at the hub
        self.current_address = "4001 S 700 E"

    def __str__(self):
        package_ids = ""
        for i in self.packages:
            package_ids = f"{package_ids}{i.package_id}, "
        return (f"distance_traveled: {self.distance_traveled}\n"
                f"current_time: {self.current_time}\n"
                f"current_address: {self.current_address}\n"
                f"package ids: {package_ids}")

    def load_package(self, package):
        """
        Appends a package to the truck's delivery list.
        Loading is instantaneous per project requirements.
        """
        self.packages.append(package)

    def add_distance(self, distance):
        """
        Advances the truck's state by a given distance.
        Converts distance to travel time using d = r * t, then updates
        the internal clock. Also accumulates total distance traveled.
        Time complexity: O(1)
        """
        time_traveled = distance / self.mph
        to_minutes = time_traveled * 60.0
        self.__advance_time(to_minutes)
        self.distance_traveled += distance

    def __advance_time(self, num=0):
        """
        Adds the given number of minutes to the truck's current time.
        Uses datetime.combine with a fixed dummy date so timedelta arithmetic
        works correctly — datetime.time objects do not support addition directly.
        """
        dummy_date = datetime(2000, 1, 1, 8, 0, 0)
        dummy_dt = datetime.combine(dummy_date, self.current_time)
        new_dt = dummy_dt + timedelta(minutes=num)
        self.current_time = new_dt.time()
        return self.current_time
