import random
import string
import time
import os

# Function to validate the password
# Define a list of valid passwords
valid_passwords = ['ILoveGracie', 'AaronKing', 'LoveIsPain']

# Function to validate the password
def validate_password(password):
    return password in valid_passwords

# Function to generate a random code
def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a custom key
def generate_custom_key(segment_length, num_segments):
    segments = [''.join(random.choices(string.ascii_uppercase, k=segment_length)) for _ in range(num_segments)]
    return '-'.join(segments)

# ANSI escape code for red text
red_text = "\033[91m"
# ANSI escape code for purple text
purple_text = "\033[95m"
# ANSI escape code for resetting text color to default
reset_text = "\033[0m"

# The text you want to make red
text = """
  _________           .___                                 .___          _____ ___.                  .__               __  .__               
 /   _____/____     __| _/____   ____   ______ ______ _____|   | ______ /  _  \\_ |__   ____   _____ |__| ____ _____ _/  |_|__| ____   ____  
 \\_____  \\\\__  \\   / __ |/    \\_/ __ \\ /  ___//  ___//  ___/   |/  ___//  /_\\  \\| __ \\ /  _ \\ /     \|  |/    \\\\__  \\   __\\  |/  _ \\ /    \\ 
 /        \\/ __ \\_/ /_/ |   |  \\  ___/ \\___ \\ \\___ \\ \\___ \\ |   |\\___ \\/    |    \\ \\_\\ (  <_> )  Y Y  \\  |   |  \\/ __ \\|  | |  (  <_> )   |  
/_______  (____  /\\____ |___|  /\\___  >____  >____  >____  >|___/____  >____|__  /___  /\\____/|__|_|  /__|___|  (____  /__| |__|\\____/|___|  
        \\/     \\/      \\/    \\/     \\/     \\/     \\/     \\/         \\/        \\/    \\/             \\/        \\/     \\/                    \\/ 
"""

# Print the text in red
print(red_text + text + reset_text)

# Set the terminal window title with "MadeWithGracieInHeart" in purple color
os.system("title MadeWithGracieInHeart")



# Loop until the correct password is entered
while True:
    # Ask the user to input the password
    password = input("Enter A Product Key: ")

    # Validate the password
    if validate_password(password):
        # Print "Key Is True" in purple with a heart
        print(purple_text + "Only For Aaron.ly Key Is True \u2764" + reset_text + ". You may proceed.")
        # Your code for generating custom keys or other features can be placed here
        break  # Exit the loop when the correct password is entered
    else:
        print("Invalid password. Please try again.")

# Main menu loop

def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    print("Options:")
    print("1. Discord Nitro Promo Codes")
    print("2. $1.25 RoBux Codes")
    print("3. How Strong is your love?")
    print("4. Quit")

    choice = input("Select an option: ")

    if choice == '1':
        try:
            num_codes = int(input("Yh Just put any amount you wanna try/CheckerSoon "))
            if num_codes <= 0:
                print("Please enter a positive number.")
                continue

            code_length = 21  # Adjust the length as needed
            generated_codes = [generate_random_code(code_length) for _ in range(num_codes)]

            print("Generated Promo Codes:")
            for code in generated_codes:
                promo_url = "https://discord.com/billing/promotions/" + code
                print(promo_url)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '2':
        try:
            num_keys = int(input("So um.. Just put in the amount you want to generate: "))
            if num_keys <= 0:
                print("Please enter a positive number.")
                continue

            segment_length = 5
            num_segments = 3

            print(f"{num_keys} Robux Codes:")
            for _ in range(num_keys):
                custom_key = generate_custom_key(segment_length, num_segments)
                print(custom_key)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '3':
        name = input("What is their name?: ")
        try:
            love_strength = int(input(f"How Strong is your love for {name}? Enter The Value: "))
            if love_strength <= 0:
                print("Please enter a positive number.")
                continue

            print(
                "\x1b[31;1m" + f"YOU LOVE {name.upper()} SO MUCH WOW FUCKING ROMANTICAL\n" * love_strength + "\x1b[0m")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please select a valid option.")
    
    input("Click Enter To Return")
