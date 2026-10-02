from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# AES in ECB mode.  Each block is encrypted independently (no IV).
# Note: ECB is insecure for real use because identical plaintext blocks
# produce identical ciphertext blocks, revealing patterns in the data.

key = "thebestsecretkey"  # 16 bytes = AES-128
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

aes_cipher = Cipher(algorithms.AES(key_bytes), modes.ECB())
aes_encryptor = aes_cipher.encryptor()
aes_decryptor = aes_cipher.decryptor()

# Plaintext must be a multiple of the block size (16 bytes) in ECB mode
plaintext = "thebestplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

ciphertext_bytes = aes_encryptor.update(plaintext_bytes) + aes_encryptor.finalize()
ciphertext = ciphertext_bytes.hex()
print("Ciphertext: " + ciphertext)

plaintext_bytes_2 = aes_decryptor.update(ciphertext_bytes) + aes_decryptor.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
