def bin_to_hex(binary_str):
    decimal_num = int(binary_str, 2)  
    hex_num = hex(decimal_num)[2:].upper()  
    return hex_num

binaries = ['10101', '10110111', '111000', '1101101']
for binary in binaries:
    hex_result = bin_to_hex(binary)
    print(f"Biner: {binary} → Heksadesimal: {hex_result}")