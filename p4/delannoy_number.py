import time


COUNTER = 0


def v1(m, n):
    global COUNTER
    if m == 0 or n == 0:
        return 1
    COUNTER += 2
    return v1(m - 1, n) + v1(m - 1, n - 1) + v1(m, n - 1)


def v2(m, n):
    global COUNTER
    assert (m >= 0 and m >= 0)

    d = [[None] * (n + 1) for i in range(m + 1)]
    
    for j in range(n + 1):
        d[0][j] = 1

    for i in range(1, m + 1):
        d[i][0] = 1

        for j in range(1, n + 1):
            COUNTER += 2
            d[i][j] = d[i - 1][j] + d[i - 1][j - 1] + d[i][j - 1]
    return d[m][n]


def main():
    global COUNTER
    print("%8s %8s %8s %8s %8s" % ("m", "n", "result", "COUNTER", "time"))
    for m in range(10, 11):
        for n in range(10, 11):
            COUNTER = 0
            start_time = time.time()
            result = v1(m, n)
            end_time = time.time() - start_time
            print("%8d %8d %8d %8d %6f" % (m, n, result, COUNTER, end_time))
    print('--------------------------------------------')
    for m in range(10, 11):
        for n in range(10, 11):
            COUNTER = 0
            start_time = time.time()
            result = v2(m, n)
            end_time = time.time() - start_time
            print("%8d %8d %8d %8d %6f" % (m, n, result, COUNTER, end_time))


if __name__ == "__main__":
    main()
