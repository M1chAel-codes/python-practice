def main():
    x = input("Enter here: ")
    alphab = "abcdefghijklmnopqrstuvwxyz"
    reversed_alphab = "zyxwvutsrqponmlkjihgfedcba"
    for i in x:
        ind = alphab.find(i)
        print(reversed_alphab[ind], end = "")




main()