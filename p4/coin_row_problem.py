import time


COUNTER = 0
COINS = [None, 5, 1, 2, 10, 6, 2]


def v1(n):
    global COUNTER, COINS
    if n == 0:
        return 0
    if n == 1:
        return COINS[1]
    COUNTER += 1
    max_coin = max({COINS[n - 1] + v1(n - 2), v1(n - 1)})
    return max_coin


# counter pode estar mal
def main():
    global COUNTER
    print("%8s %8s %8s %8s" % ("n", "result", "COUNTER", "time"))
    for n in range(0, 7):
        COUNTER = 0
        start_time = time.time()
        result = v1(n)
        end_time = time.time() - start_time
        print("%8d %8d %8d %6f" % (n, result, COUNTER, end_time))

if __name__ == "__main__":
    main()
