##print("<-----Fibonacci Sequence----->")
##print("Created by EarlierMeat1", '\n')


from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

###--- Start Up Window
root = Tk()
root.title('Fibonacci Sequence')
root.geometry('400x400')

# Setting Variables
n1, n2 = 0, 1

###--- Command For When Button Is Clicked
def fib_sequence():

    global n1, n2

    #print(n1) #Prints Fibonacci Number To Terminal Screen

    fibNumber = Label(root, text=n1)
    fibNumber.pack()
    nth = n1 + n2
    n1 = n2
    n2 = nth
###---
    
###--- Close Application Pop Up
def pop_up():
    response = messagebox.askokcancel("Close Application", "Are you sure you want to close?")
    if response == True:
        root.destroy()
    else:
        return

###---
    
###--- Header Information In Window
chall_name = Label(root, text="<-----Fibonacci Sequence----->")
chall_name.pack()

creator_info = Label(root, text="Created by EarlierMeat1")
creator_info.pack()

spacer = Label(root, text="--------")
spacer.pack()
###---

###--- Button For Next Number
progress = Button(root, text="Next Number!", command=fib_sequence)
progress.pack()
###---

###--- Close Application Button
close = Button(root, text="Close", command=pop_up)
close.pack()
###---


root.mainloop()
