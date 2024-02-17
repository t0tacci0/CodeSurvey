import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style, init
import time
import re
import os


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('code_survey')


# Colorama colours for the terminal
B_GREEN = Fore.GREEN + Style.BRIGHT  # green color text
B_YELLOW = Fore.YELLOW + Style.BRIGHT  # yellow color text
B_CYAN = Fore.CYAN + Style.BRIGHT  # cyan color text
B_RED = Fore.RED + Style.BRIGHT  # red color text for errors
B_LIGHTMAGENTA_EX = Fore.LIGHTMAGENTA_EX + Style.BRIGHT  # magenta color text


# This function is a introduction to the survey
def welcome():
    print(B_GREEN + f"System loading.....")
    time.sleep(5)
    clear()
    print(B_GREEN + f"Welcome to the Code Survey Program!\n")
    time.sleep(5)
    print(B_GREEN + f"This Survey was created to help people have a better")
    print(B_GREEN + f"understanding of coding and at the same time")
    print(B_GREEN + f"gaining information from answers.\n")
    time.sleep(6)
    print(B_GREEN + f"You will shortly be asked a series of questions.")
    print(B_GREEN + f"Please answer honestly and enjoy the survey!\n")
    time.sleep(5)
    clear()

    while True:
        user_name = input(B_YELLOW + f"Please enter your name: ")
        print()
        if re.match("^[a-zA-Z]+$", user_name):
            break
        else:
            print(B_RED + f"Invalid name.")
            print(B_RED + f"Please enter a valid name with only letters.")
    print(B_YELLOW + f"Hello, {user_name}!Preparing the Code Survey.\n")


def clear():
    # Check the OS and clear the screen
    if os.name == 'nt':  # This is for Windows
        os.system('cls')
    else:  # This is for Linux and macOS
        os.system('clear')


# Menù options
def homepage():
    while True:
        print(B_GREEN + f"1. Take Survey")
        print(B_GREEN + f"2. View Statistics")
        print(B_GREEN + f"3. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice (1, 2 or 3): ")

        if choice == '1':
            take_survey()
        elif choice == '2':
            # Prompt for passphrase
            passphrase = input(f"{Fore.YELLOW}Enter the passphrase: ")
            if passphrase == "surveydone":
                view_statistics()
            else:
                print(B_RED + f"Invalid passphrase. Access denied.")
            view_statistics()
        elif choice == '3':
            print()
            print(f"{Fore.YELLOW}{Style.BRIGHT}Exiting the Code Survey...")
            print()
            time.sleep(2)
            print(f"{Fore.YELLOW}{Style.BRIGHT}Your data will be saved...")
            print()
            time.sleep(2)
            print(f"{Fore.YELLOW}{Style.BRIGHT}Hope to see you soon!")
            break
        else:
            print("Invalid choice. Please enter the correct number.")


def view_statistics():
    # Open the worksheet "user_choices"
    worksheet = SHEET.worksheet("user_choices")

    # Get all values from the worksheet
    all_values = worksheet.get_all_values()
    print(f"{Fore.YELLOW}{Style.BRIGHT}--- Survey Statistics ---")

    # Display statistics for each question
    for i in range(len(all_values[0])):
        question = all_values[0][i]
        choices = [row[i] for row in all_values[1:]]
        total_responses = len(choices)
        print(B_CYAN + f"User Choices {i + 1}: {question}")

        # Count each  user choice
        set_c = set(choices)
        choice_counts = {choice: choices.count(choice) for choice in set_c}

        # Display the choices percentages
        for choice, count in choice_counts.items():
            percentage = (count / total_responses) * 100
            print(B_GREEN + f"{choice}: {count} responses ({percentage:.2f}%)")

        print()


