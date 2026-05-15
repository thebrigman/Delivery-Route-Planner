from datetime import datetime, time, timedelta





class Truck:

    def __init__(self, hour=0, minute=0, second=0):
        self.mph = 18
        self.packages = []
        self.distance_traveled = 0
        self.t = datetime(2000,1, 1, hour, minute, second)
        self.current_time = self.t.time()
        self.current_address = "4001 S 700 E"

    def load_package(self, package):
        self.packages.append(package)

    def get_package_by_id(self, num):
        for i in self.packages:
            if i.get_id() == num:
                return i
        return None

    def add_distance(self, distance):
        time_traveled = distance/self.mph
        to_minutes = time_traveled * 60.0
        self.__update_time(to_minutes)
        self.distance_traveled += distance

    def __update_time(self, num = 0):
        self.t = self.t + timedelta(minutes=num)
        self.current_time = self.t.time()

    def print_packages(self):
        for i in self.packages:
            print(f"[{i}]\n")
        return None
