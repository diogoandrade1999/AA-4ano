import time

COUNTER = 0
def fibonacci(n):
    global COUNTER
    if n == 0 or n == 1:
        return n
    COUNTER += 1
    return fibonacci(n-1) + fibonacci(n-2)


def main():
    global COUNTER
    print("%4s %8s %8s %6s" % ("n", "result", "COUNTER", "time"))
    for n in range(10, 30):
        COUNTER = 0
        start_time = time.time()
        result = fibonacci(n)
        print("%4d %8d %8d %6f" % (n, result, COUNTER, (time.time() - start_time)))

if __name__ == "__main__":
    main()
