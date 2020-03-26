# # 3/19 販賣機
import vending_machine.vending_service as machine

flag = True

while flag:
    print('\n==============================')
    select = eval(input('1. 儲值\n2. 購買\n3. 查詢餘額\n4. 離開\n請選擇:'))

    if select == 1:  # 儲值
        machine.deposit()

    elif select == 2:  # 購買
        machine.buy()


    elif select == 3:  # 查詢餘額
        print(f"目前餘額為{machine.balance}元")
    elif select == 4:  # 離開
        print("bye")
        flag = False
        break

    else:  # 重新輸入
        print('====請輸入1-4之間====')
        continue
#
# x = 100
# y = 80
#
# def add_weight(w1, w2=1) :
#     result = w1 + w2
#     return result
#
# a = add_weight(x)
# b = add_weight(x, y)
# print(a, b)
#
#
# def calculate(x, y):
#     return x+y ,x-y, x/y, x*y
#
# num1 = 2
# num2 = 5
# result = calculate(num1, num2)
# print(result)
# r1, r2, r3, r4 = calculate(num1, num2)
# print(r1, r2, r3, r4)










