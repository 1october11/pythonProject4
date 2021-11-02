
i = [x**3 for x in range (100) if  x%2 != 0]
lower = 1
upper = 1000
n = 7
for i in range(lower, upper + 1):
    if(i % n == 0):
        print(i)