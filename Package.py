from Color import Color


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
        self.departure_time = None

    def __str__(self):
        return (f"ID:{Color.BLUE}{self.package_id}{Color.RESET} "
                f"Address:{Color.BLUE}{self.address}{Color.RESET} "
                f"City:{Color.BLUE}{self.city}{Color.RESET} "
                f"State:{Color.BLUE}{self.state}{Color.RESET} "
                f"Zip:{Color.BLUE}{self.zip_code}{Color.RESET} "
                f"Weight:{Color.BLUE}{self.weight}{Color.RESET} "
                f"Deadline:{Color.ORANGE}{self.deadline}{Color.RESET} "
                f"Departure time:{Color.BLUE}{self.departure_time}{Color.RESET} "
                f"Status:{Color.GOLD}{self.status}{Color.RESET} "
                f"Delivery time:{Color.BLUE}{self.delivery_time}{Color.RESET} "
                f"Notes:{Color.TEAL}{self.notes}{Color.RESET}")