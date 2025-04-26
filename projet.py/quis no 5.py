list_nilai = []
nilai1 = int(input("Input nilai 1: "))
list_nilai.append(nilai1)
nilai2 = int(input("Input nilai 2: "))
list_nilai.append(nilai2)
nilai3 = int(input("Input nilai 3: "))
list_nilai.append(nilai3)
nilai4 = int(input("Input nilai 4: "))
list_nilai.append(nilai4)
nilai5 = int(input("Input nilai 5: "))
list_nilai.append(nilai5)
nilai6 = int(input("Input nilai 6: "))
list_nilai.append(nilai6)
nilai7 = int(input("Input nilai 7: "))
list_nilai.append(nilai7)
nilai8 = int(input("Input nilai 8: "))
list_nilai.append(nilai8)
nilai9 = int(input("Input nilai 9: "))
list_nilai.append(nilai9)
nilai10 = int(input("Input nilai 10: "))
list_nilai.append(nilai10)

def hitung_rata_rata():
    n = 0
    for i in list_nilai:
        n = n + i
    return n / 10

rata_rata = hitung_rata_rata()
terbesar = max(list_nilai)
terkecil = min(list_nilai)

print(f"Bilangan terbesar: {terbesar}")
print(f"Bilangan terkecil: {terkecil}")
print(f"Rata rata: {rata_rata}")
