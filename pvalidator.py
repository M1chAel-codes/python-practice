def main():
    while True:
        p = input("enter here: ")
        if len(p) >= 8:
            if any(c.isdigit() for c in p):
                valid = True
                pass
            else:
                print("must contain a number")
                continue
            if any(c.isupper() for c in p):
                valid = True
                pass
            else:
                print("must contain an uppercase letter")
                continue
            if any(c.islower() for c in p):
                valid = True
                pass
            else:
                print("must contain a lowercase letter")
                continue
        if valid:
            print("Password accepted")
            return
        else:
            print("minimum of 8 characters")
            continue

    


main()