import argparse
import random
import string
import matplotlib.pyplot as plt

import utils
import main


def draw(labelsx:list, labelsy:list, labelsz:list, func_name:str):
    for i in range(len(labelsx)):
        plt.plot(labelsx[i], labelsz[i])
    plt.title(func_name + " Algorithm")
    plt.xlabel('Number of basic operations')
    plt.ylabel('Distance')
    plt.show()

    for i in range(len(labelsx)):
        plt.plot(labelsx[i], labelsy[i])
    plt.title(func_name + " Algorithm")
    plt.xlabel('Number of basic operations')
    plt.ylabel('Execution Time')
    plt.show()

    for i in range(len(labelsx)):
        plt.plot(labelsz[i], labelsy[i])
    plt.title(func_name + " Algorithm")
    plt.xlabel('Dista
        labelz = []
        for x in rang

def test(func, func_name:str, repetitions:int, max_str_size:int) -> None:
    labelsx = []
    labelsy = []
    labelsz = []
    for _ in range(repetitions):
        labelx = []
        labely = []
        labelz = []
        for x in range(1, max_str_size):
            str1 = ''.join(random.choices(string.ascii_lowercase, k=x))
            str2 = ''.join(random.choices(string.ascii_lowercase, k=x))
            distance, operations, finish_time = main.run(func, func_name, str1, str2, False)
            labelx += [operations]
            labely += [finish_time]
            labelz += [distance]
        labelsx += [labelx]
        labelsy += [labely]
        labelsz += [labelz]

    if func_name == "improved":
        unc_name = "dynamic"
    draw(labelsx, labelsy, labelsz, func_name.capitalize())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", dest="memoized", help="recursive algorithm", default=False, action='store_true')
    parser.add_argument("-d", dest="dynamic", help="recursive algorithm", default=False, action='store_true')
    parser.add_argument("-r", dest="repetitions", required=True, help="repetitions", type=int)
    parser.add_argument("-s", dest="max_str_size", required=True, help="max_str_size", type=int)
    args = parser.parse_args()

    func_name = "recursive"
    func = main.distance_recursive
    if args.memoized:
        func_name = "memoized"
        func = main.memoize(main.distance_recursive)
    elif args.dynamic:
        func_name = "improved"
        func = main.distance_dynamic_improved

    test(func, func_name, args.repetitions, args.max_str_size)
