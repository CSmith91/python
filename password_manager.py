'''
This is a basic password manager. It prompts the user to add or view passwords. 
On adding a password, the script adds this information to a txt file. While this is viewable to anyone, the password info is encrypted such that the information cannot be viewed by others.
This project can be taken further with the addition of setting (and changing) a master password at the beginning as a 'log in'
'''

from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb") #reading bytes
    key = file.read() # reading the file
    file.close() # closing the file
    return key # returning the key

key = load_key()
# we key we created and combine this with the master_password to allow us access
fer = Fernet(key)


# this was used to create the initalise the key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def view():
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            #print(line.rstrip()) # removes the carriage return
            data = line.rstrip()
            user, password = data.split("|")
            # we do the opposite of what we did in the 'add' function, where we decrypt
            print("User:", user, ",  " "Password:", fer.decrypt(password.encode()).decode())         

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # this  lets us automatically close the file as the operations are completed, as opposed to 'open' 'close'
    # 'w' will clear any existing file and make an entirely new one
    # 'r' just reads the file
    # 'a' append mode - allows us to add somethng to the end of an exisitnig file, OR createe a new file if the file doesn't exist
    with open('passwords.txt', 'a') as file:
        # we need to encode our password pwd first of all, as this converts it to bytes
        # we then encrypt this password
        # and we also need to decode it afterwards to make it a readable string
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add), or press q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Type 'add', 'view' or 'q' to quit.")
        continue