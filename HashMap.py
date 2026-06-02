"""
HashMap.py - Custom hash table implementation using separate chaining.
Separate chaining is used to resolve collisions: each bucket holds a fixed-size
list of values. When two keys hash to the same bucket, they occupy different
slots within that bucket's list.
"""

class HashMap:
    def __init__(self):
        # Table size of 10 distributes 40 packages evenly — 4 per bucket
        self.size = 10
        # Each slot starts as None; buckets are created on first insertion
        self.table = [None] * self.size
        # Maximum number of entries per bucket (handles collisions via chaining)
        self.bucket_size = 4

    def _get_hash(self, key: int) -> int:
        """"
        Hash function: modulo maps any integer key to a valid bucket index.
        Time complexity: O(1)
        """
        index = key % self.size
        return index

    def put(self, key, value):
        """
        Inserts a key-value pair into the hash table.
        Steps: hash the key to find the bucket, initialize the bucket if empty,
        then find the first open slot and insert the value.
        Time complexity: O(1) average — bucket size is fixed and small
        """

        bucket = self._get_hash(key)

        # Initialize the bucket as a fixed-size list on first use
        if self.table[bucket] is None:
            self.table[bucket] = [None] * self.bucket_size

        # Find the first empty slot in the bucket and insert
        for i in range(self.bucket_size):
            if self.table[bucket][i] is None:
                self.table[bucket][i] = value
                break

    def get(self, key: int):
        """
        Looks up and returns the value associated with the given key.
        Steps: hash the key to find the bucket, then search the bucket
        for an entry whose package_id matches the key.
        Time complexity: O(1) average — bucket size is fixed and small
        """

        bucket = self._get_hash(key)

        if self.table[bucket] is not None:
            for i in self.table[bucket]:
                if i is not None:
                    if i.package_id == key:
                        return i
        # Return None if the key is not found
        return None

    def capacity(self):
        """
        Returns the total number of slots across all buckets.
        Used by the UI to validate package ID input range.
        Time complexity: O(1)
        """
        return self.size * self.bucket_size
