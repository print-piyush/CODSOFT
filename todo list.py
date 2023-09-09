import tkinter
import tkinter.messagebox
import pickle

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")

def clear_all_tasks():
    confirmed = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?")
    if confirmed:
        listbox_tasks.delete(0, tkinter.END)

def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find tasks.dat.")
    except Exception as e:
        tkinter.messagebox.showerror(title="Error!", message=str(e))

def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    try:
        pickle.dump(tasks, open("tasks.dat", "wb"))
    except Exception as e:
        tkinter.messagebox.showerror(title="Error!", message=str(e))

root = tkinter.Tk()
root.title("To-Do List by @TokyoEdtech")

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_clear_all = tkinter.Button(root, text="Clear All", width=48, command=clear_all_tasks)
button_clear_all.pack()

button_load_tasks = tkinter.Button(root, text="Load tasks", width=48, command=load_tasks)
button_load_tasks.pack()

button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
