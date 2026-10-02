from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = "thisisonelongkey"  # 16 bytes = AES-128
key_bytes = bytes(key, "utf-8")
print("Key: " + key)

iv = bytes(16)
aes_cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))

plaintext = "thebestplaintext"
plaintext_bytes = bytes(plaintext, "utf-8")
print("Plaintext: " + plaintext)

padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_bytes = padder.update(plaintext_bytes) + padder.finalize()

aes_encryptor = aes_cipher.encryptor()
ciphertext_bytes = aes_encryptor.update(padded_bytes) + aes_encryptor.finalize()
ciphertext = ciphertext_bytes.hex()
print("Ciphertext: " + ciphertext)

aes_decryptor = aes_cipher.decryptor()
padded_bytes_2 = aes_decryptor.update(ciphertext_bytes) + aes_decryptor.finalize()

unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
plaintext_bytes_2 = unpadder.update(padded_bytes_2) + unpadder.finalize()
plaintext_2 = str(plaintext_bytes_2, "utf-8")
print("Original Plaintext: " + plaintext_2)
