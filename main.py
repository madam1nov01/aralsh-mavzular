# random --- tasodify son

# choice --- tanlamoq
# randint --- raqam uchun

# met = ["shdc",  "sdhjvbhv",   "chsbsd", "dkjcbdhicb"]
# print(random.choice(met))
# print(random.randint(1,5))
import random

mening_sonim = int(input("0 dan 20 gacha son tanlang: "))
random1 = random.randint(0, 20)

print( mening_sonim)
print( random1)

if mening_sonim == random1:
    print("G‘olibsiz")
elif mening_sonim > random1:
    print("Pastroq son tanlang")
else:
    print("Balandroq son tanlang")
print("Yutqazdingiz")"?:."