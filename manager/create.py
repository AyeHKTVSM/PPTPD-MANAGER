import subprocess
import sys
import getpass
import random

count = 0
userlist = []
autopassword = 0


def clear():
    subprocess.run("clear", shell=True)


def create():
    global userlist
    global count
    global autopassword

    command = f"echo '{name}             pptpd             {password}        *' >> /etc/ppp/chap-secrets"
    subprocess.run(command, shell=True)
    userlist.append(name)

    if autopassword == 1:
        userlist.append(password)

    count += 1
    clear()


def log_down():
    global name
    global password
    global autopassword

    print(f"Adding user {count + 1} of {target_users_to_add}")
    name = input("Username:")

    if not name:
        print("Username cannot be blank, please try again!")
        log_down()

    if autopassword == 0:
        password = getpass.getpass('Password (Press Enter to Auto Generate Password):')

    if autopassword == 1 or not password:
        generate_password()

    if autopassword == 0:
        retype_password = getpass.getpass('Retype Password:')

        if retype_password != password:
            clear()
            print("Your passwords do not match, please try again!")
            log_down()


def batch_add():
    global target_users_to_add
    target_users_to_add = int(input("Number of users to add:"))


def success():
    global userlist
    global autopassword

    print("Users Added Successfully!")

    if autopassword == 1:
        print("Username and Auto Generated Passwords Are:")
        print(userlist)
    else:
        print("Users that were successfully added:", userlist)

    print("Total Users Added:", count)


def generate_password():
    global count
    global password

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pw_length = 8
    my_pw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        my_pw += alphabet[next_index]

    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(my_pw) // 2)
        my_pw = my_pw[:replace_index] + str(random.randrange(10)) + my_pw[replace_index + 1:]

    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(my_pw) // 2, len(my_pw))
        password = my_pw[:replace_index] + my_pw[replace_index].upper() + my_pw[replace_index + 1:]


clear()
batch_add()
clear()

while count < target_users_to_add:
    log_down()
    create()

success()
