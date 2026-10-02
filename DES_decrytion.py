from des import DesKey


key = input("Enter DES key: ").encode("utf-8")
ciphertext_hex = input("Enter ciphertext (hex): ").strip()

try:
	ciphertext = bytes.fromhex(ciphertext_hex)
except ValueError:
	raise SystemExit("Ciphertext must be a hexadecimal string.")

if not ciphertext or len(ciphertext) % 8 != 0:
	raise SystemExit("Ciphertext must contain complete 8-byte DES blocks.")

try:
	plaintext = DesKey(key).decrypt(ciphertext, padding=True)
	print("Plaintext: " + plaintext.decode("utf-8"))
except (ValueError, UnicodeDecodeError) as error:
	raise SystemExit("Decryption failed. Check the key and ciphertext.") from error
