數字 = []
for i in range(5):
    數字.append(int(input("請請輸入5位學生的成績 ：")))

總數 = sum(數字)
平均數 = int(總數 / 5)
print(f"平均成績是：{平均數}")
