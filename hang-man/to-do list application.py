import tkinter as tk
from tkinter import messagebox
from telegram_send import send

# Create the main application window
app = tk.Tk()
app.title("To-Do List with Alarm")

# Create a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        entry.delete(0, tk.END)

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

# Function to set an alarm
def set_alarm():
    alarm_time = alarm_entry.get()
    if alarm_time:
        try:
            send("Alarm!", parse_mode="text")
            messagebox.showinfo("Alarm", "Alarm set successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to set alarm: {str(e)}")
    else:
        messagebox.showerror("Error", "Please enter an alarm time.")

# Create and configure widgets
frame = tk.Frame(app)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter Task:")
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=30)
entry.grid(row=0, column=1, padx=5)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5)

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=3, padx=5)

task_list = tk.Listbox(app, selectmode=tk.SINGLE, width=40)
task_list.pack(padx=10, pady=5)

alarm_label = tk.Label(app, text="Enter Alarm Time (HH:MM):")
alarm_label.pack(pady=5)

alarm_entry = tk.Entry(app, width=15)
alarm_entry.pack(pady=5)

set_alarm_button = tk.Button(app, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=5)

# Start the main event loop
app.mainloop()
