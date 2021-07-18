# sum(i, i=1 to n)
# f1(n) = n(n+1)/2
# n_iters1(n) = n
def f1(n: int):
    counter = 0
    r = 0
    for i in range(1, n + 1):
        counter += 1
        r += i
    return r, counter


# sum(sum(1, j=1 to n), i=1 to n)
# f2(n) = n**2
# n_iters2(n) = f2(n)
def f2(n: int):
    counter = 0
    r = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            counter += 1
            r += 1
    return r, counter


# sum(sum(1, j=i to n), i=1 to n)
# f3(n) = n(n+1)/2
# n_iters3(n) = f3(n)
def f3(n: int):
    counter = 0
    r = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            counter += 1
            r += 1
    return r, counter


# sum(sum(j, j=1 to i), i=1 to n)
# f4(n) = n(n+1)(n+2)/6
# n_iters4(n) = n(n+1)/2
def f4(n: int):
    counter = 0
    r = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            counter += 1
            r += j
    return r, counter


def main():
    print(f1(10))
    print(f2(10))
    print(f3(10))
    print(f4(10))


if __name__ == "__main__":
    main()
