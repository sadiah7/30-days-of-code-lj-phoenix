# Given a number N. The task is to find the sum of N Harmonic Number.
# Let the nth harmonic number be Hn. The harmonic series is as follows:
# H1 = 1
# H2 = H1 + 1/2
# H3 = H2 + 1/3
# H4 = H3 + 1/4
# . . .
# Hn = Hn-1 + 1/n
num = int(input())
h = 1
for i in range(1, num):
    h = h + (1/(i+1))
print("Harmonic sum upto 4 decimal places:", "{:0.4f}".format(h))
