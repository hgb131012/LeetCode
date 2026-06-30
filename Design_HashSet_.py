class MyHashSet(object):
    def __init__(self):
        self.hash_set = set()

    def add(self, key):
        self.hash_set.add(key)

    def remove(self, key):
        if key in self.hash_set:
            self.hash_set.remove(key)

    def contains(self, key):
        return key in self.hash_set
