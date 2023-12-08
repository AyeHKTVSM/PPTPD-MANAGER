import subprocess

def check_username(username):
    command = f"grep '{username}' /etc/ppp/chap-secrets"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"Username '{username}' found in /etc/ppp/chap-secrets:")
        print(result.stdout)
    else:
        print(f"Username '{username}' not found or command failed.")

def main():
    username = input("What Username Do You Want To Check? ")
    check_username(username)

if __name__ == "__main__":
    main()
