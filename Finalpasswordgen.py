from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
import string

def password():
    global password
    try :
     characterList = string.ascii_letters + string.digits + string.punctuation

     password = ""

     for x in range(int(screen.get())):
         password = password + random.choice(characterList)
     leng.set(password)

     print("The randompassword is " + "".join(password))
     lab = Label(frm3,text="".join(password), font="lucida 15 bold")
     lab.pack(side=RIGHT)
    except Exception as err:
        messagebox.showerror('Admin', 'Please enter a valid number')

def exit():
    messagebox.showinfo('Admin', 'Thank you for using Password Generator')
    root.destroy()

def copy():
    # print("ok")
    random_password = password[0:]
    pyperclip.copy(random_password)
    messagebox.showinfo('Admin', 'Password copied')

root = Tk()
root.geometry('500x300')
root.title("Password Generator")
root.wm_iconbitmap("passwordgen_icon.ico")


r1 = random.randint(5, 10)

len = Entry()
frm = Frame(root)
frm2 = Frame(root)
frm3 = Frame(root)
frm4 = Frame(root)

l =Label(frm, text="Enter password length : ", font="lucida 14 bold")
l.pack(side=LEFT,pady=35,anchor='w')
leng = StringVar()
screen = Entry(frm, font=" lucida 14 bold")
screen.pack(pady=35,anchor='e')

btn = Button(frm2, text="Get password", command=password)
btn.pack(side=LEFT)
btn = Button(frm2, text="Copy password", command=copy)
btn.pack()
password = []

l = Label(frm3, text="Password is:", font="lucida 15 bold")
l.pack(side=LEFT,ipadx=10,pady=35,anchor='w')

btn = Button(frm4, text="Exit", command=exit)
btn.pack(anchor='se')

frm.pack()
frm2.pack()
frm3.pack()
frm4.pack()
root.mainloop()



