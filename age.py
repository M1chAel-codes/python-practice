def main():
    age = int(input("what's your age? "))
    if 0 <= age and age <= 12:
        print("Child")
    elif 13 <= age or age <= 17:
        print("Teenager")
    elif 18 <= age or age <= 35:
        print("Young Aged")
    elif 36 <= age or age <= 60:
        print("Middle Aged")
    elif age >= 61:
        print("Senior")
    elif age < 0:
        print("Invalid Age")

        

main()