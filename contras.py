import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

amount = int(input("Cuantos caracteres quieres que tenga tu contraseña?:  "))

password = ""

for i in range (amount):
    x = random.choice(caracteres)
    password = password + x

print("Esta es tu contraseña generada automaticamente:", password)
