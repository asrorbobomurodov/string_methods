#task29 #if-else
#calendar #day of the week

k = int(input("Enter day of the year (1-365): "))
n = int(input("Enter 1st january day of the week (1-7): ")) 

r = n - 1
week = (k + r) // 7 + 1
day_week = (k % 7 + n - 1) % 7

if day_week == 1:
    print(f'week: {week}, Monday of the week')
elif day_week == 2:
    print(f'week: {week}, Tuesday of the week')
elif day_week == 3:
    print(f'week: {week}, Wednesday of the week')
elif day_week == 4:
    print(f'week: {week}, Thursday of the week')
elif day_week == 5:
    print(f'week: {week}, Friday of the week')
elif day_week == 6:
    print(f'week: {week}, Saturday of the week')
elif day_week == 0:
    print(f'week: {week}, Sunday of the week')
