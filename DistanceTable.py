import csv

class DistanceTable:
    def __init__(self):
        self.grid = []
        self.addresses = []
        self.load_addresses()
        self.load_grid()

    def __str__(self):
        the_grid = ""
        for i, row in enumerate(self.grid):
            the_grid = the_grid + f"{self.addresses[i] + ": "}{row}\n"
        return the_grid

    def load_addresses(self):
        with open("WGUPS Distance Table.csv", newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:
                destination = row["Address"].strip()
                self.addresses.append(destination)

    def load_row(self, address: str):
        with open("WGUPS Distance Table.csv", newline="") as f:
            reader = csv.DictReader(f)
            distances = []

            for i, row in enumerate(reader):
                num = row[address]
                if num != '':
                    num = float(row[address])
                else:
                    num = None
                distances.append(num)
            self.grid.append(distances)

    def load_grid(self):
        for i, address in enumerate(self.addresses):
            self.load_row(address)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is None:
                    self.grid[i][j] = self.grid[j][i]

    def get_distance(self, address1, address2):
        address1_index = self.addresses.index(address1)
        address2_index = self.addresses.index(address2)

        return self.grid[address1_index][address2_index]
