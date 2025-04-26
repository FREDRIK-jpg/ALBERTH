import math
pilihan = input("masukan oprasi (1: FPB, 2: KPK): ")

def fpb(a, b):
    return math .gcd(a, b)

def kpk(a, b):
    return math.lcm(a, b)

if pilihan == "1":
    a = int(input("input bilangan a: "))
    b = int(input("input bilangan b: "))
    hasil = fpb(a, b)
    print(f"FPB dari {a} dan {b} adalah {hasil}")
elif pilihan == "2":
    a = int(input("input bilangan a: "))
    b = int(input("input bilangan b: "))
    hasil = kpk (a, b)
    print(f"KPK dari {a} dan {b} adalah {hasil}")
else:
    print("operasi tidak valid")