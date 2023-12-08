import subprocess

username = input("What Username Do You Want To Check? ")
command = f"grep '{username}' /etc/ppp/chap-secrets"

subprocess.run(command, shell=True)
