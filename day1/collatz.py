# The Collatz sequence is generated sequentially where
# n = n / 2 if n is even
# n = 3 * n + 1 if n is odd
# And the sequence ends if n = 1
n = int(input())
ls = []
ls.append(n)
while(1):
    if(n % 2 == 0):
        n = n/2
        ls.append(n)
    else:
        n = 3*n + 1
        ls.append(n)
    if(n == 1):
        break
print(len(ls))
