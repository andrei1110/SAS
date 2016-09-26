from Crypto.Cipher import AES

# Vars
message = "A 16 message...."
IV = "Encrypting msg.."
key = "1234567891098765"

# Encrypting
obj1 = AES.new(key, AES.MODE_CBC, IV)
ciphertext = obj1.encrypt(message)
print(ciphertext)

# Decrypting
obj2 = AES.new(key, AES.MODE_CBC, IV)
deciphertext = obj2.decrypt(ciphertext)
newMessage = deciphertext.decode()
print(newMessage)
