def main():
    x = input("Enter here: ")
    z = ""
    for i in x:
        if not i.isdigit():
            z += i    
    print(z)





main()