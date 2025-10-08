from tkinter import *

#Create Window
window = Tk()
window.title("Event Handler!")
window.geometry("250x250")

# Event Handler for Keypress
def handle_keypress(event):
    print(event.char)

# Bind keypress event to handle_keyprees()
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    print("The button was clicked!")

#Add Widgets
button = Button(text="Click Me!")
button.pack()

# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)

window.mainloop()