from des import DesKey


key_short = "superkey"                                              #Key 1
key_short_des = DesKey(bytes(key_short, "utf-8"))
ciphertext_hex = input("Enter ciphertext (hex): ").strip()

try:
	ciphertext = bytes.fromhex(ciphertext_hex)
except ValueError:
	raise SystemExit("Ciphertext must be a hexadecimal string.")

if not ciphertext or len(ciphertext) % 8 != 0:
	raise SystemExit("Ciphertext must contain complete 8-byte DES blocks.")

try:
	plaintext = key_short_des.decrypt(ciphertext, initial=bytes(8), padding=True)
	print("Plaintext: " + plaintext.decode("utf-8"))
except (ValueError, UnicodeDecodeError) as error:
	raise SystemExit("Decryption failed. Check the key and ciphertext.") from error
