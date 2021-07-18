import time


COUNTER = 0


def v1(n, j, t):
    global COUNTER
    if n == 0 and j == 0:
        return 1
    COUNTER += 1
    if j == 0:
        return (1 - t) * v1(n - 1, 0, t)
    if n == j:
        return t * v1(n - 1, n - 1, t)
    COUNTER += 1
    return (1 - t) * v1(n - 1, j, t) + t * v1(n - 1, j - 1, t)


def main():
    global COUNTER
    t = 1/2
    print("%8s %8s %8s %8s %8s %8s" % ("n", "j", "t", "result", "COUNTER", "time"))
    for n in range(0, 4):
        for j in range(0, n):
            COUNTER = 0
            start_time = time.time()
            result = v1(n, j, t)
            end_time = time.time() - start_time
            print("%8d %8d %8f %8f %8d %6f" % (n, j, t, result, COUNTER, end_time))


if __name__ == "__main__":
    main()
