# python -m pip install pycryptodome

from Crypto.Cipher import DES
key = '11001101'
iv = '11111111'
cipher = DES.new(key, DES.MODE_OFB,iv)
plaintext = 'This is the plain text to be encrypted  '
msg =cipher.encrypt(plaintext)
print(msg)
decipher = DES.new(key, DES.MODE_OFB,iv)

decrypted = decipher.decrypt(msg)
print(decrypted)