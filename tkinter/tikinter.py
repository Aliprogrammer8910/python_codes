import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)
        save_tasks_to_file()

# Function to update the task list
def update_task_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

# Function to remove a task
def remove_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_task_list()
        save_tasks_to_file()

# Function to save tasks to a file
def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            tasks.extend(file.read().splitlines())
            update_task_list()
    except FileNotFoundError:
        pass

# Create and configure widgets
frame = tk.Frame(app)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Task:")
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.grid(row=0, column=2, padx=5)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task, bg="#F44336", fg="white")
remove_button.grid(row=0, column=3, padx=5)

task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40, bg="#E0E0E0")
task_list.pack(padx=10, pady=5)

# Load tasks from the file when the application starts
load_tasks_from_file()

# Start the main event loop
app.mainloop()
