
# Función para calcular XOR
def xor_bytes(a, b):

    # Variables que toman dos num Hex
    a = bytes.fromhex(a)
    b = bytes.fromhex(b)
    # Realiza el XOR
    return ''.join(f'{x ^ y:02x}' for x, y in zip(a, b))

# Operación XOR 
if __name__ == "__main__": # Descubro el porque del __name__ == "__main__"
    input_1 = "B1EF2ACFE2BAEEFF"
    input_2 = "91BA13BA21AABB12"

    print(f"{input_1} XOR {input_2} = {xor_bytes(input_1, input_2)}")
