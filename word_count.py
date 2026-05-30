def main():
    word = input("make a sentece: ").lower()
    parts = word.split(" ")
    num = 0
    word = {}
    for c in parts:
        if c in word:
            word[c] += 1
        else:
            word[c] = 1
    for c in word:
        print(f"{c}: {word[c]}")


main()

