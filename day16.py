#time and message
time = int(input("Enter time: "))
period = input("Enter am or pm: ").lower()

if period == "am":
    if time >= 5 and time < 12:
        print("Good morning")
    else:
        print("Good night")
elif period == "pm":
    if time >=1 and time < 5:
        print("Good Afternoon")
    elif time >=5 and time <=11:
        print("Good Evening")
    else:
        print("Invalid time")
else:
    print("Invalid period please enter in Am or Pm")