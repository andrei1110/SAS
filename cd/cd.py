#Para sha256
import hashlib
#Para RSA
from Crypto.PublicKey import RSA
from Crypto import Random

def calculate_sha256(arq):
	##Read BUF_SIZE bytes each time
	BUF_SIZE = 65536
	sha256 = hashlib.sha256()
	with open(arq, 'rb') as f:
	    while True:
	        data = f.read(BUF_SIZE)
	        if not data:
	            break
	        sha256.update(data)
	return sha256.hexdigest()

random_generator = Random.new().read
key = RSA.generate(2048, random_generator)

public_key = key.publickey()

##Create and encrypt the hash
file_hash = calculate_sha256("file.txt")
enc_file_hash = public_key.encrypt(file_hash.encode(encoding='UTF-8'), 32)

print (input('Pause to modify the file. Press Enter to continue.'))

##Decrypt the hash and compare with the file
dec_file_hash = key.decrypt(enc_file_hash)
file_hash = calculate_sha256("file.txt").encode(encoding='UTF-8')

##Compare the sent hash with the generated hash
if(dec_file_hash == file_hash):
	print ("That is the original file!")
else:
	print ("The file has been modified!")