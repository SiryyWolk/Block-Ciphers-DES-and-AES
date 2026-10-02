from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


key = input("Enter AES key: ").encode("utf-8")
ciphertext_hex = input("Enter ciphertext (hex): ").strip()

try:
	ciphertext = bytes.fromhex(ciphertext_hex)
except ValueError:
	raise SystemExit("Ciphertext must be a hexadecimal string.")

if not ciphertext or len(ciphertext) % 16 != 0:
	raise SystemExit("Ciphertext must contain complete 16-byte AES blocks.")

try:
	plaintext = Cipher(algorithms.AES(key), modes.ECB()).decryptor().update(ciphertext) + Cipher(algorithms.AES(key), modes.ECB()).decryptor().finalize()
	print("Plaintext: " + plaintext.decode("utf-8"))
except (ValueError, UnicodeDecodeError) as error:
	raise SystemExit("Decryption failed. Check the key and ciphertext.") from error
