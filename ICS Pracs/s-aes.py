# python -m pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32) # Use a stored / generated key
data_to_encrypt = 'This is plain text!' # This is your data

# === Encrypt ===

# First make your data a bytes object. To convert a string to a bytes object, we can call .encode() on it
data = data_to_encrypt.encode('utf-8')

# Create the cipher object and encrypt the data
cipher_encrypt = AES.new(key, AES.MODE_CFB)
ciphered_bytes = cipher_encrypt.encrypt(data)

# This is now our data
iv = cipher_encrypt.iv
ciphered_data = ciphered_bytes
print(ciphered_data)

# From here we now assume that we do not know data_to_encrypt or data (we will use it for proof afterwards
# We do know the iv, data and the key you have stored / generate

# === Decrypt ===

# Create the cipher object and decrypt the data
cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
deciphered_bytes = cipher_decrypt.decrypt(ciphered_data)

# Convert the bytes object back to the string
decrypted_data = deciphered_bytes.decode('utf-8')

# === Proving the data matches ===

# Now we prove that the original data is the same as the data we just ciphered out (running these should throw no errors)
assert data_to_encrypt == decrypted_data, 'Original data does not match the result'
print(data_to_encrypt)