# Package.py - Represents a single WGUPS delivery package.
# Stores all data fields required by the project: address, deadline, city,
# zip code, weight, truck id, and delivery status including delivery time.
# Status transitions: "at hub" -> "en route" -> "delivered"

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
        # Set to None until the package is delivered; updated by nearest_neighbor
        self.delivery_time = None
        # Set to the truck's departure time when the package is loaded onto a truck
        self.departure_time = None
        # Set to 'Not assigned yet' until the package is loaded onto a truck
        self.truck_id = "Not assigned yet"

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
                f"Delivery truck:{Color.BLUE}{self.truck_id}{Color.RESET} "
                f"Notes:{Color.TEAL}{self.notes}{Color.RESET}")
