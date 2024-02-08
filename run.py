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
    print(f"{Fore.GREEN}{Style.BRIGHT}This Survey was created to help people have a better understanding of coding")
    print(f"{Fore.GREEN}{Style.BRIGHT}and at the same time gaining information from answers.\n")
    time.sleep(6)
    print(f"{Fore.GREEN}{Style.BRIGHT}You will shortly be asked a series of questions.")
    print(f"{Fore.GREEN}{Style.BRIGHT}Please answer honestly and enjoy!\n")
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
        print(f"{Fore.GREEN}{Style.BRIGHT}2. View Statistics")
        print(f"{Fore.GREEN}{Style.BRIGHT}3. Exit")
        choice = input(f"{Fore.YELLOW}Enter your choice (1, 2 or 3): ")

        if choice == '1':
            take_survey()
        elif choice == '2':
            view_statistics()
        elif choice == '3':
            print()
            print(f"{Fore.YELLOW}{Style.BRIGHT}Exiting the Code Survey Program...")
            print()
            time.sleep(2)
            print(f"{Fore.YELLOW}{Style.BRIGHT}Your data will be saved for statistics...")
            print()
            time.sleep(2)
            print(f"{Fore.YELLOW}{Style.BRIGHT}Hope to see you soon with more questions!")
            break
        else:
            print("Invalid choice. Please enter 1 to take the survey or 2 to exit.")        

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
        print(f"{Fore.CYAN}{Style.BRIGHT}Question {i + 1}: {question}")
        
        # Count each  user choice
        choice_counts = {choice: choices.count(choice) for choice in set(choices)}
        
        # Display the choices percentages
        for choice, count in choice_counts.items():
            percentage = (count / total_responses) * 100
            print(f"{Fore.GREEN}{Style.BRIGHT}{choice}: {count} responses ({percentage:.2f}%)")
        
        print()                     

def take_survey():
    print()
    print("Survey started!")
    time.sleep(3)
    clear()

    user = []

    # First survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 1: Are you interested in coding?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Yes, for personal growth.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Yes, for my school.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. Yes, to change career.")
    print(f"{Fore.CYAN}{Style.BRIGHT}4. No.")

    while True:
        answer = input("Enter your choice (1, 2, 3 or 4.): ")

        if answer in ['1', '2', '3', '4']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")      

    if answer == '1' or answer == '3':
        # Survey sub-question 1
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: What type of career would you be interested in?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. Full Stack Web Development.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. Software Developer.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}3. Data Engineer.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}4. Game Development.")
        
        while True:
            sub_answer = input("Enter your choice (1, 2, 3, or 4): ")

            if sub_answer in ['1', '2', '3', '4']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")
                    

    # Second survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 2: How many hours you would spend per week to study?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. 15-25.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. 25-35.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. 35+.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if answer == '1' or answer == '2':
        # Survey sub-question 2
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: Are you working at the moment?")
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
    print(f"{Fore.CYAN}{Style.BRIGHT}1. I have some knowledge about.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Yes , i do.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. No, i'm totally new in Coding.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if answer == '1' or answer == '2':
        # Survey sub-question 3
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: Where did you acquire this knowledge?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. At school or any course paid.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. On your own with free material on internet.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}3. During your free time as hobby.")
        
        while True:
            sub_answer = input("Enter your choice (1, 2 or 3): ")

            if sub_answer in ['1', '2', '3']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")        

    # Fourth survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 4: Are you mentally active?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Yes , i am.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Not actually.")

    while True:
        answer = input("Enter your choice (1 or 2): ")

        if answer in ['1', '2']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if answer == '1':
        # Survey sub-question 4
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: Do you play sports during your free time?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. Yes.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. Not really.")
        
        while True:
            sub_answer = input("Enter your choice (1 or 2): ")

            if sub_answer in ['1', '2']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")        

    # Fifth survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 5: Do you prefer to work on at home or in the office?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Remote.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Hybrid.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. In the Office.")

    while True:
        answer = input("Enter your choice (1, 2, or 3): ")

        if answer in ['1', '2', '3']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if answer == '1' or answer == '3':
        # Survey sub-question 5
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: Do you prefer to work alone or in a team?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. I prefer to work alone at home.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. Absolutely in a team.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}3. I like to alternate.")
        
        while True:
            sub_answer = input("Enter your choice (1, 2 or 3): ")

            if sub_answer in ['1', '2', '3']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")

    # Sixth survey question
    print(f"{Fore.CYAN}{Style.BRIGHT}\nQuestion 6: How do you prefer to learn coding?")
    print(f"{Fore.CYAN}{Style.BRIGHT}1. Online courses.")
    print(f"{Fore.CYAN}{Style.BRIGHT}2. Coding Bootcamps.")
    print(f"{Fore.CYAN}{Style.BRIGHT}3. Interactive platforms.")
    print(f"{Fore.CYAN}{Style.BRIGHT}4. Other.")

    while True:
        answer = input("Enter your choice (1, 2, 3 or 4): ")

        if answer in ['1', '2', '3', '4']:
            user.append(answer)
            print("Data saved. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")

    if answer == '1' or answer == '3':
        # Survey sub-question 6
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nSub-Question: What programming languages you want to learn first?")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}1. HTML and CSS.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}2. JAVASCRIPT.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}3. PYTHON.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}4. C++.")
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}5. Other.")
        
        while True:
            sub_answer = input("Enter your choice (1, 2, 3, 4 or 5): ")

            if sub_answer in ['1', '2', '3', '4', '5']:
                print("Data saved. Thank you!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4 or 5.")                    

    worksheet = SHEET.worksheet("user_choices")
    worksheet.append_row(user)
    print(f"{Fore.GREEN}{Style.BRIGHT}\nThank you for partecipating the survey!")                                     

welcome()
homepage()