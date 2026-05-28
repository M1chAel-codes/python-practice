def main():
    i = float(input("1st test score: "))
    ii = float(input("2nd test score: "))
    iii = float(input("3rd test score: "))
    iv = float(input("4th test score: "))
    v = float(input("5th test score: "))
    sums = i + ii + iii + iv + v
    average = sums / 5
    print("Average test score: ", average)
    if average >= 90:
        print("Grade: A")
    elif average >= 80:
        print("Grade: B")
    elif average >= 70:
        print("Grade: C")
    elif average >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
main()



