#vowel or consonant

ch = input("Enter a alphabet: ").lower()

if ch.isalpha():
    if ch in ['a','e','i','o','u']:
        print("it is a vowel")
    else:
        print("it is a consonant")
else:
    print("please enter a valid english alphabet character!")