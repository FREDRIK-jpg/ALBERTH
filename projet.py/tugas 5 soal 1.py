nama_karyawan = input("masukkan nama: ")
golongan = input("masukkan golongan: ")
jam_kerja = float(input("masukkan jam kerja: "))
total_gaji = 0
def hitung_gaji(upah):
    upah_lembur = 0
    if jam_kerja > 48:
        lembur = jam_kerja-48
        upah_lembur = lembur*4000
    return jam_kerja * upah + upah_lembur

if golongan == "a":
    upah_perjam = 5000
    total_gaji = hitung_gaji(upah_perjam)
elif golongan == "b":
    upah_perjam = 7000
    total_gaji = hitung_gaji(upah_perjam)
elif golongan == "c":
    upah_perjam = 8000
    total_gaji = hitung_gaji(upah_perjam)
elif golongan == "d":
    upah_perjam = 10000
    total_gaji = hitung_gaji(upah_perjam)
else:
    print("golongan tidak valid")

print(f"nama karyawan: {nama_karyawan}")
print(f"golongan: {golongan}")
print(f"gaji: {total_gaji}")
