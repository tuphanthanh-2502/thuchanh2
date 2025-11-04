n = input("Nhập: ")
nguyenam = "ueoai"
songuyenam = 0
sophuam = 0
for i in n:
    if i in nguyenam:
        songuyenam += 1  
    else:
        sophuam += 1
print(songuyenam)
print(sophuam)


