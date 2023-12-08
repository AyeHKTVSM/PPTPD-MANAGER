import subprocess

username = input("Which User's Login History Do You Want To Check?: ")
command = f"last | grep ppp | grep {username}"

subprocess.run(command, shell=True)
