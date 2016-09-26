mod = 23
base  = 5

privateKey = int(input("Private Key: "))

print("Result: ",(base ** privateKey) % mod)

res = int(input("Inter key: "))

print("Result: ",(res ** privateKey) % mod)
