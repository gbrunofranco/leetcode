from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.mappings = OrderedDict()
        self.capacity = capacity
        self.used_capacity = 0

    def get(self, key: int) -> int:
        if key in self.mappings:
            self.mappings.move_to_end(key)
            return self.mappings[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mappings:
            self.mappings.move_to_end(key)
        else:
            if self.used_capacity < self.capacity:
                self.used_capacity += 1
            else:
                self.mappings.popitem(False)
        self.mappings[key] = value


if __name__ == "__main__":
    ex = LRUCache(2)
    ex.put(1, 1)
    ex.put(2, 2)
    assert ex.get(1) == 1
    ex.put(3, 3)
    assert ex.get(2) == -1
    ex.put(4, 4)
    assert ex.get(1) == -1
    assert ex.get(3) == 3
    assert ex.get(4) == 4
