import random
comguess=random.randint(0,100)
while True:
    userguess=int(input("guess a number between 0-100 \n"))
    if userguess<comguess:
        print("guess higher\n")
    elif userguess>comguess:
        print("guess lower \n")
    else:
        print("you guessed correct !\n")
        break