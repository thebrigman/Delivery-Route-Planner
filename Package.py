class Package:
    def __init__(self, ID, street, city, state, zip_code, weight, deadline, notes, status):
        self.ID = ID
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.deadline = deadline
        self.notes = notes
        self.delivery_time = None

    def __str__(self):
        return (f"ID:{self.ID}\n"
                f"Street:{self.street}\n"
                f"City:{self.city}\n"
                f"State:{self.state}\n"
                f"Zip:{self.zip_code}\n"
                f"Weight:{self.weight}\n"
                f"Deadline:{self.deadline}\n"
                f"Status:{self.status}\n"
                f"Delivery time:{self.delivery_time}"
                f"Notes:{self.notes}")


    def get_street(self):
        return self.street

    def get_id(self) -> int:
        return self.ID

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_status(self):
        return self.status

    def get_deadline(self):
        return self.deadline