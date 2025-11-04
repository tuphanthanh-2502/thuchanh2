a = list(map(int, input().split()))
tongc = 0
for i in a:
    if i % 2 == 0:
        tongc += i
print(tongc)