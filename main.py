from tkinter import *


def button_click():
    # print("I got clicked")
    input_text = (input.get())
    print(input_text)
    my_label["text"] = input_text

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label["text"] = "New Text"
# my_label.config(text="New Text")
# my_label.pack(side="left")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button

button = Button(text="Click Me", command=button_click)
# button.pack()
# button.place(x=100, y=200)
button.grid(column=1, row=1)

# Button2

button2 = Button(text="New Me", command=button_click)
# button.pack()
# button.place(x=100, y=200)
# button2.grid(column=4, row=0)
button2.place(x=300, y=10)

# Entry

input = Entry(width=10)
# input.pack()
# input.grid(column=5, row=2)
input.place(x=430, y=250)

window.mainloop()
