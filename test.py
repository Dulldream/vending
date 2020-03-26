#
#mathScores = [60, 70, 10, 20 , 81, 63, 4]
# print(mathScores[0])
# firstItem = f'first item in mathScore is {mathScores[0]}'
# print(firstItem)
#
# for i in range(len(mathScores)):
#     print(i,mathScores[i])

# family = {
#     'dad' : 'Homer',
#     "mom" : 'Marge',
#     'son' : 'Bart',
#     'daughter' : 'Lisa'
# }
# for member in family.items():
#     print(member)
#
# for key, value, in family.items():
#     print(f"my {key} is {value}")
#
# mathScores = [60, 70, 10, 20 , 81, 63, 4]
# for i in range(len(mathScores)):
#     print(mathScores[i]**0.5*10)
# for j in mathScores:
#     print(j ** 0.5 * 10)

# for i in range(10):
#     print(i)
#
# [print(i) for i in range(10)]
# import math
# [print(math.sqrt(x)*10) for x in mathScores]

# count = 0
# while count<10 :
#     print(count)
#     count += 1
# else:
#     print("LOL")


# for score in mathScores:
#     if score > 80:
#         continue
#     print(score)

# import random
# i = random.randint(1, 3)
# print(i)
#
# rows = eval(input('How many rows:'))
# print(type(rows))

# #1.九九乘法表
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in a :
#     for j in b :
#         print(f'{i}*{j} = {i*j}')
#
#
#
# #2
# count = 0
# while count <51:
#     print("你好" , end=" ")
#     count+=1
# else:
#     print("我說完了")
#
# #3
# num = eval(input("enter a number"))
# for i in range(1 , num+1):
#     if i % 2 == 1:
#         print(i)

#4
# import random
# ls = []
# rows = eval(input("row_number:"))
# columns = eval(input("col_number"))
# for i in range(rows) :
#     ls.append([])
#     for j in range(columns):
#         num = random.randint(0, 100)
#         ls[i].append(num)
# for rows in ls :
#     for value in rows:
#         print(f"{value}", end=" ")
#     print()



mathscoes = [10, 202, 30]

for idx, score in enumerate(mathscoes):
    print(idx, score)









