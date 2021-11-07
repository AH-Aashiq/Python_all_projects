#Password Genaretor
import random

print("Welcome to Password Genaretor Tools")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = int(input("Amout of password to genarate: "))

length = int(input("Input your password length: "))

print("\nHere your passwords list")
for pwd in range(number):
     password =''
     for c in range(length):
          password += random.choice(chars)
     print(password)
#End of Programme
