# Given a decimal number as input, we need to write a program
# to convert the given decimal number into equivalent binary number.
num = int(input())
op = ''
while(num > 0):
    i = num % 2
    op += str(i)
    num = num // 2
print(op[::-1])
