
import random

computer = random.choice([1,-1,0])
youstr = input("Enter your choice \nfrom('stone','Paper','scissor' ) : ")
youdict = {"paper": 1, "stone": -1, "scissor":0}
reversedict = {1:"paper", -1:"stone", 0:"scissor"}

you = youdict[youstr]

print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
   print("It's a Draw")

else:
   if(computer == -1 and you == 1):
      print("You win!")
   elif(computer == -1 and you == 0):
      print("you lose!")
   elif(computer == 1 and you == -1):
      print("you lose!")
   elif(computer == 1 and you == 0):
      print("you win!")
   elif(computer == 0 and you == 1):
      print("you lose!")
   elif(computer == 0 and you == -1):
      print("you win!")
   else:
      print("something went wrong!")


        