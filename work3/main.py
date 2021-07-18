import argparse
from collections import Counter

from Generator import Generator
from CountMinSketch import CountMinSketch


def main(size:int, size_hash:int, number_hash:int):
    # * generate the data stream
    generator = Generator(size)

    # * init Counter
    count_min_sketch = CountMinSketch(size_hash, number_hash)
    counter = {}

    # * update the counter
    with open('datastream_' + str(size) + '.txt', 'r') as target:
        data = target.read().split(' ')
        counter = Counter(data)
        for d in data:
            count_min_sketch.update(d)

    # * show results
    counter_min_sketch = {}
    for letter, value in counter.items():
        counter_min_sketch[letter] = count_min_sketch.estimate(letter)

    total = sum(counter_min_sketch.values())
    for letter, count in sorted(counter_min_sketch.items(), key=lambda item: item[1], reverse=True):
        print(f'letter: {letter} - {counter[letter]:5} - {count:5} - {(count/total)*100:.2f}%')
    print(f'Expected: {size:5}\nCounted: {total:5}')


if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', dest='size', required=True, help='Size of data stream', type=int)
    parse.add_argument('-sh', dest='size_hash', required=True, help='Size of hash tables', type=int)
    parse.add_argument('-nh', dest='number_hash', required=False, help='Number of hash tables (default=5)', type=int, default=5)
    args = parse.parse_args()

    main(args.size, args.size_hash, args.number_hash)
