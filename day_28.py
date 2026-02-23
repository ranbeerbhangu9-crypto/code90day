#guessing game

secret_no = 7
count_chance = 3

print("Welcome to the number guessing game!")
print("You have only 3 chances")

for i in range(count_chance):
    guess = int(input("Enter your guess: "))

    if guess == secret_no:
        print("You guessed correct number...you won!")
        break
    else:
        print("Wrong guess!")

    if i == count_chance -1:
        print("game over")
        print("secret number was:",secret_no)