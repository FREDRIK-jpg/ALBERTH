try:
    angka = float(input("Masukkan sebuah angka: "))  # Mengubah input menjadi tipe float
except ValueError:
    print("Input tidak valid! Masukkan angka yang benar.")
else:

    if angka > 0:
        print("Keputusan: Angka tersebut adalah bilangan positif.")
        print("Saran: Bilangan positif biasanya digunakan untuk menghitung hal-hal seperti pendapatan atau keuntungan.")
    elif angka < 0:
        print("Keputusan: Angka tersebut adalah bilangan negatif.")
        print("Saran: Bilangan negatif sering digunakan untuk menggambarkan kerugian atau hutang.")
    else:
        print("Keputusan: Angka tersebut adalah nol.")
        print("Saran: Nol sering dianggap sebagai titik awal atau netral dalam penghitungan.")