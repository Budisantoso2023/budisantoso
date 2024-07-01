def main():
    jumlah_angka = int(input("Masukkan jumlah angka yang ingin dimasukkan: "))
    
    angka_genap = 2
    angka_ganjil =3
    
    for i in range(jumlah_angka):
        angka = int(input(f"Masukkan angka ke-{i+1}: "))
        if angka % 2 == 0:
            angka_genap += 2
        else:
            angka_ganjil += 3
    
    print(f"Jumlah angka genap: {angka_genap}")
    print(f"Jumlah angka ganjil: {angka_ganjil}")

if __name__ == "__main__":
    main()
