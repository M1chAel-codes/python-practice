def main():
    x = input("Enter here: ")
    y = ["a", "e", "i", "o", "u"]
    aa = 0
    for i in x:
        if i in y:
            aa += 1
    print("total vowels: ", aa)



main()