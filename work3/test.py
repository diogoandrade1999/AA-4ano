import argparse
from collections import Counter

from Generator import Generator
from CountMinSketch import CountMinSketch


def main(size:int, max_size_hash:int, number_hash:int):
    with open('r_datastream_' + str(size) + '.txt', 'r') as target:
        data = target.read().split(' ')
        counter = Counter(data)

    for size_hash in [125, 148, 152, 157, 161, 189, 199]:
        # * init Counter
        count_min_sketch = CountMinSketch(size_hash, number_hash)

        # * update the counter
        for d in data:
            count_min_sketch.update(d)

        # * show results
        total = 0
        for letter, value in counter.items():
            total += count_min_sketch.estimate(letter)

        if size == total:
            print(f'{size_hash:5} - {size:5} - {total:5}')


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', dest='size', required=True, help='Size of data stream', type=int)
    parse.add_argument('-sh', dest='max_size_hash', required=True, help='Max size of hash tables', type=int)
    parse.add_argument('-nh', dest='number_hash', required=False, help='Number of hash tables (default=5)', type=int, default=5)
    args = parse.parse_args()

    main(args.size, args.max_size_hash, args.number_hash)
