# #task1 #functions
# def user_data(first_name, last_name, age):
#     print(f"""
# Name : {first_name}
# Surname: {last_name}
# Age: {age}
# """)

# first_name = input("First name: ")
# last_name = input("Last name: ")
# age = int(input("Your age: "))

# user_data(first_name, last_name, age)

# #task2 #functions #homework
# def find_max(a, b, c):
#     maxx = a
#     max_variable = "a"
#     if maxx < b:
#         maxx = b
#         max_variable = "b"
#     if maxx < c:
#         maxx = c
#         max_variable = "c"

#     if a == b and a == c:
#         max_variable = "A and B and C"
#     elif a == b:
#         max_variable = "A and B"
#     elif a == c:
#         max_variable = "A and C"
#     elif b == c:
#         max_variable = "B and C"

#     return f"Max number is - {max_variable} = {maxx}"

# a = int(input('a = '))
# b = int(input('b = '))
# c = int(input('c = '))

# print(find_max(a, b, c))

# #task3 #functions #homework
# def find_letter_count(word, letter):
#     return f'"{letter}" {word.count(letter)} time(s) in {word}'

# print(find_letter_count('Asror', "r"))

# #task4 #functions #homework
# def list_sum(myList: list):
#     summ = 0
#     for num in myList:
#         summ += num
#     return summ

# print(list_sum([3, 5, 9, 11]))

# #task6 #functions #homework
# def square4(a: int | float, b, c, d):
#     return f"{a}**{b} = {a**b} \n\
# {a}**{c} = {a**c} \n\
# {a}**{d} = {a**d}"

# num = square4(4,2,3,1)
# print(num)

# #task7 #functions #homework
# def digit_count_and_sum(word):
#     summ = 0
#     for item in word:
#         if item.isdigit():
#             summ += int(item) 
#     return summ

# print(digit_count_and_sum("23adss42v 3"))

# #task8 #functions #homework
# def add_right(a: int, b: int): 
#     return int(str(b) + str(a))

# number = add_right(4, 8)
# print(number)

# #task10 #functions #homework
# def work_with_list(a: list):
#     i = 0
#     minn = a[0]
#     while len(a) > i:
#         if a[i] < minn:
#             minn = a[i]
#         i += 1

#     array = []
#     for num in a:
#         array.append(num * minn)
    
#     return array

# multiplies = work_with_list([3,2,6,45,11])
# print(multiplies)

# #task11 #functions #homework
# def big_sale(sales: dict):
#     month_sales = list(sales.keys())
#     prices = list(sales.values())
#     max_price = prices[0]

#     for i in range(len(sales)):
#         if max_price < prices[i]:
#             max_price = prices[i]
#             month = month_sales[i]

#     return month

# sales = {
#   "January": 12000,
#   "March": 6000,
#   "Aprel": 15000,
#   "September": 9000,
#   "December": 10000,
# }

# print(big_sale(sales=sales))

# #task12 #functions #homework
# def min_max(numbers: list | set | tuple, max_num, min_num) -> bool:
#     return max(numbers) == max_num and min(numbers) == min_num

# print(min_max({2,4,5,2,8,99,102}, 102, 2))

#task13 #functions #homework
def expensive_product(products: list):
    expensive = products[0]['price']
    for product in products:
        price = product.get("price")
        if expensive < price:
            expensive = price
            expensive_product = product.get("name")
    return expensive_product

products = [{
    "name": "Iphone X",
    "price": 600
  },
  {
    "name": "Iphone 12",
    "price": 1500
  },
  {
    "name": "Samsung Note 9",
    "price": 800
  },
  {
    "name": "Samsung S10",
    "price": 1100
  },
]

print(expensive_product(products))