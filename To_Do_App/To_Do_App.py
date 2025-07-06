import customtkinter as ctk

tasks = [] 

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_entry.delete(0, 'end')
        display_tasks()

def delete_task(index):
    
    confirm_window = ctk.CTkToplevel(root)
    confirm_window.geometry("300x200")
    confirm_window.title("Confirm Delete")

    ctk.CTkLabel(confirm_window, text="Are you sure you want to delete this task?", font=("Arial", 16), wraplength=250).pack(pady=15)

    def confirm():
        tasks.pop(index)
        display_tasks()
        confirm_window.destroy()

    yes_button = ctk.CTkButton(confirm_window, text="Yes", fg_color="red", command=confirm)
    yes_button.pack(pady=10)

    no_button = ctk.CTkButton(confirm_window, text="No", fg_color="green", command=confirm_window.destroy)
    no_button.pack(pady=5)

def edit_task(index):
   
    edit_window = ctk.CTkToplevel(root)
    edit_window.geometry("300x200")
    edit_window.title("Edit Task")

    ctk.CTkLabel(edit_window, text="Edit your task:", font=("Arial", 16)).pack(pady=10)

    edit_entry = ctk.CTkEntry(edit_window, font=("Arial", 16), width=250)
    edit_entry.pack(pady=10)
    edit_entry.insert(0, tasks[index]) 

    def save_edit():
        new_task = edit_entry.get().strip()
        if new_task:
            tasks[index] = new_task
            display_tasks()
            edit_window.destroy() 

    save_button = ctk.CTkButton(edit_window, text="Save", command=save_edit, corner_radius=10)
    save_button.pack(pady=10)

    cancel_button = ctk.CTkButton(edit_window, text="Cancel", fg_color="gray", corner_radius=10,
                                  command=edit_window.destroy)
    cancel_button.pack(pady=5)

def display_tasks():
    for widget in tasks_frame.winfo_children():
        widget.destroy()

    for index, task in enumerate(tasks):
        frame = ctk.CTkFrame(tasks_frame, corner_radius=10)
        frame.pack(fill="x", padx=5, pady=5)

        task_label = ctk.CTkLabel(frame, text=task, font=("Arial", 18))
        task_label.pack(side="left", padx=10, pady=5)

        edit_button = ctk.CTkButton(frame, text="Edit", width=50, height=30,
                                    command=lambda i=index: edit_task(i))
        edit_button.pack(side="right", padx=5)

        delete_button = ctk.CTkButton(frame, text="Delete", width=60, height=30,
                                      fg_color="red", command=lambda i=index: delete_task(i))
        delete_button.pack(side="right", padx=5)


root = ctk.CTk()
root.geometry("450x600")
root.title("To-Do List App")


task_entry = ctk.CTkEntry(root, placeholder_text="Enter task here...", font=("Arial", 20), width=350, height=40)
task_entry.pack(pady=15)


add_button = ctk.CTkButton(root, text="Add Task", command=add_task, corner_radius=15, font=("Arial", 18))
add_button.pack(pady=10)


tasks_frame = ctk.CTkFrame(root, corner_radius=15)
tasks_frame.pack(fill="both", expand=True, padx=15, pady=15)

root.mainloop()
