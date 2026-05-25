class Package:
    def __init__(self, ID, street, city, state, zip_code, weight, deadline, notes, status):
        self.package_id = ID
        self.address = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.deadline = deadline
        self.notes = notes
        self.delivery_time = None

    def __str__(self):
        return (f"ID:{self.package_id}\n"
                f"Address:{self.address}\n"
                f"City:{self.city}\n"
                f"State:{self.state}\n"
                f"Zip:{self.zip_code}\n"
                f"Weight:{self.weight}\n"
                f"Deadline:{self.deadline}\n"
                f"Status:{self.status}\n"
                f"Delivery time:{self.delivery_time}"
                f"Notes:{self.notes}")