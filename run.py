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
    print(f"{Fore.GREEN}Welcome to the Code Survey Program!\n")
    time.sleep(5)
    print(f"{Fore.GREEN}This survey is made to help people to have a better vision of coding")
    print(f"{Fore.GREEN}and at the same time to get information from answers.\n")
    time.sleep(6)
    print(f"{Fore.GREEN}Soon you will be asked a series of questions.")
    print(f"{Fore.GREEN}Please answer truthfully and enjoy!\n")
    time.sleep(5)

    while True:
        user_name = input(f"{Fore.YELLOW}Please enter your name: ")
        print()
        if re.match("^[a-zA-Z ]+$", user_name):
            break
        else:
            print(f"{Fore.RED}Invalid name. Please enter a valid name containing only letters and spaces.")

    print(f"{Fore.YELLOW}Hello, {user_name}! Thank you for participating in the Code Survey.\n")
    time.sleep(3)
    print(f"{Fore.YELLOW}Get Ready!")
    print(Style.RESET_ALL)


def homepage():
    while True:
        print(f"{Fore.GREEN}1. Take Survey")
        print(f"{Fore.GREEN}2. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice (1 or 2): ")

        if choice == '1':
            take_survey()
        elif choice == '2':
            print(f"{Fore.YELLOW}Exiting the Code Survey Program...")
            print(f"{Fore.YELLOW}Hope to see you soon!")
            break
        else:
            print("Invalid choice. Please enter 1 to take the survey or 2 to exit.")



welcome()
homepage()