# Raam is superstitious. He will only use a particular digit of number as a roll number
#  if its sum of digits is 11. Find those numbers having sum 11.
# Here, find the Nth number having sum 11.
# So, in short: Given an integer value n, find out the n-th positive integer whose sum is 11.

n = int(input())
num = 29
x = 29
while(1):
    total = 0
    while(x > 0):
        total += x % 10
        x = x // 10
    if(total == 11):
        n -= 1
    if(n == 0):
        print(num)
        break
    x = num + 9
    num += 9
