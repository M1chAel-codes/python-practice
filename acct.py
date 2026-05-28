def main():
    tries = 0
    while True:
        username = "mike"
        password = "pass"
        u = input("Username: ")
        p = input("Password: ")
        if tries == 2:
            print("ALERT: Account locked — suspicious activity detected")
            return
        if u == username:
            pass
        if u == username and p == password:
            print(f"Access granted. Welcome, {username}")
            return
        elif u != username or p != password:
            print("invalid username and password ")
            tries += 1
            continue
        if tries == 3:
            print("ALERT: Account locked — suspicious activity detected")
    


main()