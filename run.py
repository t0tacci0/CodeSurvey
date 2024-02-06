import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style, init
import time
import re


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
    print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to the Code Survey Program!\n")
    time.sleep(5)
    print(f"{Fore.GREEN}{Style.BRIGHT}This survey is made to help people to have a better vision of coding")
    print(f"{Fore.GREEN}{Style.BRIGHT}and at the same time to get information from answers.\n")
    time.sleep(6)
    print(f"{Fore.GREEN}{Style.BRIGHT}Soon you will be asked a series of questions.")
    print(f"{Fore.GREEN}{Style.BRIGHT}Please answer truthfully and enjoy!\n")
    time.sleep(5)

    while True:
        user_name = input(f"{Fore.YELLOW}{Style.BRIGHT}Please enter your name: ")
        print()
        if re.match("^[a-zA-Z ]+$", user_name):
            break
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid name. Please enter a valid name containing only letters and spaces.")

    print(f"{Fore.YELLOW}{Style.BRIGHT}Hello, {user_name}! Thank you for participating in the Code Survey.\n")
    time.sleep(3)
    print(f"{Fore.YELLOW}{Style.BRIGHT}Get Ready!")
    print(Style.RESET_ALL)


def homepage():
    while True:
        print(f"{Fore.GREEN}{Style.BRIGHT}1. Take Survey")
        print(f"{Fore.GREEN}{Style.BRIGHT}2. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): ")

        if choice == '1':
            take_survey()
        elif choice == '2':
            print(f"{Fore.YELLOW}{Style.BRIGHT}Exiting the Code Survey Program...")
            print(f"{Fore.YELLOW}{Style.BRIGHT}Hope to see you soon!")
            break
        else:
            print("Invalid choice. Please enter 1 to take the survey or 2 to exit.")

def take_survey():
    print("Survey started!")

    # First survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 1: Why are you interested in coding?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Personal Growth")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. School")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. Change Career")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            # Add code to record the answer in the survey data
            print("Answer recorded. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

welcome()
homepage()