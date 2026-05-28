def main():
    x = input("Enter here: ")
    y = x[0]
    
    for i in range(1, len(x) -1):
        y += "*"
    y += x[-1]
    print(y)





main()