import random
chars="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
length=int(input("Enter the length of the password: "))

password=""

for i in range(length):
    password+=random.choice(chars)
print(f"The password is: {password}")