def fibonacci(n):
    fib_sequence = [0, 1]  # Menyimpan dua angka pertama Fibonacci
    while len(fib_sequence) < n:
        # Menambahkan angka Fibonacci berikutnya
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Meminta input dari pengguna
n = int(input("Masukkan jumlah angka Fibonacci yang diinginkan: "))

# Menampilkan hasil deret Fibonacci
print(f"Deret Fibonacci hingga {n} angka:")
print(fibonacci(n))
