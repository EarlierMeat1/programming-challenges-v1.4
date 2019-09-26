
print("<-----BMI CALCULATOR----->")
print("Created by EarlierMeat1", '\n')

cont = 1

while cont == 1:
    weight = input("Please enter weight in 'kilograms': ")
    height = input("Please enter height in 'metres': ")

    float(weight)
    float(height)

    if weight == '0':
        print("The values cannot be zero")
    elif height == '0':
        print("The values cannot be zero")
    else:      
        print("The details you have entered are;", weight,"kg", "&", height,"meters")

        bmi = float(weight) / (float(height) * float(height))
        print("Your BMI is: ")
        print(bmi, "kg/m^2")

        if bmi < 18.50:
            print("Underweight")
        elif bmi > 18.50 and bmi < 24.99:
            print("Normal Range")
        elif bmi > 25.00:
            print("Overweight")
        elif bmi > 30.00:
            print("Obese")
        else:
            print("Answer is unkown")

    cont = 0

    restart = input("Do you want to use the BMI Calculator again? (yes/no): ")   #Restart the program condition
    print("")
    
    if restart == 'no':
        break
    else:
        cont = cont + 1


print("Thank you for using the BMI Calculator")
