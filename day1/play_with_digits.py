# Take 'n' as the first line of input ('n' is total number of digits).
# Then input the number with 'n' digits in new line.
# Find the sum of digits and product of digits and then the difference of them.
def digits():
    n = int(input())
    num = int(input())
    total, prod = 0, 1
    for i in range(n):
        x = num % 10
        total += x
        prod *= x
        num = num//10
    diff = abs(total - prod)
    return diff


print(digits())
