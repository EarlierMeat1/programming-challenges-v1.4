print("<-----Fizz Buzz----->")
print("Created by EarlierMeat1", '\n')


print("Welcome To FIZZ BUZZ, Please Enter Two Values For FIZZ & BUZZ [example: 3, 5]", '\n')

##-- Asign A Number To FIZZ & BUZZ
F = int(input("Enter a FIZZ Number: "))
B = int(input("Enter a BUZZ Number: "))

##-- Asign A Number To Count To 
count = int(input("Enter a Number to Count To: "))
##-- Adds An Additional Value Since Count Starts At 0 Not 1
count = count+1
##-- Tells Loop To Start At Value 1 Not 0
start = 1

for i in range(start, count):
    
    ##-- Makes Sure Values Are Divisible Wholely By Both Fizz and Buzz Numbers
    if i % F == 0 and i % B == 0:
        print("FIZZ BUZZ")
    elif i % F == 0:
        print("FIZZ")
    elif i % B == 0:
        print("BUZZ")
    else:
        print(i)
