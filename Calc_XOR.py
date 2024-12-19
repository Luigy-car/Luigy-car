# Función para calcular XOR
def xor_bytes(a, b):

    # Variables que toman dos num Hex
    a = bytes.fromhex(a)
    b = bytes.fromhex(b)
    # Realiza el XOR
    return ''.join(f'{x ^ y:02x}' for x, y in zip(a, b))

# Tipea inputs para el calculo de manera manual 
if __name__ == "__main__": # Descubro el porque del __name__ == "__main__"
    input_1 = "B1EF2ACFE2BAEEFF"
    input_2 = "91BA13BA21AABB12"
    input_3 = "B98A15BA31AEBB3F"

    # Calculo segun inputs
    print("--------------------------------------------------------")
    print(f"{input_1} XOR {input_2} = {xor_bytes(input_1, input_2)}")
    print("--------------------------------------------------------")
    print(f"{input_1} XOR {input_3} = {xor_bytes(input_1, input_3)}")
    print("--------------------------------------------------------")
