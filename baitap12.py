a = list(map(int, input().split()))
b = set(a)
xuathien = 0
solan = 0
for i in b:
    dem = a.count(i)
    if dem > xuathien:
        xuathien = dem
        solan = i
print(solan)
print(xuathien)