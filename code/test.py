from customtkinter import *
root = CTk()

temp1 = ["1", "2", "3", "4", "5"]

test = CTkOptionMenu(master=root, values=temp1)
test.pack(padx=20, pady=5, side=LEFT)

def click():
    temp2 = ["6","7","8","9"]
    test.configure(root, values=temp2)

btn = CTkButton(root, text="Change text", command=click)
btn.pack()

root.mainloop()