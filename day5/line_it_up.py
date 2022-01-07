n = 10
a = 3
b = 4
start = a + 1
count = 0
while(start <= n):
    if(start > a and n-start <= b):
        count = n-start+1
        break
    start += 1
print(count)
