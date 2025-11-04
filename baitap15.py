s = input()
daucau = '.,!?'
for i in daucau:
    s = s.replace(i, '')
dstu = s.split()
dem = {}
for i in dstu:
    if i in dem:
        dem[i] += 1
    else:
        dem[i] = 1
sapxep = sorted(dem.items(), key=lambda item: item[1], reverse=True)
for i in sapxep:
    print(i)