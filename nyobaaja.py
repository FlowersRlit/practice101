def pertama():
    print("Selamat datang di Alien Shooter!\nPilihlah salah satu warna:\n0. Kuning\n1. Hijau\n2. Merah")
    
    warna_alien = int(input("Masukkan angka: "))
    
    if warna_alien == 1:
        print("Anda mendapatkan 20 poin")
    elif warna_alien == 0:
        print("Anda mendapatkan 10 poin")
    elif warna_alien == 2:
        print("Anda mendapatkan 10 poin")
    else:
        print("Maaf, nomor invalid")

def kedua():
    namaUser = input("Masukkan nama Anda: ")
    umurUser = int(input("Masukkan umur Anda: "))
    
    if umurUser < 2:
        print("Halo, " + namaUser + " ade bayi yang imut, huehue")
    elif 2 <= umurUser < 4:
        print("Anaknya udah balita ya, " + namaUser + "!")
    elif 4 <= umurUser < 13:
        print(namaUser + " masih anak-anak, jangan sokap jadi orang")
    elif 13 <= umurUser < 20:
        print("Kalo udah dewas jangan kek anak kecil dong, " + namaUser + "!")
    elif 20 <= umurUser < 60:
        print("Halo bapak/ibu senior " + namaUser +", mohon kerjasamanya!")
    else:
        print("weh, nilai yg dimasukkin kok gaada")

def ketiga():
    toppingPizza = ["keju", "daging", "sosis", "jagung"]
    
    for x in toppingPizza:
        print("Tambah topping", x, "dong")