kunlar = ("Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba")
n = int(input("N :"))
k = int(input("K :"))
if n < 1 or n > 7 or k < 1 or k > 365:
    print("Xatolik yuz  berdi")
else:
    son = k % 7
    print(kunlar[son + n - 2])