number = 0
data_angka = []

while number <= 1000:
    input_user = float(input("Masukkan angka yang akan dirata-ratakan : "))
    
    data_angka.append(int(input_user))
    total_angka = sum(data_angka)

    number += 1
    jumlah_angka = number
    print("Apakah cukup data di atas? [Y/N] ")
    jawab = input().upper()
    
    if jawab == "Y":
        print("Total angka yang dimasukkan", total_angka)
        print("Jumlah angka yang dimasukkan", jumlah_angka)
        average = total_angka / jumlah_angka
        print("Rata-rata bilangan yang Anda masukkan adalah = ", average)
        break
    else:
        continue
else:
    print("Maaf program ini terbatas hanya dapat menghitung sejumlah", number, "kali")
