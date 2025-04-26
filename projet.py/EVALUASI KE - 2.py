# Konversi pecahan desimal ke biner
def decimal_to_binary_fraction(decimal, precision=6):
    binary = []
    for _ in range(precision):
        decimal *= 2
        bit = int(decimal)
        binary.append(str(bit))
        decimal -= bit
    return '0.' + ''.join(binary)

# Bukti untuk 53/64
binary_frac = decimal_to_binary_fraction(53/64)  # Output: '0.110101'
decimal_value = int('110101', 2) / 2**6          # Output: 0.828125 (53/64)