from tkinter import *


def click(cl):
    global data
    text = cl.widget.cget("text")
    if text == "=":
        if data.get().isdigit():
            value = int(data.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as err:
                print(err)
                value = "Error"

        data.set(value)
        screen.update()

    elif text == "C":
        data.set("")
        screen.update()

    elif text == "D":
        screen.delete(first=len(data.get()) - 1, last="end")

    else:
        data.set(data.get() + str(text))
        screen.update()


root = Tk()
root.geometry("320x410")
root.title("Calculator")
root.wm_iconbitmap("favicon.ico")

data = StringVar()
data.set("")
screen = Entry(root, textvariable=data, font=" lucida 42 bold", bd=5)
screen.pack(fill=X, ipadx=8, padx=10, pady=10)
l1 = ['C', '/', '%', 'Delete', 9, 8, 7, '*', 6, 5, 4, '-', 3, 2, 1, '+', '00', 0, '.', '=']
# sqrt=\u221A
f = Frame(root)
for i in l1[0:3]:
    b = Button(f, text=i, padx=17, bg="white", pady=2, font="Intro 16", relief=RIDGE)
    b.pack(side=LEFT, padx=6, pady=5)
    b.bind("<Button-1>", click)
delete = Button(f, text='D', padx=17, bg="white", fg='red', pady=2, font="Intro 16", relief=RIDGE)
delete.pack(side=LEFT, padx=6, pady=5)
delete.bind("<Button-1>", click)
f.pack()

f = Frame(root)
for i in l1[4:8]:
    b = Button(f, text=i, padx=20, bg="white", pady=5, font="Intro 15", relief=RIDGE)
    b.pack(side=LEFT, padx=5, pady=5)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
for i in l1[8:12]:
    b = Button(f, text=i, padx=20, bg="white", pady=5, font="Intro 15", relief=RIDGE)
    b.pack(side=LEFT, padx=5, pady=5)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root)
for i in l1[12:16]:
    b = Button(f, text=i, padx=20, bg="white", pady=5, font="Intro 15", relief=RIDGE)
    b.pack(side=LEFT, padx=5, pady=5)
    b.bind("<Button-1>", click)
f.pack()
f = Frame(root)
for i in l1[16:19]:
    b = Button(f, text=i, padx=19, bg="white", pady=5, font="Intro 15", relief=RIDGE)
    b.pack(side=LEFT, padx=5, pady=5)
    b.bind("<Button-1>", click)
b = Button(f, text='=', padx=22, bg="blue", fg="white", pady=2, font="Intro 15", relief=RIDGE)
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()
