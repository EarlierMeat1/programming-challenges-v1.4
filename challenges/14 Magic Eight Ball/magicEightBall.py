import random
import time

print("<-----Magic Eight Ball----->")
print("Created by EarlierMeat1", '\n')

cont = 1

while cont == 1:
    print("Welcome to the magic 8 ball", '\n')

    question = input("Go on ask me a question?: ")

    print("You have asked: ")
    print("'",question, "?""'", '\n')

    responses = [1, 2, 3]
    rand = random.choice(responses)
    #print(rand)
    #rand = 1
    print("Waiting for response...")
    time.sleep(3)

    if rand == 1:
        #print("Good")
        goodResponses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        goodRand = random.choice(goodResponses)
        #print("responses random number")
        #print(goodRand)

        if goodRand == 1:
            print("It is certain")
        elif goodRand == 2:
            print("It is decidely so")
        elif goodRand == 3:
            print("Without a doubt")
        elif goodRand == 4:
            print("Yes - definately")
        elif goodRand == 5:
            print("You may rely on it")
        elif goodRand == 6:
            print("As I see it")
        elif goodRand == 7:
            print("yes")
        elif goodRand == 8:
            print("Most likely")
        elif goodRand == 9:
            print("Outlook good")
        elif goodRand == 10:
            print("Yes")
        else:
            print("Signs point to yes")


    elif rand == 2:
        #print("Bad")
        badResponses = [1, 2, 3, 4, 5]
        badRand = random.choice(badResponses)
        #print("responses random number")
        #print(badRand)

        if badRand == 1:
            print("Don't count on it")
        elif badRand == 2:
            print("My reply is no")
        elif badRand == 3:
            print("My sources say no")
        elif badRand == 4:
            print("Outlook not so good")
        else:
            print("Very doubtful")

    else:
        #print("neutral")
        neutResponses = [1, 2, 3, 4, 5, 6]
        neutRand = random.choice(neutResponses)
        #print("responses random number")
        #print(neutRand)

        if neutRand == 1:
            print("Reply hazy")
        elif neutRand == 2:
            print("Try again")
        elif neutRand == 3:
            print("ASk again later")
        elif neutRand == 4:
            print("Better not tell you now")
        elif neutRand == 5:
            print("Cannot predict now")
        else:
            print("Concentrate and ask again")
 
    print("")

    cont = 0

    restart = input("Do you want to ask another question? (yes/no): ")
    print("")

    if restart == 'no':
        break
    else:
        cont = cont + 1
        
print("Thank you for using the Magic 8 Ball")
    

##
##    goodResponse = [4, 5, 6]
##    badResponse = [1, 2, 3]
##    neturalResponse = [7, 8, 9]

##    responses = ['goodResponse', 'badResponse', 'neturalRepsonse']
##
##    rand = random.choice(responses)
##    print(rand)

    
##
##    answer = random.choice(rand)
##    print(answer)
