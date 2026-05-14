import csv


class DistanceTable:
    def __init__(self):
        self.grid = []
        self.addresses = []

    def load_addresses(self):
        with open("WGUPS Distance Table.csv", newline="") as f:
            reader = csv.DictReader(f)

            for i, row in enumerate(reader):
                destination = row["Address"].strip()
                self.addresses.append(destination)

    def get_data(self, address: str):
        with open("WGUPS Distance Table.csv", newline="") as f:
            reader = csv.DictReader(f)
            weights = []

            for i, row in enumerate(reader):
                num = row[address]
                if num != '':
                    num = float(row[address])
                else:
                    num = None
                weights.append(num)
            self.grid.append(weights)

    def load_grid(self):
        for i, address in enumerate(self.addresses):
            self.get_data(address)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is None:
                    self.grid[i][j] = self.grid[j][i]