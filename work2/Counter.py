import random


class Counter:
    """
    Counts the number of occurrences of an element in the chain

    :attr   chain          :str   :chain of elements
    :attr   exact_count    :dict  :exact count of occurrences of an element in the chain
    :param  prob           :float :probablity of increment
    :param  base_log       :float :base of logarithm
    :method _exact_counter :dict  :count the exact number of occurrences of an element in the chain
    :method prob_counter   :dict  :count the number of occurrences of an element in the chain using prob
    :method log_counter    :dict  :count the number of occurrences of an element in the chain using log
    """
    def __init__(self, chain, prob:float, base_log:float):
        """
        :param chain    :list or str :chain of elements
        :param prob     :float       :probablity of increment
        :param base_log :float       :base of logarithm
        """
        assert isinstance(chain, list) or isinstance(chain, str)
        if isinstance(chain, list):
            chain = ''.join(chain)
        self._chain:str = chain
        self._exact_count:dict = self._exact_counter()
        self._prob:float = prob
        self._base_log:int = base_log

    @property
    def chain(self) -> str:
        return self._chain

    @property
    def exact_count(self) -> dict:
        return self._exact_count

    @property
    def prob(self) -> float:
        return self._prob

    @prob.setter
    def prob(self, prob:float) -> None:
        self._prob = prob

    @property
    def base_log(self) -> float:
        return self._base_log

    @base_log.setter
    def base_log(self, base_log:float) -> None:
        self._base_log = base_log

    def _exact_counter(self) -> dict:
        """
        count the exact number of occurrences of an element in the chain
        :return exact_count :dict :exact count of occurrences of an element in the chain
        """
        count:dict = {}
        for element in self._chain:
            count[element]:int = count.get(element, 0) + 1
        return count

    def prob_counter(self) -> dict:
        """
        count the number of occurrences of an element in the chain using prob
        :return prob_count :dict :prob count of occurrences of an element in the chain
        """
        count:dict = {}
        for element in self._chain:
            if random.uniform(0, 1) < self._prob:
                count[element]:int = count.get(element, 0) + 1
        return count

    def log_counter(self) -> dict:
        """
        count the number of occurrences of an element in the chain using log
        :return log_count :dict :log count of occurrences of an element in the chain
        """
        count:dict = {}
        for element in self._chain:
            if element not in count:
                count[element]:int = 1
            else:
                prob:float = (1 / self._base_log) ** count[element]
                if random.uniform(0, 1) < prob:
                    count[element]:int = count[element] + 1
        return count
