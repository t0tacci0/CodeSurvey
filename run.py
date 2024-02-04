import gspread
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore, Style, init

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('code_survey')

print(f"{Fore.GREEN}Welcome to the Code Survey Program!")
print(f"{Fore.GREEN}This survey is made to help people to have a better vision of the world of coding")
print(f"{Fore.GREEN}and at the same time to get information from answers.")
print(Style.RESET_ALL)
print(f"{Fore.YELLOW}Please enter your name...")
print(f"{Fore.YELLOW}Name example: MyName")
