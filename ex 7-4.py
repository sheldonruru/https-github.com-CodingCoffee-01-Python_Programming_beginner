def add(x, y):
    return x + y
def mul(x, y):
    return x * y
def sub(x, y):
    if z == 1:
        return x - y
    if z == 2:
        return y - x
def div(x, y):
    if z == 1:
        return x / y
    if z == 2:
        return y / x
x = int(input("請輸入數字 :"))
y = int(input("請輸入數字 :"))
if x > y:
    z = 1
else:
    z = 2
print("x+y =",add(x ,y))
print("x*y =",mul(x ,y))
print("x-y =",sub(x ,y))
print("x/y =",div(x ,y))
