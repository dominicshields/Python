def encrypt(plaintext,cipher):
    ciphertext = ""
    for x in plaintext:
        i = 0
        for y in cipher:
            if x == y:
                ciphertext += cipher[i+2:i+3]
                break
            i += 1
    return ciphertext

def decrypt(ciphertext,cipher):
    plaintext = ""
    for x in ciphertext:
        i = 0
        for y in cipher:
            if x == y:
                plaintext += cipher[i-1:i]
                break
            i += 1
    return plaintext

cipher = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza"
plaintext = "the quick brown fox jumps over the lazy dog"
ciphertext = encrypt(plaintext,cipher)
print(ciphertext)
decryptedtext = decrypt(ciphertext,cipher)
print(decryptedtext)