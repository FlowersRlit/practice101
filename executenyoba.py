# linked to nyobaaja.py
from nyobaaja import pertama
from nyobaaja import kedua
from nyobaaja import ketiga

opsi = int(input("Mau liat soal yang mana? [0-2]:"))

if opsi == 0:
    pertama()
elif opsi == 1:
    kedua()
elif opsi == 2:
    ketiga()
else:
    print("Invalid number")