# one file code
print("JAWAB PERTANYAAN DIBAWAH DENGAN y/t SAJA!")
inv = "Jawaban Invalid"
tndklnjt = "Sedang atau pernah mengalami:\n- demam(>38c)\n- pilek\n- batuk\n- sesak napas?"
sehat = "Anda tidak perlu memeriksakan diri Anda. Selalu jaga kesehatan"
layanan = "Hubungi 119 EXT 9 atau periksakan diri ke rumah sakit rujukan COVID-19 di daerah anda"

soal1 = input("Pernah kontak dengan pasien positif covid-19(berada dalam satu rungan yang sama atau kontak dalam jarak 1 meter)\natau pernah berkunjung ke negara atau daerah endemis covid-19 dalam 14 hari terakhir..?:\n")
# control flow soal1
if soal1 == "y":
    # control flow soal2
    soal2a = input(tndklnjt)
    if soal2a == "y":
        print(layanan)
    elif soal2a == "t":
        print("Karantina diri Anda semenjak 14 hari terhitung dari hari kunjungan")
        soal3 = input("Selama karantina 14 hari mengalami:\n- demam(>38c)\n- pilek\n- batuk\n- sesak napas?")
        if soal3 == "y":
            print(layanan)
        elif soal3 == "t":
            print(sehat)
        else:
            print(inv)
    else:
        print(inv)
elif soal1 == "t":
    soal2b = input(tndklnjt)
    if soal2b == "y":
        print(layanan)
    elif soal2b == "t":
        print(sehat)
    else:
        print(inv)
else:
    print(inv)