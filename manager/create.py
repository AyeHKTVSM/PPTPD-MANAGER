import getpass
import random
import subprocess
import string

userlist = []
autopassword = 1  # Force auto-generation of password


def clear():
    subprocess.run("clear", shell=True)


def create():
    global userlist
    global autopassword

    name = generate_username()
    password = generate_password()

    command = f"echo '{name}             pptpd             {password}        *' >> /etc/ppp/chap-secrets"

    try:
        subprocess.run(command, shell=True, check=True)  # Check if the command runs without errors
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return

    userlist.append(name)
    userlist.append(password)

    clear()


def success():
    global userlist
    global autopassword

    if not userlist:
        print("No users were added.")
        return

    print("User Added Successfully!")
    print("Username and Auto Generated Password Are:")
    print(userlist[-2:])  # Display the last added user's credentials


def generate_username():
    # Generate a random username, for example, a combination of 'user' and a random number
    return 'user' + str(random.randint(1000, 9999))


def generate_password():
    alphabet = string.ascii_letters + string.digits  # Ensure the alphabet includes letters and digits
    pw_length = 8
    my_pw = ""

    while True:
        my_pw = ''.join(random.choice(alphabet) for i in range(pw_length))

        # Ensure the password contains at least one uppercase letter and one digit
        if any(char.isupper() for char in my_pw) and any(char.isdigit() for char in my_pw):
            break

    return my_pw


clear()
create()
success()
