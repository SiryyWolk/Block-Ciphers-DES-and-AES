# Block Ciphers: DES and AES

Small Python examples that demonstrate block-cipher encryption and decryption
with AES and DES/3DES. These scripts are for learning, not for protecting real
data.

## Requirements

- Python 3
- `cryptography` for AES
- `des` for DES/3DES

Install the libraries with:

```sh
python -m pip install cryptography des
```

Run a script from this directory with `python <script-name>`. Prompt-based
decryption scripts accept a key as a UTF-8 string and ciphertext as hexadecimal
bytes; see each section for its mode and padding requirements.

## AES

AES encrypts and decrypts 16-byte blocks. The key must be 16, 24, or 32 bytes
(AES-128, AES-192, or AES-256). In these scripts, keys and plaintext are
converted from UTF-8 strings to bytes.

### ECB demo and decryption

Run `python aes_encrypt_decrypt.py` to encrypt and then decrypt a built-in
example. It uses AES-128 in ECB mode with the key `thisisonelongkey` and the
plaintext `thebestplaintext`. Both are exactly 16 bytes, so this example does
not add padding. The script prints the key, plaintext, ciphertext in hex, and
the recovered plaintext.

Run `python AES_decryption.py` to decrypt AES-ECB ciphertext. Enter a valid AES
key and ciphertext as hex. The ciphertext must contain one or more complete
16-byte blocks, and the decrypted bytes are decoded as UTF-8. This script does
not remove padding; use it with ciphertext whose plaintext was not padded.

### CBC decryption

Run `python AES_CBC_decryption.py` to decrypt AES-CBC ciphertext. Enter a valid
AES key and ciphertext as hex. The ciphertext must contain complete 16-byte
blocks. This script uses an all-zero, 16-byte initialization vector (IV), then
removes PKCS#7 padding and prints the UTF-8 plaintext. Its ciphertext must have
been produced with the same key, CBC mode, zero IV, and PKCS#7 padding.

## DES and 3DES

DES operates on 8-byte blocks. `des_encrypt_decrypt.py` demonstrates encryption
and decryption with padding enabled: it uses the 8-byte key `apoorkey` (single
DES) and encrypts the built-in plaintext `Hello`. It also checks how the
`des` library classifies 8-byte and 16-byte keys; a 16-byte key selects two-key
3DES.

Run `python DES_decrytion.py` to decrypt DES/3DES ciphertext. Enter the key
used for encryption and ciphertext as hex. The ciphertext must contain one or
more complete 8-byte blocks. This script decrypts with padding enabled and
decodes the result as UTF-8. Use the same key type and padding convention as
the encrypting program.

## Security notes

- ECB reveals repeated-block patterns and should not be used for real data.
- The CBC example hard-codes a zero IV and does not authenticate ciphertext.
	Real CBC use requires a fresh, unpredictable IV for each encryption and
	authentication; prefer a modern authenticated mode such as AES-GCM.
- DES is obsolete and its effective key strength is inadequate. 3DES is also
	deprecated for new applications. Use a modern authenticated cipher instead.
- These examples print or prompt for keys and do not provide secure key
	management.