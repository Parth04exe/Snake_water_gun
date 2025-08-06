import random
computer = random.choice([-1, 0, 0])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("You win!")

    if(computer == -1 and you == 0):
        print("You lose!")

    if(computer == 1 and you == -1):
        print("You lose!")

    if(computer == 1 and you == 0):
        print("You win!")

    if(computer == 0 and you == -1):
        print("You win!")

    if(computer == 0 and you == 1):
        print("You lose!")

    else:
        print("Something went wrong")