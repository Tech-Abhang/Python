#To make random password for websites basic level project
 
import random

length=int(input("enter a length : "))
char="abcdefghijklmnopqrstuvwxyz1234567890@#$%^&*~!?"

password=""

for a in range(length):
    password+=random.choice(char)


print("Passowrd is: ",password)