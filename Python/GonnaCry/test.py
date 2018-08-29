from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import pickle

# const variables
server_public_key = ("""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxF5BOX3N5UN1CsHpnfuU
58lOw0+scQ39hOn6Q/QvM6aTOnYZki57O6/JtgV2CetE+G5IZrRwYPAipFdChGM9
RNZVegpnmGQCSRPlkfjN0TjfCFjaUX80PgRVm0ZHaeCeoNjit0yeW3YZ5nBjPjNr
36BLaswJo1zbzhctK2SYX+Miov04D3iC83Vc8bbJ8Wiip4jpKPDFhyO1I3QkykL0
4T1+tQXaGujLzc3QxJN3wo8rWkQ4CaLAu1pb9QkdYhFG0D3TrljkRNiH0QnF3Asc
XAQNI94ZPaqD6e2rWcSy2ZMiKVJgCWA40p9qe34H8+9ub3TgC52oSyapwbxzqs5v
DQIDAQAB
-----END PUBLIC KEY-----""")

server_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAxF5BOX3N5UN1CsHpnfuU58lOw0+scQ39hOn6Q/QvM6aTOnYZ
ki57O6/JtgV2CetE+G5IZrRwYPAipFdChGM9RNZVegpnmGQCSRPlkfjN0TjfCFja
UX80PgRVm0ZHaeCeoNjit0yeW3YZ5nBjPjNr36BLaswJo1zbzhctK2SYX+Miov04
D3iC83Vc8bbJ8Wiip4jpKPDFhyO1I3QkykL04T1+tQXaGujLzc3QxJN3wo8rWkQ4
CaLAu1pb9QkdYhFG0D3TrljkRNiH0QnF3AscXAQNI94ZPaqD6e2rWcSy2ZMiKVJg
CWA40p9qe34H8+9ub3TgC52oSyapwbxzqs5vDQIDAQABAoIBAC3HA1GRwGQH+8sM
NZf8xFPcnB3v/vVEG6vWl98rl61k0cG5MnDfoR7i9hUW5NOfIy7/FqXKvr/6ezjw
lrMiJ3BavwZ6Ung2KEo89zG2XNS/e08I16xUCSvD+uj90zwdfx1kMkYk+G299H/C
B4DCoA074xj8g+qvhRZgVMle5B7F/gdun6AUGSxHC5uFmibM39MmMuSH16oJGcn5
0VRBmaB8vqMOFIyVKraoX4XAQwKE3by/VTM0kxBjmUZeUs2C1Paag7g09TuzQbXm
y3Tsv4aCZwrZlEXaFHopGz3HVHot2Ps3Qaq8WD76+SbzBm3pHayo3cDXvQwC1L7O
i/bihAkCgYEA23sqvBSVdMtWF+ktSXkt2OfVJsFpp3ym+qm2U5q9M+BTeyf4dnfP
/+Z5O5x6blFyf7ug8h2+8b0L6o34QfuaSXbJBtpmFS2GqG8B3KAYC4nnxonUxGuZ
ECc7wJRvo22A55rKVicmDWWr8rqNmbrNy9eoWUNYvNEouwr9nSW2Z9MCgYEA5QqW
rkUnmbIFd5gEKX+m9IKTUZ+dbuh1oHO3QqgmpeyZdxIvNa5C3bwuk6WBFGMjtCNl
NZeLGN8plcwlPxGEdCBTnhmKw0ikQWubYCx/NNNI2sWXidiym2bHI+2JkdOVx0HA
OU27+sbxyjqExCID+9b+c+t3MKZlzshif7L/YZ8CgYBLu8ZVO+0ObhN5ELbVwYC2
ddixFNA2QOcFW4ZUdvKOcfucZYBwsIsPTCHNFgORCX2u4bl5khYPKCJyfyaI7h6g
9uILAVV0PU9X02YbEQr7AEz/zxOh61bXohIWM6IKDIEMafcjn0KcINciXIj74N+e
VP38PybhkHKzh+lXTmoQjQKBgBKDHZSuUDoS8nAtIED+aU8f8qpJPV9GeKNkVu6T
SrRkgC7okFpFYHAtkpIqcVllffBEYBzJx9tVxjWuT2BemRcNudRweg+4olYLTX6j
ehCZ9yx/hfUFR8JZt0THITRhJpz5SoEXMFdflxFiU3LK0Qmc4eoaoQKUoGvrNFLf
89Y/AoGABgsbLx258EPtVqgY9uS9ta/XpUyKKjVGIqEY+jhn9lNhxQK+0iRQvD6C
eSopcx2e09eODLXAxOpi+f6K2mxJVMjxhvIthnad4vhtJjaBojaMG23+uOpX9Gj/
u7KSAN0pGuIw57saMWU1KFy2POKHI8+PP4rGeJhKx6isAt+3ZFk=
-----END RSA PRIVATE KEY-----"""

def encrypt(msg, key):
    line = msg
    n = 127
    x = [line[i:i+n] for i in range(0, len(line), n)]

    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    cifrado = []
    for i in x:
        ciphertext = cipher.encrypt(i)
        cifrado.append(ciphertext)
    return cifrado

def decrypt(enc, key):
    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)

    decifrado = ""
    for i in enc:
        ciphertext = cipher.decrypt(i)
        decifrado += ciphertext
    return decifrado

cifrado = encrypt(server_private_key, server_public_key)
with open('encrypted_private_key.key', 'wb') as output:
    pickle.dump(cifrado, output, pickle.HIGHEST_PROTOCOL)


with open('encrypted_private_key.key', 'rb') as input:
    enc = pickle.load(input)

decoded = decrypt(enc, server_private_key)

print(decoded, decoded == server_private_key)