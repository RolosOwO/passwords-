import random, string
long=int(input("длина пароля:"))
password=""
for i in range(long):
    password += random.choice(string.printable)
print(password)
