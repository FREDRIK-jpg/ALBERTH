total_belanja = float(input("masukkan total belanja: Rp. "))

if total_belanja < 100000 :
    diskon = 0
elif 100000 <= total_belanja <=500000 :
    diskon = 10
elif 500000 < total_belanja <= 100000 :
    diskon = 20
else:
    diskon = 30

jumlah_diskon = total_belanja * (diskon / 100)
harga_setelah_diskon = total_belanja - jumlah_diskon

print(f"total belannja: Rp.{total_belanja}")
print(f"diskon: {diskon}%")
print(f"jumlah diskon: Rp.{jumlah_diskon}")
print(f"harga setelah diskon: Rp.{harga_setelah_diskon}")
