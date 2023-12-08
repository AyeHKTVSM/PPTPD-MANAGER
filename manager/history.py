import subprocess
import shlex

def get_login_history(username):
    sanitized_username = shlex.quote(username)
    command = f"last | grep ppp | grep {sanitized_username}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

username = input("Which User's Login History Do You Want To Check?: ")

if username.strip():  # Check if the username is not empty or whitespace
    login_history = get_login_history(username)
    if login_history:
        print(f"Login history for {username}:")
        print(login_history)
    else:
        print(f"No login history found for {username}.")
else:
    print("Please provide a valid username.")

