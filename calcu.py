def main():
    while True:
        try:
            x = int(input("what is x? "))
            y = int(input("what is y? "))
            print(x / y)
            while True:
                retry = input("Try again? (yes/no) ").lower().strip()
                if retry == "yes":
                    continue
                elif retry == "no":
                    return
                else:
                    print("Please enter yes or no")
                
        except ZeroDivisionError and ValueError:
            pass


    

main()