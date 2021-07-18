import time

COUNTER = 0

# r1(n) = n
def r1(n: int):
    global COUNTER
    COUNTER += 1
    if(n == 0): return 0
    return 1 + r1(n - 1)


def r2(n: int):
    global COUNTER
    COUNTER += 1
    if(n == 0): return 0
    if(n == 1): return 1
    return 1 + r2(n - 2)


def r3(n: int):
    global COUNTER
    COUNTER += 1
    if(n == 0): return 0
    return 1 + 2 * r3(n - 1)


def r4(n: int):
    global COUNTER
    COUNTER += 1
    if(n == 0): return 0
    return 1 + r4(n - 1) + r4(n - 1)


def main():
    global COUNTER
    start = time.time()
    print((r1(10), COUNTER, time.time()-start))
    COUNTER = 0
    start = time.time()
    print((r2(10), COUNTER, time.time()-start))
    COUNTER = 0
    start = time.time()
    print((r3(10), COUNTER, time.time()-start))
    COUNTER = 0
    start = time.time()
    print((r4(10), COUNTER, time.time()-start))
    COUNTER = 0


if __name__ == "__main__":
    main()
