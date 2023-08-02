import time
import getpass
import bcrypt
import os.path

# Creates a file for a username and password that holds usernames and passwords for users

# Encrypts password
def encrypt(password):
    hashpassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashpassword

# Compares password with encrypted password
def checkpw(password,hashpw):
    ans = bcrypt.checkpw(password.encode('utf-8'), hashpw)
    return ans

# Prompts user to create a password and requires them to retype to ensure no typos
def createpassword():
    password = getpass.getpass("Create a password:   ")
    secondp = getpass.getpass("Please enter your password again:   ")
    if (password != secondp):
        print("passwords do not match, please try again \n")
        createpassword()

    else:
        return password
    
# Prompts user to create a password and requires them to retype to ensure no typos
def enterpassword():
    password = getpass.getpass("Enter the password:   ")
    secondp = getpass.getpass("Please enter your password again:   ")
    if (password != secondp):
        print("passwords do not match, please try again \n")
        enterpassword()

    else:
        return password

# Prompts user to enter password twice in order to avoid typos
def createa(file):
    if (os.path.isfile(file)): #check if file exisits in path
        print("account already exists")
        return
    else:
        password = createpassword()

        with open(file, 'wb') as f:
            f.write(encrypt(password))
        
        print("account created")

# Prompts user to log into account then log their username and password for a site
def createp(file,pw):
    if (os.path.isfile(file)): #check if user exists
        with open(file, 'rb') as r:
            userpw = r.readline()
        
        if(checkpw(pw,userpw)): #checking if password matches the one in file
            src = input("Website/src name:      ")
            username = input("Enter the username:   ")
            pw = enterpassword()
            with open(file, 'a') as w:
                w.write("\n%s   %s   " % (src, username))
                        
            with open(file, 'ab') as ab:
                ab.write(encrypt(pw))

            print("username and password successfully stored")
            
        else:
            newpass = getpass.getpass("incorrect password, please try again")
            createp(file,newpass)
            return
        
        return
    else:
        print("username does not exist")
        return

# Users can check and update passwords
def manage(file,password):
    return

def main():
    while True:
        option = int(input("What operation would you like to perform?\n Type 1 to Create a new account\n Type 2 to Generate a new password\n Type 3 to Manage passwords \n Type 4 to Exit Password manager\n"))
        if (option == 1):
            user = input("Enter your username:   ")
            file = str(user) + ".txt"
            createa(file)
        elif (option == 2):
            user = input("Enter your username:   ")
            file = str(user) + ".txt"
            password = getpass.getpass("Enter your password:   ")
            createp(file,password)
        elif (option == 3):
            user = input("Enter your username:   ")
            file = str(user) + ".txt"
            password = getpass.getpass("Enter your password:   ")
            manage(file, password)
        elif (option == 4):
            break
        else:
            option = int(input("Invalid option try again: \n"))
    return

if __name__ == "__main__":
    main()