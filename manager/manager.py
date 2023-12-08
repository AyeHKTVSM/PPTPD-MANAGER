import subprocess

def main():
    while True:
        print_menu()
        select = input("Please select the number: ")

        actions = {
            "1": create_account,
            "2": check_account,
            "3": show_logged_in_users,
            "4": edit_account,
            "5": login_history,
            "6": individual_history,
            "7": exit_program
        }

        if select in actions:
            if select == "7":
                exit_program()
            else:
                clear_screen()
                actions[select]()
        else:
            print("Invalid selection. Please choose a number between 1 and 7.")

def print_menu():
    print("""
        1. Create Account
        2. Check Account
        3. Currently Online
        4. Edit Account
        5. Login History
        6. Check Individual Account History
        7. Exit
    """)

def clear_screen():
    subprocess.run("clear", shell=True)

def create_account():
    subprocess.run(["python3", "/etc/manager/create.py"])

def check_account():
    subprocess.run(["python3", "/etc/manager/checking.py"])

def show_logged_in_users():
    result = subprocess.run("last | grep still | grep ppp", shell=True, capture_output=True, text=True)
    output = result.stdout.strip()  # Remove leading/trailing whitespaces, newline characters
    
    if output:
        print("Currently logged in users:")
        print(output)
    else:
        print("No users are currently logged in.")

def edit_account():
    subprocess.run("nano /etc/ppp/chap-secrets", shell=True)

def login_history():
    result = subprocess.run("last | grep ppp", shell=True, capture_output=True, text=True)
    if result.stdout:
        print("Login history for 'ppp' connections:")
        print(result.stdout)
    else:
        print("No 'ppp' login history found.")

def individual_history():
    subprocess.run(["python3", "/etc/manager/history.py"])

def exit_program():
    print("Exiting the VPN Manager. Goodbye!")
    exit()

clear_screen()

print("""
[PPTPD MANAGER]         
""")

main()
