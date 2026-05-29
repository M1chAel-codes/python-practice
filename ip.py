def main():
    while True:
        ip = input("ip address: ")
        parts = ip.split(".")
        num = len(parts)
        if num == 4:
            valid = True
            for n in parts:
                try:
                    n = int(n)
                    if 0 < n and n < 255:  
                        pass
                    else:
                        print("out of range")
                        valid = False
                        break
                except ValueError:
                    print("invalid syntax")
                    valid = False
                    break 
            if valid:
                print("Valid ip")
                return
        elif num != 4:
            print("insufficient number of parts")
            continue



main()