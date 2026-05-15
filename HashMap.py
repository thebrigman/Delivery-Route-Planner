
class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        self.bucket_size = 4

    def get_hash(self, key: int) -> int:
        index = key % self.size
        return index

    def put(self, key, value):
        bucket = self.get_hash(key)

        if self.map[bucket] is None:
            self.map[bucket] = [None] * self.bucket_size

        for i in range(self.bucket_size):
            if self.map[bucket][i] is None:
                self.map[bucket][i] = value
                break
        return

    def get(self, key: int):
        bucket = self.get_hash(key)

        if self.map[bucket] is not None:
            for i in self.map[bucket]:
                if i is not None:
                    if i.get_id() == key:
                        return i
        return None

    def get_map(self):
        return self.map