import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to save tasks to a file
def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("todo_list.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("todo_list.txt", "r") as file:
            tasks = file.read().splitlines()
            for task in tasks:
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Create the main window
root = tk.Tk()
root.title("Todo List Manager")
root.geometry("280x280")  # Set window size

# Set the application icon
icon = tk.PhotoImage(file="icon.png")  
root.iconphoto(True, icon)

# Disable maximize button
root.resizable(False, False)

# Create an entry field for adding tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create a "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, width=40)
task_listbox.pack()

# Create a "Remove Task" button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

load_tasks()

# Save tasks to a file when the app is closed
def on_closing():
    save_tasks()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
