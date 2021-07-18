import string
import random


# * 's', 't', 'u', 'v', 'w', 'x': 5
# * 'g', 'h', 'i', 'j', 'k', 'l': 4
# * 'a', 'b', 'c', 'd', 'e', 'f': 3
# * 'm', 'n', 'o', 'p', 'q', 'r': 2
# * 'y', 'z': 1
# * size: 86
LETTERS:str = string.ascii_lowercase + \
        string.ascii_lowercase[:6] * 2 + \
        string.ascii_lowercase[6:12] * 3 + \
        string.ascii_lowercase[12:18] + \
        string.ascii_lowercase[18:24] * 4


class Generator:
    """Generator of simulated data stream."""
    def __init__(self, size:int):
        """
        Args:
            size (int): size of data stream
        """
        self._letters:str = LETTERS
        self._size:int = size
        self._generate()

    @property
    def letters(self) -> str:
        return self._letters

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size:int) -> None:
        self._size = size

    def _generate(self) -> None:
        """Data stream simulator and write them in file"""
        with open('datastream_' + str(self._size) + '.txt', 'w') as target:
            for i, _ in enumerate(range(self._size)):
                target.write(random.choice(self._letters))
                if i != self._size - 1 :
                    target.write(' ')
