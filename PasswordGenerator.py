import string
import random
length = int(input("Enter password length: "))
print('''Choose type of password :
         1. strong
         2. only Letters
         3. only numbers
         ''')
 
characterList = ""
choice=4
while(choice>3):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        characterList=string.ascii_letters+string.digits+string.punctuation
    elif(choice == 2):
         
        characterList += string.ascii_letters
    elif(choice == 3):
         
        characterList += string.digits
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))
password = []
for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))
