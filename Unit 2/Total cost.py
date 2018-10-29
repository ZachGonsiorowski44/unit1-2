import math

a = int(input())

b = float(input())

n = int(input())

print(math.floor((n*a)+(n*(b/100))) , (((n*a)+(n*(b/100)))
- math.floor((n*a)+(n*(b/100))))*100)