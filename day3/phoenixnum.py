num = int(input())


def fact(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod


def PhoenixNumber(n):
    total = 0
    while(n > 0):
        total += fact(n % 10)
        n = n//10
    if total == num:
        return "Phoenix Number"
    else:
        return "Not a Phoenix Number"


print(PhoenixNumber(num))
