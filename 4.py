from tkinter import Button, Label,Tk

root = Tk()
root.title("LabelButton")

btn = Button(root, text="Button")
btn.pack()

lbl = Label(root, text="Label")
lbl.pack()

root.mainloop()
