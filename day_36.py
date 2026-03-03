secret_no = 7
chance = 3

while chance > 0:
    guess = int(input("Guess the secret number: "))
    if guess == secret_no:
        print("you guessed correct number, you won!")
        break
    else:
        chance -= 1
        if chance > 0:
            print(f"wrong guess! You have only {chance} chance left ")
        else:
            print("Game over! secret number was:",secret_no)