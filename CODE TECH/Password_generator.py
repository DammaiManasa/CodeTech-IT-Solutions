import random
import string

#taking inputs from user
length = int(input("Enter the desired length of the password in integers : "))
complexity = input("Enter the desired complexity level (SIMPLE/MEDIUM/DIFFICULT): ").upper()
    

#defining func to return required password to user based on complexity mentioned by the user
def password_generator(length, complexity):
    if complexity == "SIMPLE":
        chars = string.ascii_letters 
    elif complexity == "MEDIUM":
        chars = string.ascii_letters + string.digits
    elif complexity == "DIFFICULT":
        chars = string.ascii_letters + string.digits + string.punctuation

    try:
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    except BaseException as be:
         print("Invalid complexity level. Please choose 'SIMPLE','MEDIUM','DIFFICULT'.",be) 
        

Password =password_generator(length, complexity)#func calling
if Password!=None:
 print("Generated Password:", Password)#printing generated password on the console 



