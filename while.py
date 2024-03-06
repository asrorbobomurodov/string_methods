# #task1 #while
# num = int(input("num = "))
# i = 0
# while i < 5:
#     i += 1
#     print(str(i)*i)

# #task2 #while
# num = int(input("Enter number = "))
# sum = 0
# while num:
#     r = num % 10
#     sum += r
#     num //= 10
# print(sum)

# #task3 #while
# i = 1
# sum = 0
# while i < 100:
#     if i % 2:
#         sum += i
#     i += 1
# print(sum)

# #task4 #while
# num = int(input("Enter number : "))
# box = []
# while num:
#     r = num % 10
#     box.append(r)
#     if box[0] < r:
#         box[0] = r
#     num //= 10
# print(box[0])

#task5 #while
import random
user_num = 0
random_num = random.choice(range(1,101))
while user_num != random_num:
    user_num = int(input("Your guess (1-100): "))
    if user_num > random_num:
        print("Your guess number is larger than random number.")
    elif user_num < random_num:
        print("Your guess number is smaller than random number.")
print("You have found random number!!!")