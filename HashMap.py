
class HashMap:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.bucket_size = 4

    def __get_hash(self, key: int) -> int:
        index = key % self.size
        return index

    def put(self, key, value):
        bucket = self.__get_hash(key)

        if self.table[bucket] is None:
            self.table[bucket] = [None] * self.bucket_size

        for i in range(self.bucket_size):
            if self.table[bucket][i] is None:
                self.table[bucket][i] = value
                break
        return

    def get(self, key: int):
        bucket = self.__get_hash(key)

        if self.table[bucket] is not None:
            for i in self.table[bucket]:
                if i is not None:
                    if i.package_id == key:
                        return i
        return None
