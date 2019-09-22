

print("<-----TEMPERATURE CONVERTER----->")
print("Created by EarlierMeat1", '\n')

cont = 1
#print(cont)

while cont == 1:
    print("Select Temperature to Convert")                          #Menu option to choose the temperature to convert from
    print("1. Celsius       (converts to Fahrenheit and Kelvin)")
    print("2. Fahrenheit    (converts to Celsius and Kelvin)")
    print("3. Kelvin        (converts to Celsius and Fahrenheit)")
    print("")

    cont == False

    choice = input("Enter choice to convert (1/2/3): ")

    tempNum = int(input("Enter the Temperature reading: "))
    print("")

    if choice == '1':
        print("Temperature to Convert", tempNum, '\n')

        fahrenheit = tempNum * 9 / 5 + 32
        print("Fahrenheit is:", fahrenheit,"°F", '\n')          #Convert celsius to fahrenheit

        kelvin = tempNum + 273.15
        print("Kelvin is:", kelvin,"°K", '\n')                  #Convert celsius to kelvin
        


    elif choice == '2':
        print("Temperature to Convert", tempNum, '\n')

        celsius = (tempNum - 32) * 5 / 9 
        print("Celsius is:", celsius,"°C", '\n')                    #Convert fahrenheit to celsius

        kelvin = (tempNum + 459.67) * 5 / 9 
        print("Kelvin is:", kelvin,"°K", '\n')                      #Convert fahrenheit to kelvin



    elif choice == '3':
        print("Temperature to Convert", tempNum, '\n')

        celsius = tempNum - 273.15
        print("Celsius is:", celsius,"°C", '\n')                    #Convert kelvin to celsius

        fahrenheit = tempNum * 9 / 5 - 459.67
        print("Fahrenheit is:", fahrenheit,"°F", '\n')              #Convert kelvin to fahrenheit
    


    else:                                                           #Invalid input exception
        print("Invalid Input")
        print("You entered an option which does not exsist", '\n')
        

    cont = 0

    restart = input("Do you want to use the converter again? (yes/no): ")   #Restart the program condition
    print("")
    
    if restart == 'no':
        break
    else:
        cont = cont + 1


print("Thank you for using the Temperature converter")




