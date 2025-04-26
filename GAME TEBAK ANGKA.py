import random

def main():
    print("=== SELAMAT DATANG DI GAME TEBAK ANGKA ===")
    print("Saya telah memilih sebuah angka antara 1 hingga 100.")
    print("Coba tebak angka tersebut! Anda memiliki 7 kesempatan.\n")
    

    angka_rahasia = random.randint(1, 100)
    kesempatan = 7  

    while kesempatan > 0:
        try:
            
            tebakan = int(input("Masukkan tebakan Anda: "))
            
           
            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar!")
                break
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
        
        kesempatan -= 1
        print(f"Sisa kesempatan Anda: {kesempatan}\n")
    
    if kesempatan == 0:
        print(f"Kesempatan habis! Angka rahasianya adalah {angka_rahasia}.")
    print("=== GAME OVER ===")

if __name__ == "__main__":
    main()