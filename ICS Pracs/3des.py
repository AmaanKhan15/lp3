# python -m pip install pycryptodome

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
# Avoid Option 3
while True:
    try:
        key = DES3.adjust_key_parity(get_random_bytes(24))
        break
    except ValueError:
        pass

cipher = DES3.new(key, DES3.MODE_CFB)
plaintext = b'We are no longer the knights who say ni!'
msg =cipher.encrypt(plaintext)
msg2 = cipher.encrypt(plaintext=plaintext)
print(msg)

decipher = DES3.new(key, DES3.MODE_CFB)
decrypted = decipher.decrypt(msg)
print(decrypted)
