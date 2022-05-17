import random
import string


def get_N(p, q):
    return p*q

def phi_of_n(p, q):
    return (p - 1) * (q - 1)

def get_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

# Generate Public and private keys

def get_encryption_key(n, phi_of_n):
    lst = [i for i in range(1, n+1)]
    e_list = []
    for i in lst:
        if (1 < i) and (i < phi_of_n):
            gcd = get_gcd(i, n)
            gcd_phi = get_gcd(i, phi_of_n)
            if (gcd == 1) and (gcd_phi == 1):
                e_list.append(i)
    if len(e_list) == 1:
        return e_list[0]
    else:
        return e_list[random.randint(1, len(e_list)-1)]  


def get_decryption_key(e, phi_of_n):
    d_list = []
    for i in range(e * 25):
        if (e * i) % phi_of_n == 1:
            d_list.append(i)
    return d_list[random.randint(1, len(d_list) - 1)]


p = 11
q = 29
n = get_N(p, q)  # 319
phi_func = phi_of_n(p, q)  # 280
e = get_encryption_key(n, phi_func)
d = get_decryption_key(e, phi_func)
# to avoid key collision
while d == e:
    d = get_decryption_key(e, phi_func)

public_key = [e, n]  # [137, 319]
private_key = [d, n]  # [1633, 319]

# Encryption
def text_to_digits(PT):
    pool = string.ascii_letters + string.punctuation + " "
    M = []
    for i in PT:
        M.append(pool.index(i))
    return M

def digits_to_text(DT):
    pool = string.ascii_letters + string.punctuation + " "
    msg = ''
    for i in DT:
        # print(i)
        msg += pool[i]
    return msg
    
def encrypt(M, public_key):
    return [(i ** public_key[0]) % public_key[1] for i in M]

message = "hello world!"
M = text_to_digits(message)
CT = encrypt(M, public_key)
print("Cipher text: ",CT)

# Decryption
def decrypt(CT, private_key):
    return [((i ** private_key[0]) % private_key[1]) for i in CT]



DT = decrypt(CT, private_key) 
m = digits_to_text(DT)
print("Decrypted text: ", m)