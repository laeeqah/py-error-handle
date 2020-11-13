from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Authentication")

# Interface 1 Layout
heading = Label(window, text="Please enter login details")
heading.pack()

subhead1 = Label(window, text="Username")
subhead1.pack(pady = 10)

user_entry = Entry(window, width = 30)
user_entry.pack()

sub_head2 = Label(window, text="Password")
sub_head2.pack(pady = 10)

pass_word = Entry(window, width = 30)
pass_word.pack()


window.mainloop()
