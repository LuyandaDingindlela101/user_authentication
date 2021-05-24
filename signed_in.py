from tkinter import *

#   CREATE THE FRAME FOR TKINTER
window = Tk()
window.title("User sign in")
window.geometry("550x500")


username_label = Label(window, text="You are signed in.", font=(30), fg="blue", pady=50).pack()
# username_label.place(x=10, y=10)

window.mainloop()
