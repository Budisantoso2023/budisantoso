# belajar perbandingan lanjutan, ELIF

nama = input("masukan nama :")

if nama=="edy":  # kondisi 1
    print("mahasiswa ganteng") # aksi true 1
elif nama=="haryanto":  # kondisi 2
    print("mahasiswa ganteng banget") # aksi true 2
elif nama=="ika":  # kondisi 3
    print("anda kn mahasiswi") # aksi true 3
else:
    print("bukan mahasiswa ganteng") # aksi false
print("program selesai") 

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

# Memilih operasi
operasi = input("Pilih operasi (1 untuk penjumlahan, 2 untuk pengurangan): ")

if operasi == '1':
    # Memasukkan angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    print("Hasil penjumlahan:", penjumlahan(angka1, angka2))
elif operasi == '2':
    # Memasukkan angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    print("Hasil pengurangan:", pengurangan(angka1, angka2))
else:
    print("Operasi tidak valid")

    
