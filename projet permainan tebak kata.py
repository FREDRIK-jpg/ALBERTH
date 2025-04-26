import random

def main():
    kata_kunci = ["papeda", "kasbi", "gedi", "sungai", "tanjung"]
    kata_rahasia = random.choice(kata_kunci)
    huruf_ditebak = []
    percobaan = 6

    print("Selamat Datang di permainan Tebak Kata!")
    print("Tebak kata ini berhubungan dengan hal hal sebagai berikut:")
    print("1.makanan khas orang papua.")
    print("2.Tumbuhan Umbi umbian yang sering di konsumsi oleh orang papua.")
    print("3.sayuran yang sering di konsumsi orang papua.")
    print("4.merupakan objek wisata yang terkenal di sorong selatan.")
    print("5.merupakan tempat yang sering di kunjungi di kota sorong pada hari minggu atau weekend.")
    print("Coba ko Tebak Kata ini dengan memasukkan satu huruf pada setiap langkah.")
    print(f"Ko punya {percobaan} kesempatan untuk menebak kata.")
    print("_" * len(kata_rahasia))

    while percobaan > 0:
        tebakan = input("Coba ko tebak kata ini dengan satu huruf?: ").lower()

        if len(tebakan) != 1 or not tebakan.isalpha():
            print("Nanti kas masuk satu huruf saja e.")
            continue

        if tebakan in huruf_ditebak:
            print("bah! ko su tebak tadi baru.")
            continue

        huruf_ditebak.append(tebakan)

        if tebakan in kata_rahasia:
            print("Benar!")
        else:
            print("Salah.")
            percobaan -= 1
            print(f"Sisa kesempatan: {percobaan}")

        kemajuan_kata = ""
        for huruf in kata_rahasia:
            if huruf in huruf_ditebak:
                kemajuan_kata += huruf
            else:
                kemajuan_kata += "_"

        print("Kemajuan: " + kemajuan_kata)

        if "_" not in kemajuan_kata:
            print("Selamat! Ko berhasil menebak kata dengan benar.")
            break

    if percobaan == 0:
        print("Maaf e,Ko pu kesempatan su habis. de pu Kata yang benar tu:", kata_rahasia)


main()