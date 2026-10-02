from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7

key = input("Enter AES key: ").encode("utf-8")
ciphertext_hex = input("Enter ciphertext (hex): ").strip()

try:
	ciphertext = bytes.fromhex(ciphertext_hex)
except ValueError:
	raise SystemExit("Ciphertext must be a hexadecimal string.")

if not ciphertext or len(ciphertext) % 16 != 0:
	raise SystemExit("Ciphertext must contain complete 16-byte AES blocks.")

try:
	decryptor = Cipher(algorithms.AES(key), modes.CBC(bytes(16))).decryptor()
	padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

	unpadder = PKCS7(algorithms.AES.block_size).unpadder()
	plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
	print("Plaintext: " + plaintext.decode("utf-8"))
except (ValueError, UnicodeDecodeError) as error:
	raise SystemExit("Decryption failed. Check the key and ciphertext.") from error

	