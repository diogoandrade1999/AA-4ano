import argparse
import time
import utils


def distance_recursive(str1:str, str2:str, index1:int = 0, index2:int = 0) -> int:
    # * insert remaining letters
    if index1 == len(str1):
        return len(str2) - index2

    # * remove remaining letters
    if index2 == len(str2):
        return len(str1) - index1

    utils.increment(1)
    # * equal letters
    if str1[index1] == str2[index2]:
        return distance_recursive(str1, str2, index1 + 1, index2 + 1)

    utils.increment(2)
    return 1 + min(
                distance_recursive(str1, str2, index1, index2 + 1),      # * insert
                distance_recursive(str1, str2, index1 + 1, index2),      # * remove
                distance_recursive(str1, str2, index1 + 1, index2 + 1)   # * replace
                )


def memoize(func):
    cache:dict = {}

    def memoized_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized_func


def distance_dynamic(str1:str, str2:str) -> tuple:
    size1:int = len(str1)
    size2:int = len(str2)

    # ! it is more fast create all list than add sublist during next loops
    d:list = [[None for _ in range(size2 + 1)] for _ in range(size1 + 1)]

    for index1 in range(size1 + 1):
        for index2 in range(size2 + 1):
            if index1 == 0:
                d[index1][index2] = index2
            elif index2 == 0:
                d[index1][index2] = index1
            elif str1[index1 - 1] == str2[index2 - 1]:
                d[index1][index2] = d[index1 - 1][index2 - 1]
            else:
                d[index1][index2] = 1 + min(
                    d[index1][index2 - 1],      # * insert
                    d[index1 - 1][index2],      # * remove
                    d[index1 - 1][index2 - 1]   # * replace
                )
    return d[size1][size2], size1 * size2


def distance_dynamic_improved(str1:str, str2:str) -> tuple:
    size1:int = len(str1)
    size2:int = len(str2)

    d:list = [[x if y == 0 else None for x in range(size2 + 1)] for y in range(2)]

    for index1 in range(1, size1 + 1):
        for index2 in range(size2 + 1):
            if index2 == 0:
                d[index1 % 2][index2] = index1
            elif str1[index1 - 1] == str2[index2 - 1]:
                d[index1 % 2][index2] = d[(index1 - 1) % 2][index2 - 1]
            else:
                d[index1 % 2][index2] = 1 + min(
                    d[(index1 - 1) % 2][index2],    # * insert
                    d[index1 % 2][index2 - 1],      # * remove
                    d[(index1 - 1) % 2][index2 - 1] # * replace
                )
    return d[size1 % 2][size2], size1 * size2


def run(func, func_name:str, str1:str, str2:str, to_print:bool = True) -> tuple:
    utils.initialize()
    start_time:float = time.time()
    if func_name in ["recursive", "memoized"]:
        distance = func(str1, str2)
        operations = utils.counter
    else:
        distance, operations = func(str1, str2)
    finish_time:float = time.time() - start_time
    if to_print:
        print("%10s %8d %12d %3.10f" % (func_name, distance, operations, finish_time))
    return distance, operations, finish_time


def main(str1:str, str2:str) -> None:
    print("\nstr1: {:15} str2: {:15}".format(str1, str2))
    print("%10s %8s %12s %14s" % ("func", "distance", "operations", "execution time"))

    run(distance_recursive, "recursive", str1, str2)

    run(memoize(distance_recursive), "memoized", str1, str2)

    run(distance_dynamic, "dynamic", str1, str2)

    run(distance_dynamic_improved, "improved", str1, str2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s1", dest="str1", required=True, help="str1", type=str)
    parser.add_argument("-s2", dest="str2", required=True, help="str2", type=str)
    args = parser.parse_args()

    main(args.str1, args.str2)
