import json
import jks
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Ruta al archivo keystore
keystore_path = "/home/luigy/Desktop/Bootcamp/CriptoGrafía/cripto-main/Practica/KeyStorePracticas" 
# Contraseña para abrir el keystore
keystore_password = "123456" 
# Alias de la clave en el keystore 
alias_clave = "cifrado-sim-aes-256"
# Contraseña de la clave específica
clave_password = "123456"  

# Cargar el keystore
keystore = jks.KeyStore.load(keystore_path, keystore_password)

# Acceder a la clave específica usando el alias y la contraseña de la clave
entry = keystore.secret_keys[alias_clave]
if not entry.is_decrypted():
    entry.decrypt(clave_password)  # Desencriptar la clave con su contraseña


# Datos cifrados en Base64
txt_cifrado = "TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI="
iv_bytes = bytes([0] * 16)

# Extrae la clave en formato bytes
clave = entry.key  

# Decodificar texto cifrado desde Base64
txt_cif_bytes = b64decode(txt_cifrado) 

# Configurar el cifrador AES en modo CBC
cipher = AES.new(clave, AES.MODE_CBC,iv_bytes)

# Descifrar los datos
descifrado_bytes = cipher.decrypt(txt_cif_bytes)

# Eliminar padding (PKCS#7)
descifrado = unpad(descifrado_bytes, AES.block_size)

# Texto descifrado para mostrar tamaño en bytes
texto = "Esto es un cifrado en bloque típico. Recuerda, vas por el buen camino. Ánimo."

print("-----------------------------------------------------")
print(f"Dato en claro: {descifrado.decode('UTF-8')}")

# Se muestra tamaño texto cifrado 80 bytes
print("-----------------------------------------------------")
print(f"Tamaño del texto cifrado en bytes: {len(b64decode(txt_cifrado))}")

# Se muestra tamaño texto 79 bytes
print("-----------------------------------------------------")
print(f"Tamaño en bytes (UTF-8): {len(texto.encode('utf-8'))}")