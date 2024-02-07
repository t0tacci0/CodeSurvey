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

def welcome():
    print(f"{Fore.GREEN}{Style.BRIGHT}System loading.....")
    time.sleep(5)
    clear()
    print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to the Code Survey Program!\n")
    time.sleep(5)
    print(f"{Fore.GREEN}{Style.BRIGHT}This survey is made to help people to have a better vision of coding")
    print(f"{Fore.GREEN}{Style.BRIGHT}and at the same time to get information from answers.\n")
    time.sleep(6)
    print(f"{Fore.GREEN}{Style.BRIGHT}Soon you will be asked a series of questions.")
    print(f"{Fore.GREEN}{Style.BRIGHT}Please answer truthfully and enjoy!\n")
    time.sleep(5)
    clear()

    while True:
        user_name = input(f"{Fore.YELLOW}{Style.BRIGHT}Please enter your name: ")
        print()
        if re.match("^[a-zA-Z]+$", user_name):
            break
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid name. Please enter a valid name containing only letters.")
        

    print(f"{Fore.YELLOW}{Style.BRIGHT}Hello, {user_name}! Get Ready for the Code Survey.\n")


def clear():
    # Check the OS and clear the screen
    if os.name == 'nt':  # This is for Windows
        os.system('cls')
    else:  # This is for Linux and macOS
        os.system('clear')    


def homepage():
    while True:
        print(f"{Fore.GREEN}{Style.BRIGHT}1. Take Survey")
        print(f"{Fore.GREEN}{Style.BRIGHT}2. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): ")

        if choice == '1':
            take_survey()
        elif choice == '2':
            print()
            print(f"{Fore.YELLOW}{Style.BRIGHT}Exiting the Code Survey Program...")
            print(f"{Fore.YELLOW}{Style.BRIGHT}Hope to see you soon!")
            break
        else:
            print("Invalid choice. Please enter 1 to take the survey or 2 to exit.")

def take_survey():
    print()
    print("Survey started!")
    time.sleep(3)
    clear()

    # First survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 1: Are you interested in coding?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Personal Growth")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. School")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. Change Career")
    print(f"{Fore.CYAN}{Style.BRIGHT}4. No")

    while True:
        answer = input("Enter your choice (1, 2, 3 or 4.): ")

        if answer in ['1', '2', '3', '4']:
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

    if answer == '1' or answer == '3':
        # Survey sub-question 1
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: What study program are you interested in?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. Full Stack Web Development")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. Software Developer")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}3. Data Engineer")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}4. Game Development")
        
        while True:
            sub_answer = input("Enter your choice (1, 2, 3, or 4): ")

            if sub_answer in ['1', '2', '3', '4']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")        

    # Second survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 2: How many hours you would spend per week to study?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. 15-25")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. 25-35")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. 35+")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if answer == '1' or answer == '2':
        # Survey sub-question 1
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: Are you working in the while?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. Yes, full-time.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. Yes, Part-time.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}3. No.")
        
        while True:
            sub_answer = input("Enter your choice (1, 2 or 3): ")

            if sub_answer in ['1', '2', '3']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")        

    # Third survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 3: Do you have any background in Coding?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Really not too much.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Yes , i do.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. No, totally new in this.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Fourth survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 4: Are you mentally active?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Yes , i am.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Not actually.")

    while True:
        answer = input("Enter your choice (1 or 2): ")

        if answer in ['1', '2']:
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    # Fifth survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 5: Do you prefer working on remote or in office?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Remote.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Hybrid.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. In Office.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")                             

welcome()
homepage()