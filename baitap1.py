chuoi_dau_vao = input("Nhập: ")
do_dai = len(chuoi_dau_vao)
print(f"Độ dài chuỗi: {do_dai}")   
print("Số lần xuất hiện:")
dem_ky_tu = {}
for ky_tu in chuoi_dau_vao:
    dem_ky_tu[ky_tu] = dem_ky_tu.get(ky_tu, 0) + 1
for ky_tu, so_lan in dem_ky_tu.items():
    print(f"  - Ký tự '{ky_tu}': {so_lan} lần")