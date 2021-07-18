import time

COUNTER = 0
def robot(n):
    global COUNTER
    if n == 1 or n == 2:
        return n
    if n == 3:
        return 4
    COUNTER += 2
    return robot(n-1) + robot(n-2) + robot(n-3)


def main():
    global COUNTER
    print("%4s %8s %8s %6s %10s" % ("n", "result", "COUNTER", "time", "rel time"))
    old_time = 1
    for n in range(10, 30):
        COUNTER = 0
        start_time = time.time()
        result = robot(n)
        end_time = time.time() - start_time
        rel_time = end_time / old_time
        print("%4d %8d %8d %6f %6f" % (n, result, COUNTER, end_time, rel_time))
        old_time = end_time

if __name__ == "__main__":
    main()
