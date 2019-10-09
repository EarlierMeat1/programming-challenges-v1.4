import random
import os

print("<-----Magic Eight Ball----->")
print("Created by EarlierMeat1", '\n')

score = 0

game = 1

while game == 1:

    print("Game Difficulty")
    print("1.EASY - Numbers 1-10")
    print("2.MEDIUM - Numbers 1-100")
    print("3.HARD - Numbers 1-1000")

    gameOption = input("What difficulty do you want to play (1/2/3)?: ")

    print("You have selected:", gameOption)

    if gameOption == "1":
        print("Game Difficulty = EASY", '\n')

        playAgain = 1

        while playAgain == 1:
            flag = 0
            number = random.randint(1,10)
            print(number)

            guess = input("Is the next number going to be Higher or Lower? (h/l): ")

            if guess == "h":
                print("You think Higher")
            elif guess == "l":
                print("You think Lower")
            else:
                print("Error- You did not select higher or lower")
                exit()
            
            nxtNumber = random.randint(1,10)
            print("Next: ", nxtNumber)

            if nxtNumber >= number and guess == "h":
                print("Correct the number is higher")
                score = score + 1
            elif nxtNumber < number and guess == "h":
                print("Incorrect the number was lower")
                flag = 1
            elif nxtNumber > number and guess == "l":
                print("Incorrect the number was higher")
                flag = 1
            elif nxtNumber <= number and guess == "l":
                print("Correct the number was lower")
                score = score + 1 
            else:
                print("Error")
                flag = 1

            if flag == 0:
                print("Score: ", score, '\n')
                continue
            else:
                runAgain = input("Do you want to play again? (y/n): ")
                if runAgain == "y":
                    playAgain = 1
                else:
                    playAgain = 0
                    print("Final Score: ", score)
                    
                    break

        print("Thanks for playing Higher or Lower on EASY", '\n')

        
    elif gameOption == "2":
        print("Game Difficulty = MEDIUM", '\n')

        playAgain = 1

        while playAgain == 1:
            flag = 0
            number = random.randint(1,100)
            print(number)

            guess = input("Is the next number going to be Higher or Lower? (h/l): ")

            if guess == "h":
                print("You think Higher")
            elif guess == "l":
                print("You think Lower")
            else:
                print("Error- You did not select higher or lower")
                exit()
            
            nxtNumber = random.randint(1,100)
            print("Next: ", nxtNumber)

            if nxtNumber >= number and guess == "h":
                print("Correct the number is higher")
                score = score + 1
            elif nxtNumber < number and guess == "h":
                print("Incorrect the number was lower")
                flag = 1
            elif nxtNumber > number and guess == "l":
                print("Incorrect the number was higher")
                flag = 1
            elif nxtNumber <= number and guess == "l":
                print("Correct the number was lower")
                score = score + 1 
            else:
                print("Error")
                flag = 1

            if flag == 0:
                print("Score: ", score, '\n')
                continue
            else:
                runAgain = input("Do you want to play again? (y/n): ")
                if runAgain == "y":
                    playAgain = 1
                else:
                    playAgain = 0
                    print("Final Score: ", score)
                    
                    break
                
        print("Thanks for playing Higher or Lower on MEDIUM", '\n')

            
    elif gameOption == "3":
        print("Game Difficulty = HARD", '\n')

        playAgain = 1

        while playAgain == 1:
            flag = 0
            number = random.randint(1,1000)
            print(number)

            guess = input("Is the next number going to be Higher or Lower? (h/l): ")

            if guess == "h":
                print("You think Higher")
            elif guess == "l":
                print("You think Lower")
            else:
                print("Error- You did not select higher or lower")
                exit()
            
            nxtNumber = random.randint(1,1000)
            print("Next: ", nxtNumber)

            if nxtNumber >= number and guess == "h":
                print("Correct the number is higher")
                score = score + 1
            elif nxtNumber < number and guess == "h":
                print("Incorrect the number was lower")
                flag = 1
            elif nxtNumber > number and guess == "l":
                print("Incorrect the number was higher")
                flag = 1
            elif nxtNumber <= number and guess == "l":
                print("Correct the number was lower")
                score = score + 1 
            else:
                print("Error")
                flag = 1

            if flag == 0:
                print("Score: ", score, '\n')
                continue
            else:
                runAgain = input("Do you want to play again? (y/n): ")
                if runAgain == "y":
                    playAgain = 1
                else:
                    playAgain = 0
                    print("Final Score: ", score)
                    
                    break
                
        print("Thanks for playing Higher or Lower on HARD", '\n')

            
    else:
        print("You have not selected an option which is valid. Try Again.", '\n')
        continue

    changeDiff = input("Do you want to change the difficulty? (y/n): ")

    if changeDiff == "y":
        game = 1
    else:
        game = 0

print("The game will now close, press any key to continue...")
os.system('pause')
exit()

            
