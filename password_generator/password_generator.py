import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        # basic AND logic below 
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special # and means that if has_number is false, it doesnt matter what has_special is, we still return false
        
    return pwd
        

min_length = int(input("PLease enter the minimum length of your password: ")) # assuming valid user input
has_number = input("Including numbers? (y/n) ").lower() == "y"
has_special = input("Including special chars? (y/n) ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print(f"The generated password is: {pwd}")