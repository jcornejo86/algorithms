""" Implement your own hash table """

class HashTable:
    _array = [None] * 5
    _keys = []
    _max_load_factor = 0.7

    def __init__(self):
        pass

    def add(self, key, value):
        self._compute_load_factor()

        available_slot_idx = self._find_slot()

        self._keys.append((key, available_slot_idx))
        self._array[available_slot_idx] = value

    def get(self, key):
        idx = self._find_idx_by_key(key)

        return self._array[idx] if idx is not None else None

    def capacity(self):
        return len(self._array)

    def used(self):
        return len(self._keys)

    def _find_slot(self):
        for idx, item in enumerate(self._array):
            if item is None:
                return idx

    def _compute_load_factor(self):
        if len(self._keys) / len(self._array) >= self._max_load_factor:
            self._resize()

    def _resize(self):
        size_increase = len(self._keys) * 2
        slots = [None] * size_increase

        self._array += slots

    def _find_idx_by_key(self, lookup):
        for _key in self._keys:
            if _key[0] == lookup:
                return _key[1]


if __name__ == "__main__":
    cache = HashTable()

    print(cache.capacity(), cache.used())

    cache.add("coffee", 2.30)

    print(cache.capacity(), cache.used(), cache.get("coffee"))


    cache.add("milk", 4.10)
    cache.add("sugar", 1.50)
    cache.add("tea", 4.50)
    cache.add("bread", 3.20)

    print(cache.capacity(), cache.used())

    print("milk", cache.get("milk"))
    print("sugar", cache.get("sugar"))
    print("tea", cache.get("tea"))
    print("bread", cache.get("bread"))
