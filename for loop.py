# task3 #for
# num = int(input("Enter last number:"))
# sum = 0
# for i in range(num+1):
#     if i % 3 == 0 and i % 9 != 0:
#         sum += i
# print(sum)

# #task5 #for
# word = list(input("Write something: "))
# indx = int(input("Enter index (1 - {})".format(len(word))))
# del word[indx-1]

# s = ''
# for i in word:
#     s += i
# print(s)

# #task7 #for
# a = int(input("Enter a:"))
# b = int(input("Enter b (b > a): "))

# for i in range(b - 1, a, -1):
#     print(i)

# print("   Length: {}".format(len(range(a+1, b))))

# #task9 #for
# cost  = float(input("Cost of item (1 kg) = "))
# i = 0.1
# for _ in range(10):
#     print(round(cost * i, 3))
#     i += 0.1

# #task10 #for
# a = int(input("Enter a = "))
# b = int(input("Enter b = "))
# sum = 0

# for i in range(a + 1 ,b):
#     sum += i ** 2
#     print(i ** 2)

# print(f"Sum = {sum}")

# #task11 #for
# a = int(input("Enter a = "))
# n = int(input("Enter n = "))

# for i in range(1, n+1):
#     print(a ** i)

#task12 #for
n = int(input("Enter n = "))
total = 1
for i in range(1, n + 1):
    total *= i
print(total)