# Survey main function
def take_survey():
    print()
    print("Survey started!")
    time.sleep(3)
    clear()

    user = []

    # First survey question
    print(B_CYAN + f"\nQuestion 1: Are you interested in coding?\n")
    print(B_CYAN + f"1. Yes, for personal growth.")
    print(B_CYAN + f"2. Yes, for my school.")
    print(B_CYAN + f"3. Yes, to change career.")
    print(B_CYAN + f"4. No.")

    while True:
        answer = input("Enter your choice (1, 2, 3 or 4.): ")

        if answer in ['1', '2', '3', '4']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

    # Survey sub-question 1
    print(B_LIGHTMAGENTA_EX + f"\nSub-Question 1: What type of career")
    print(B_LIGHTMAGENTA_EX + f"would you be interested in?\n")
    print(B_LIGHTMAGENTA_EX + f"1. Full Stack Web Development.")
    print(B_LIGHTMAGENTA_EX + f"2. Software Developer.")
    print(B_LIGHTMAGENTA_EX + f"3. Data Engineer.")
    print(B_LIGHTMAGENTA_EX + f"4. Game Development.")

    while True:
        sub_answer = input("Enter your choice (1, 2, 3, or 4): ")

        if sub_answer in ['1', '2', '3', '4']:
            user.append(sub_answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    # Second survey question
    print(B_CYAN + f"\nQuestion 2: How many hours you would")
    print(B_CYAN + f"spend per week to study?\n")
    print(B_CYAN + f"1. 15-25.")
    print(B_CYAN + f"2. 25-35.")
    print(B_CYAN + f"3. 35+.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Survey sub-question 2
    print(B_LIGHTMAGENTA_EX + f"\nSub-Question 2: Are you working now?\n")
    print(B_LIGHTMAGENTA_EX + f"1. Yes, full-time.")
    print(B_LIGHTMAGENTA_EX + f"2. Yes, Part-time.")
    print(B_LIGHTMAGENTA_EX + f"3. No.")

    while True:
        sub_answer = input("Enter your choice (1, 2 or 3): ")

        if sub_answer in ['1', '2', '3']:
            user.append(sub_answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

    # Third survey question
    print(B_CYAN + f"\nQuestion 3: Do you have any background in Coding?\n")
    print(B_CYAN + f"1. I have some knowledge about.")
    print(B_CYAN + f"2. Yes , i do.")
    print(B_CYAN + f"3. No, i'm totally new in Coding.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Survey sub-question 3
    print(B_LIGHTMAGENTA_EX + f"\nSub-Question 3: Where did you acquire")
    print(B_LIGHTMAGENTA_EX + f"this knowledge?\n")
    print(B_LIGHTMAGENTA_EX + f"1. At school or any course paid.")
    print(B_LIGHTMAGENTA_EX + f"2. With free material on internet.")
    print(B_LIGHTMAGENTA_EX + f"3. During your free time as hobby.")

    while True:
        sub_answer = input("Enter your choice (1, 2 or 3): ")

        if sub_answer in ['1', '2', '3']:
            user.append(sub_answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

    # Fourth survey question
    print(B_CYAN + f"\nQuestion 4: Are you mentally active?\n")
    print(B_CYAN + f"1. Yes , i am.")
    print(B_CYAN + f"2. Not actually.")

    while True:
        answer = input("Enter your choice (1 or 2): ")

        if answer in ['1', '2']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    # Survey sub-question 4
    print(B_LIGHTMAGENTA_EX + f"\nSub-Question 4: Do you play sports")
    print(B_LIGHTMAGENTA_EX + f"during your free time?\n")
    print(B_LIGHTMAGENTA_EX + f"1. Yes.")
    print(B_LIGHTMAGENTA_EX + f"2. Not really.")

    while True:
        sub_answer = input("Enter your choice (1 or 2): ")

        if sub_answer in ['1', '2']:
            user.append(sub_answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

    # Fifth survey question
    print(B_CYAN + f"\nQuestion 5: Do you prefer to work at home")
    print(B_CYAN + f"or in the office?\n")
    print(B_CYAN + f"1. Remote.")
    print(B_CYAN + f"2. Hybrid.")
    print(B_CYAN + f"3. In the Office.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Survey sub-question 5
    print(B_LIGHTMAGENTA_EX + f"\nSub-Question 5: Do you prefer")
    print(B_LIGHTMAGENTA_EX + f"to work alone or in a team?\n")
    print(B_LIGHTMAGENTA_EX + f"1. I prefer to work alone at home.")
    print(B_LIGHTMAGENTA_EX + f"2. Absolutely in a team.")
    print(B_LIGHTMAGENTA_EX + f"3. I like to alternate.")

    while True:
        sub_answer = input("Enter your choice (1, 2 or 3): ")

        if sub_answer in ['1', '2', '3']:
            user.append(sub_answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")

    # Sixth survey question
    print(B_CYAN + f"\nQuestion 6: How do you prefer to learn coding?\n")
    print(B_CYAN + f"1. Online courses.")
    print(B_CYAN + f"2. Coding Bootcamps.")
    print(B_CYAN + f"3. Interactive platforms.")
    print(B_CYAN + f"4. Other.")

    while True:
        answer = input("Enter your choice (1, 2, 3 or 4): ")

        if answer in ['1', '2', '3', '4']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

    # Survey sub-question 6
    print(B_LIGHTMAGENTA_EX + f"\nSub-Question 6: What programming")
    print(B_LIGHTMAGENTA_EX + f"languages you want to learn first?\n")
    print(B_LIGHTMAGENTA_EX + f"1. HTML and CSS.")
    print(B_LIGHTMAGENTA_EX + f"2. JAVASCRIPT.")
    print(B_LIGHTMAGENTA_EX + f"3. PYTHON.")
    print(B_LIGHTMAGENTA_EX + f"4. C++.")
    print(B_LIGHTMAGENTA_EX + f"5. Other.")

    while True:
        sub_answer = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if sub_answer in ['1', '2', '3', '4', '5']:
            user.append(sub_answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")

    worksheet = SHEET.worksheet("user_choices")
    worksheet.append_row(user)
    print(B_GREEN + f"\nThank you for partecipating!!")
    print()
    print(B_GREEN + f"\nTo View statistics digit the passphrase 'surveydone'")
    print()


welcome()
homepage()
