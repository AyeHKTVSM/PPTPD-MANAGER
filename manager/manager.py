import subprocess


def main():
    while True:
        print("""
            1. Add VPN Users
            2. Check VPN Users
            3. Show Logged in VPN Users
            4. Edit VPN Users
            5. Check VPN Users Login History
            6. Check Individual VPN Users Login History
            7. Exit
        """)
        select = input("Please select the number: ")

        actions = {
            "1": add_vpn_users,
            "2": check_vpn_users,
            "3": show_logged_in_users,
            "4": edit_vpn_users,
            "5": check_login_history,
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


def add_vpn_users():
    subprocess.run(["python3", "/etc/pptp-vpn-manager/adduser"])


def check_vpn_users():
    subprocess.run(["python3", "/etc/pptp-vpn-manager/checkuser"])


def show_logged_in_users():
    subprocess.run("last | grep still | grep ppp", shell=True)


def edit_vpn_users():
    subprocess.run("nano /etc/pptp-vpn-manager/chap-secrets", shell=True)


def check_login_history():
    subprocess.run("last | grep ppp", shell=True)


def check_individual_login_history():
    subprocess.run(["python3", "/etc/pptp-vpn-manager/loginhistory"])


def exit_program():
    print("Exiting the VPN Manager. Goodbye!")
    exit()


clear_screen()

print("""
[PPTPD MANAGER]         
""")

main()