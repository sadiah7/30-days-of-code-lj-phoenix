n = int(input())


def square():
    return n*n


if square() % 10 == n % 10:
    print("true")
else:
    print("false")
