import random


COUNTER = 0

def find_n(n, lower_value=1, higher_value=100):
    global COUNTER
    COUNTER += 1
    if lower_value+1 == higher_value:
        print("The number is " + str(lower_value))
        return lower_value
    half = (lower_value + higher_value) // 2
    print("Number is biggest then " + str(half) + " ?", end=" ")
    if n >= half:
        print("y")
        return find_n(n, half, higher_value)
    print("n")
    return find_n(n, lower_value, half)


def main():
    n = random.randint(1, 100)
    print("Number: " + str(n))
    find_n(n)
    print("Iteractions: " + str(COUNTER))


if __name__ == "__main__":
    main()
