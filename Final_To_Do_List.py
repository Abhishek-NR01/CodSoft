import sqlite3 as sql
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def add_to_task():
    print(e.get())
    task_container = e.get()

    if len(task_container) == 0:

        messagebox.showinfo('Error', 'Please Enter Somthing.')
    else:

        tasks.append(task_container)

        the_cursor.execute('insert into tasks values (?)', (task_container,))

        list_update()
        e.delete(0, 'end')


def list_update():
    clear_list()

    for task in tasks:
        task_listbox.insert('end', task)


def edit():
    try:

        the_value = task_listbox.get(task_listbox.curselection())

        if the_value in tasks:
            tasks.remove(the_value)
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
            list_update()
            e.insert(tk.END, the_value)

    except:
        messagebox.showerror('Error', 'Please select a task')


def delete_task():
    try:

        the_value = task_listbox.get(task_listbox.curselection())

        if the_value in tasks:
            tasks.remove(the_value)
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
            list_update()

    except:
        messagebox.showerror('Error', 'Please select a task')


def delete_all():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')

    if message_box == True:

        while (len(tasks) != 0):
            tasks.pop()

        the_cursor.execute('delete from tasks')
        list_update()


def clear_list():
    task_listbox.delete(0, 'end')


def close():
    print(tasks)
    messagebox.showinfo("Thank You", "Thank You for using TO DO LIST")
    root.destroy()


def retrieve_database():
    while (len(tasks) != 0):
        tasks.pop()

    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x600")
    root.title("TO DO LIST")
    root.wm_iconbitmap("Notepad_icon.ico")
    frm = ttk.Frame(root)
    frm.pack()
    root.configure(bg="#FAEBD7")
    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')

    tasks = []

    header_frm = ttk.Frame(root)
    middle_frm1 = ttk.Frame(root)
    middle_frm2 = ttk.Frame(root)
    middle_frm3 = ttk.Frame(root)
    Output_frm = ttk.Frame(root)

    header_frm.pack(fill='both')
    middle_frm1.pack(fill='both')
    middle_frm2.pack(fill='both')
    middle_frm3.pack(fill='both')
    Output_frm.pack(fill="both")

    label = ttk.Label(header_frm, text="  To Do List", font=("Georgia", "40", "bold"), background="#39AD48",
                      foreground="#000000")
    label.pack(ipady=50, fill='both')
    label = ttk.Label(middle_frm1, text="Add Tasks", font=("Fanatix", "20", "bold"))
    label.pack(padx=10, ipady=5, fill='x')

    e = ttk.Entry(middle_frm1, font=("Aileron", '25'), width=40)
    e.pack()

    b = ttk.Button(middle_frm2, text='Exit', command=close)
    b.pack(side="right", padx=5, pady=20)
    b = ttk.Button(middle_frm2, text='delete all', command=delete_all)
    b.pack(side="right", padx=5, pady=20)
    b = ttk.Button(middle_frm2, text='delete', command=delete_task)
    b.pack(side="right", padx=5, pady=20)
    b = ttk.Button(middle_frm2, text='Edit', command=edit)
    b.pack(side="right", padx=5, pady=20)
    b = ttk.Button(middle_frm2, text='Submit', command=add_to_task)
    b.pack(side="right", padx=5, pady=20)

    label = ttk.Label(middle_frm3, text="Tasks", font=("Fanatix", "20", "bold"))
    label.pack(padx=10, fill='x')
    task_listbox = tk.Listbox(Output_frm, width=95, height=10, selectmode='SINGLE', background="#FFFFFF",
                              foreground="#000000", selectbackground="#0000FF", selectforeground="#FFFFFF",
                              font=("Fanatix", "20"))
    task_listbox.pack(padx=20, pady=10)

    retrieve_database()
    list_update()

    root.mainloop()

    the_connection.commit()
    the_cursor.close()
