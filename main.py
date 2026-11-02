import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    """Generate a password of at least min_length with the requested character types."""
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    # Build the pool from which password characters can be selected.
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    
    password = ""
    meets_criteria = False
    has_number = False
    has_special = False
    
    # Keep adding characters until the length and requested character types are satisfied.
    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special 

    # Return the generated value; the caller decides how to display or use it.
    return password


# Collect the desired password length and optional character types from the user.
min_length = int(input("Enter the length of your password: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").lower() == "y"

# Generate the password with those options, then display it.
new_password = generate_password(min_length, has_number, has_special)
print("Your password:\n")
print(new_password) 
