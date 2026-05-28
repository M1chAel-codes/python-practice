def main():
    password = input("Enter a password: ")
    if is_valid_password(password):
        print("Strong")
    else:
        print("Weak")

def is_valid_password(password):
    if password.islower() or password.isalpha() or len(password) < 8:
        return False
    else:
        return True




main()