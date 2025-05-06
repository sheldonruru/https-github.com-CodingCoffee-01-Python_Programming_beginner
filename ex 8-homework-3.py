while True:
    數字 = []
    錯誤 = False
    for i in range(5):
        成績 = int(input(f"請輸入第 {i+1} 位學生的成績："))
        if 成績 < 0 or 成績 > 100:
            print("輸入的數字必須介於 0 到 100！請重新輸入全部成績。")
            錯誤 = True
            break 
        數字.append(成績)
    if 錯誤:
        continue
    if sum(數字) > 500:
        print("總成績不可超過 500，請重新輸入。")
        continue
    break
總數 = sum(數字)
平均數 = int(總數 / 5)
print(f"平均成績是：{平均數}")
