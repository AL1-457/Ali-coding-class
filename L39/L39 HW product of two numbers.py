from tkinter import *
from datetime import date

#Create Window
window = Tk()
window.title("Here is the Product!")
window.geometry("400x300")

# Function to calculate the product
def multiply():
    n1 = int(n1_entry.get())
    n2 = int(n2_entry.get())

    product = n1*n2

    result.insert(END, "Here is the Result!\n")
    result.insert(END, product)

#add the Widgets
label = Label(text="Let's Multiply two numbers",fg="yellow",bg="red", height=1, width=300) #title

n1_label = Label(text="Enter First Number", bg = "lime")
n1_entry = Entry()

n2_label = Label(text="Enter Second Number", bg = "lime")
n2_entry = Entry()

result = Text(height=3)

btn = Button(text="Calculate", command=multiply, height=1, bg= "#1261a0", fg="white")

# Organize the widgets
label.pack()

n1_label.pack()
n1_entry.pack()

n2_label.pack()
n2_entry.pack()

btn.pack()
result.pack()

window.mainloop()