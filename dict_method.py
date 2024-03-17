# #task1 #dictionary #homework
# def str_counter(strs: list):
#     dct = {}
#     for i in strs:
#         dct.setdefault(len(i), i)
#     return dct

# print(str_counter(["Asror", "qwerty"]))

# #task2 #dictionary #homework
# def merge_list(l1: list, l2: list):
#     dct = {}
#     if len(l1) == len(l2):
#         for i in range(len(l1)):
#             dct.setdefault(l1[i], l2[i])
#     return dct

# l1 = ["Jan", "Feb", "Mar"]
# l2 = [1, 2, 3]
# print(merge_list(l1, l2))

# #task3 #dictionary #homework

# contacts = {"Nodir": 918602711, "Laziz":908002534}
# def add_contact(contact_name: str, contact_num: int):
#     contacts.setdefault(contact_name, contact_num)

# def update_contact(contact_name: str, contact_num: int):
#     contacts[contact_name] = contact_num

# def remove_contact(contact_name):
#     contacts.pop(contact_name)

# def contact():
#     while True:
#         print(f"""
# ************************
# *   What will you do?  *
# *˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜*
# *  1. Add contact      *
# *  2. Update contact   *
# *  3. Delete contact   *
# *  4. Search contact   *
# *  5. Exit             *
# ************************
# """)
#         choose = int(input("Enter menu (1-5): "))
#         if choose > 0 and choose < 5:
#             contact_name = input("Contact name: ")
#             if choose == 1:
#                 if contact_name not in contacts.keys():
#                     phone_num = int(input("Enter number (Ex: 975787678): "))
#                     add_contact(contact_name, phone_num)
#                     print("Success")
#                 else:
#                     print("Contact found in contacts")

#             elif choose == 2:
#                 if contact_name in contacts.keys():
#                     phone_num = int(input("Enter number (Ex: 975787678): "))
#                     update_contact(contact_name, phone_num)
#                     print("Success")
#                 else:
#                     print("Contact name not found")

#             elif choose == 3:
#                 if contact_name in contacts.keys():
#                     remove_contact(contact_name)
#                     print("Contact removed")
#                 else:
#                     print("Contact name not found in contacs")

#             elif choose == 4:
#                 if contact_name in contacts.keys():
#                     print(contacts.get(contact_name))

#         if choose == 5:
#             break
#         else:
#             print("Menu not found")
#         print(contacts)

# contact()

# #task4 #dictionary #homework
# def counter_dict(nums: list):
#     dct = {}
#     for num in nums:
#         count_num = nums.count(num)
#         dct.setdefault(num, count_num)
#     return dct

# print(counter_dict([2, 1, 1, 3, 12, 2, 12, 0, 13]))

#task5 #dictionary #homework
def max_ball_students(students: dict):
    highbrows = {}
    max_point = list(students.values())[0]
    st_max = list(students.keys())[0]
    for student, point in students.items():
        if point > max_point:
            max_point = point
            st_max = student
    highbrows.setdefault(st_max, max_point)
    st1 = students.pop(st_max)

    max_point = 0
    st_max = ""
    for student, point in students.items():
        if point > max_point:
            max_point = point
            st_max = student
    highbrows.setdefault(st_max, max_point)

    return highbrows

ar = max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80 })
print(ar)