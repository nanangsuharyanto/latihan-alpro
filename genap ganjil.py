#input bilangan
bilangan = int(input("Masukkan bilangan: "))

#menentukan ganjil genap
def cek_bilangan(bilangan):
    if bilangan % 2 == 0:
        print(f"{bilangan} adalah bilangan genap")
    else:
        print(f"{bilangan} adalah bilangan ganjil")
    return bilangan

#mengalikan bilangan setelahnya
bilangan_setelahnya = bilangan+1
hasil = bilangan*bilangan_setelahnya

#menampilkan hasil
print(f"Hasil perkalian dari {bilangan} dengan bilangan setelahnya ({bilangan_setelahnya}) adalah {hasil}")
