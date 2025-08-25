import string
import random

print("~ ~ ~ WELCOME TO SIMPLE CALCULATOR ~ ~ ~")
print("---------------------------------")
# input for password length
length = int(input("Please enter password length: "))
print("Choose character set for password: ") 
print("1. LETTERS")
print("2. DIGITS")         
print("3. SPECIAL CHARACTERS")     
print("4. EXIT")
print("---------------------------------")

characterList = ""

# Getting character set for password
while(True):
    choice = int(input("Pick a number: "))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")

password = []

for i in range(length):
    # Picking a random character 
    randomchar = random.choice(characterList)
    
    # Appending a random character to password
    password.append(randomchar)

print("The random password is " + "".join(password))
print("THANKS FOR USING THE PASSWORD GENERATOR. HAVE A NICE DAY :)")
