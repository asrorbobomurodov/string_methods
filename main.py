""" Python string methods """

name, surname, age = "Asror", "BoboMurodov", 20

txt = "my Name Is Asror"

# Gapdagi 1-so'zni bosh harfga, 
# qolganlarni kichik harfga o'zgartiradi!
result = txt.capitalize()
print(result)
### Output: "My name is asror"

# Barcha harflarni kichik harfga o'zgartitish
result = txt.casefold()
print(result)
### Output: "my name is asror"

# String ma'lumotni n ta belgi o'rtasida joylashtirish
result = name.center(20, "*")
print(result)

result2 = name.center(10, " ")
print(result2)
### Output: "*******Asror********"
### Output: "  Asror   "

# String ma'lumot ichidan biror qiymatni necha marta takrorlanishi
# string.count(value, start, end)
result = txt.count("asror")
print(result)
result2 = txt.count("m")
print(result2)
### Output: 0
### Output: 2

# encoding (UTF-8 to ASCII)
s_utf8 = "This is U†ƒ-8"
result = s_utf8.encode()
print(result)
### Output: b'This is U\xe2\x80\xa0\xc6\x92-8'

# string.endswith(value, start, end) 
# qiymatni start va stop oralig'ida va qiymat stop indeksiga to'g'ri kelishi
result = txt.endswith("Asror")
result2 = txt.endswith("my", 1, 3)
print(result)
print(result2)
### Output: True
### Output: False

# string.expandtabs(tabsize) "\t" - belgidan keyingi n ta space tashlash
word = "t\ta\tb\ts\ti\tz\te"
print(word)
print(word.expandtabs(2))
print(word.expandtabs(5))
### Output: "t       a       b       s       i       z       e"
### Output: "t a b s i z e"
### Output: "t    a    b    s    i    z    e"

# string.find(value, start, end) - valueni start va end orasidan qidiradi va indeksni qaytaradi
result = txt.find("Is")
result2 = txt.find("Asror", 5,10)
print(result)
print(result2)
### Output: 8
### Output: -1 (not found)

# string.isalnum() - matn faqat raqam va harflardan iborat ekanligni tekshiradi
print("54".isalnum())
print("Age24".isalnum())
print("School 52".isalnum())
### Output: True
### Output: True
### Output: False

# string.isalpha() - matn faqat harflardan iborat ekanligni tekshiradi
print("Asror Bobomurodov".isalpha())
print("Text".isalpha())
### Output: False
### Output: True

# string.isascii() - matn ASCII belgilaridan iborat ekanligni tekshiradi
print("ASCII characters 32".isascii())
print(" Asror™ ".isascii())
### Output: True
### Output: False

# string.isdecimal() - matn faqat raqamlardan iborat ekanligni tekshiradi
print("42".isdecimal())
print("12-42".isdecimal())
print("20.2".isdecimal())
### Output: True
### Output: False
### Output: False

# string.isdecimal() - matn faqat raqamlardan iborat ekanligni tekshiradi
print("42".isdecimal())
print("12-42".isdecimal())
print("20.2".isdecimal())
print("\u00B2".isdecimal()) # False
### Output: True
### Output: False
### Output: False
### Output: False

# string.isdigit() - *
print("\u00B2".isdigit())
### Output: True





















