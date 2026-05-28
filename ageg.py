def main():
    while True:
        try:
            x = int(input("what is your age? "))
            if x > 0 and x < 18:
                print("Access denied")
                break
            elif x > 0 and x >= 18:
                print("Access granted")
                break
            else:
                continue


        except ValueError:
            pass




main()