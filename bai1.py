# Nhập dữ liệu từ bàn phím
m = int(input())
v = int(input())
t = int(input())
d = input()

# Tính toán vị trí dừng lại
if d == 'A':
    result = (v * t) % m
else:
    result = (m - (v * t) % m) % m

# In kết quả
print(result)
