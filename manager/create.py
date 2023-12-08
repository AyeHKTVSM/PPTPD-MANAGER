import random
import string
import subprocess

display_users = []
auto_generation = 1  # Force auto-generation of password


def clear():
    subprocess.run("clear", shell=True)


def create():
    global display_users
    global auto_generation

    name = generate_username()
    password = generate_password()

    command = f"echo '{name}             pptpd             {password}        *' >> /etc/ppp/chap-secrets"

    try:
        subprocess.run(command, shell=True, check=True)  # Check if the command runs without errors
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return

    display_users.append(name)
    display_users.append(password)

    clear()


def success():
    global display_users
    global auto_generation

    if not display_users:
        print("No users were added.")
        return

    print("User Added Successfully!")
    print("Username and Auto Generated Password Are:")
    print(display_users[-2:])  # Display the last added user's credentials


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
