import random
N = 1000000
point = 0
for i in range(N):
    x = random.random()
    y = random.random()
    if(x*x + y*y < 1.0):
        point += 1
result = 4.0 * point/N
print(result)