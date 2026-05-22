from datetime import datetime, time, timedelta


class Truck:

    def __init__(self, id, hour=0, minute=0, second=0):
        self.truck_id = id
        self.mph = 18
        self.packages = []
        self.distance_traveled = 0
        self.current_time = time(hour, minute, second)
        self.current_address = "4001 S 700 E"

    def __str__(self):
        package_ids = ""
        for i in self.packages:
            package_ids = f"{package_ids}{i.ID}, "
        return (f"distance_traveled: {self.distance_traveled}\n"
                f"current_time: {self.current_time}\n"
                f"current_address: {self.current_address}\n"
                f"package ids: {package_ids}")

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
        self.update_time(to_minutes)
        self.distance_traveled += distance

    def update_time(self, num = 0):
        dummy_date = datetime(2000,1, 1, 8, 0, 0)
        dummy_dt = datetime.combine(dummy_date, self.current_time)
        new_dt = dummy_dt + timedelta(minutes=num)
        self.current_time = new_dt.time()
        return self.current_time

    def print_packages(self):
        for i in self.packages:
            print(f"[{i}]\n")
        return None

    def get_time_as_string(self):
        return self.current_time.strftime("%I:%M:%S:%p")
