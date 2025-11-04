chuoi = input("Nhập vào: ")
chuoi_nguoc = chuoi[::-1]
if chuoi == chuoi_nguoc:
    print(f"\nChuỗi '{chuoi}' là một Palindrome.")
else:
    print(f"\nChuỗi '{chuoi}' KHÔNG phải là Palindrome.")
    print(f"(Đọc ngược là: '{chuoi_nguoc}')")