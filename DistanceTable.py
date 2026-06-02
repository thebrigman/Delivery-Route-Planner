"""
DistanceTable.py - Loads and stores the WGUPS distance matrix.
Reads the distance table CSV into a 2D list (grid) where grid[i][j] is
the distance in miles between address i and address j.
The source CSV is a lower triangle matrix — only half the values are
present. Missing values are mirrored from the opposite direction since
distances are equal regardless of travel direction per project requirements.
"""
import csv


class DistanceTable:
    def __init__(self):
        # Parallel lists: addresses[i] is the name of location i,
        # grid[i][j] is the distance between location i and location j
        self.grid = []
        self.addresses = []
        # Load data immediately on construction so the table is ready to use
        self.load_addresses()
        self.load_grid()

    def __str__(self):
        the_grid = ""
        for i, row in enumerate(self.grid):
            the_grid = the_grid + f"{self.addresses[i] + ': '}{row}\n"
        return the_grid

    def load_addresses(self):
        """
        Reads the Address column from the CSV to build the ordered list of
        location names. The index of each address in this list corresponds
        to its row and column index in the grid.
        Time complexity: O(n) where n is the number of locations
        """
        with open("WGUPS Distance Table.csv", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                destination = row["Address"].strip()
                self.addresses.append(destination)

    def load_row(self, address: str):
        """
        Reads one column from the CSV — the distances from all other locations
        to the given address. Empty cells are stored as None and filled in
        later by load_grid's mirror pass.
        Time complexity: O(n) where n is the number of locations
        """
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
        """
        Builds the full distance grid by loading each address's column,
        then fills any None values by mirroring from the symmetric position.
        The CSV only contains the lower triangle of the matrix, so
        grid[i][j] == None means the value lives at grid[j][i] instead.
        Time complexity: O(n^2) for the mirror pass
        """
        for i, address in enumerate(self.addresses):
            self.load_row(address)

        # Mirror pass: fill empty cells using the symmetric value
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] is None:
                    self.grid[i][j] = self.grid[j][i]

    def get_distance(self, address1, address2):
        """
        Returns the distance in miles between two address strings.
        Converts address strings to indices, then looks up the grid.
        Time complexity: O(n) for list.index() lookup
        """
        address1_index = self.addresses.index(address1)
        address2_index = self.addresses.index(address2)
        return self.grid[address1_index][address2_index]
