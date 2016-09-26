import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

# Generating a random private and public key
randomGenerator = Random.new().read
privateKey = RSA.generate(1024, randomGenerator)
publicKey = privateKey.publickey()

# Encrypting with public key
encrypted = publicKey.encrypt(str.encode('Message to encrypt'),1024)
print ('Encrypted Message: ', encrypted)

# Decrypting with private key
decrypted = privateKey.decrypt(encrypted)
print ('Decrypted Messsage: ', decrypted.decode())
