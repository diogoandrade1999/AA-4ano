import hashlib
from array import array


class CountMinSketch:
    """Class for counting items using the Count-min Sketch strategy."""
    def __init__(self, w:int, d:int):
        """
        Args:
            w (int): width (number of collumns)
            d (int): depth (number of rows)
        """
        assert w > 0 and d > 0, "w and d should be biggest than 0"
        self._n = 0;
        self._w:int = w
        self._d:int = d
        self._c:list = [array('l', (0 for _ in range(w))) for _ in range(d)]

    def update(self, i, value:int=1) -> None:
        """
        Adds a new item, updating the count.

        Args:
            i : item
            value (int): value to increase in the item counter
        """
        self._n += value
        for j in range(self._d):
            self._c[j][self._hash(i)] += value

    def estimate(self, i) -> int:
        """
        Estimated counter value of item.

        Args:
            i : item

        Return:
            (int): counter value
        """
        est = None
        for j in range(self._d):
            if est is None:
                est:int = self._c[j][self._hash(i)]
            else:
                est:int = min(est, self._c[j][self._hash(i)])
        return est

    def _hash(self, i) -> int:
        """
        Hash table of item.

        Args:
            i : item

        Return:
            (int): hash table
        """
        hash = hashlib.sha256(str(i).encode('utf-8'))
        return int(hash.hexdigest(), 16) % self._w

    def __len__(self) -> int:
        """The amount of items counted, taking in account the repetitions."""
        return self._n
