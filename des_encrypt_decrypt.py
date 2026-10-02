from des import DesKey

# DES (Data Encryption Standard).  This uses the `des` library (not `cryptography`).
# DES uses 56-bit keys and is considered insecure; 3DES uses two or three keys.

key_short = "apoorkey"
key_short_des = DesKey(bytes(key_short, "utf-8"))

print("Short Key: " + key_short)
print("Short Key Single?: " + str(key_short_des.is_single()))  # 8 bytes = single DES
print("Short Key Triple?: " + str(key_short_des.is_triple()))

key_long = "thebestsecretkey"  # 16 bytes = triple DES (two-key)
key_long_des = DesKey(bytes(key_long, "utf-8"))

print("Long Key: " + key_long)
print("Long Key Single?: " + str(key_long_des.is_single()))
print("Long Key Triple?: " + str(key_long_des.is_triple()))

key_des = key_short_des

plaintext = "thebestplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

ciphertext_bytes = key_des.encrypt(plaintext_bytes)
ciphertext = ciphertext_bytes.hex()
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = key_des.decrypt(ciphertext_bytes)
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
