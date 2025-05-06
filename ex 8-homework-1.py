數字 = []
for i in range(10):
    數字.append(int(input("請輸入十個整數 :")))

x = 0
y = 0 
z = 0 

for i in range(10):
    if 數字[i] > 0:
        x += 1
    elif 數字[i] == 0:
        y += 1
    else:
        z += 1

print(f"正數有{x}個")
print(f"零有{y}個")
print(f"負數有{z}個")
