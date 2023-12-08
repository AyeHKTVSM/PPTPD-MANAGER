import subprocess


def main():
    while True:
        print("""
            1. Create Account
            2. Check Account
            3. Currently Online
            4. Edit Account
            5. Login History
            6. Check Individual Account History
            7. Exit
        """)
        select = input("Please select the number: ")

        actions = {
            "1": create,
            "2": checking,
            "3": show_logged_in_users,
            "4": edit_vpn_users,
            "5": check_history,
            "6": check_individual_login_history,
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


def clear_screen():
    subprocess.run("clear", shell=True)


def create():
    subprocess.run(["python3", "/etc/manager/create"])


def checking():
    subprocess.run(["python3", "/etc/manager/checking"])


def show_logged_in_users():
    subprocess.run("last | grep still | grep ppp", shell=True)


def edit_vpn_users():
    subprocess.run("nano /etc/manager/chap-secrets", shell=True)


def check_history():
    subprocess.run("last | grep ppp", shell=True)


def check_individual_login_history():
    subprocess.run(["python3", "/etc/manager/history"])


def exit_program():
    print("Exiting the VPN Manager. Goodbye!")
    exit()


clear_screen()

print("""
[PPTPD MANAGER]         
""")

main()
