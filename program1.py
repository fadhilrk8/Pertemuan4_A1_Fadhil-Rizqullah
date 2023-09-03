#Program Persyaratan SIM
umur = int(input("Masukkan umur anda= "))
nilai = int(input("Masukkan nilai tes anda= "))
lulus = "Selamat, Anda berhak mendapatkan SIM anda"
gagal = "Maaf, anda tidak berhak mendapatkan SIM anda\nSilahkan coba lagi tahun depan"

if(umur > 17):
    if(nilai < 60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)
    