# python
import json
import os

# --- File to store tasks ---
TASKS_FILE = "tasks.json"

# --- Load tasks if file exists ---
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# --- Save tasks to file ---
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# --- Display all tasks ---
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet. 🎉\n")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task.get("done") else "❌"
            print(f"{i}. {task.get('title')}  [{status}]")
        print()

# --- Add new task ---
def add_task(tasks):
    title = input("Enter new task: ").strip()
    if not title:
        print("Task title cannot be empty.\n")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

# --- Mark task as done ---
def mark_done(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done! ✅\n")
    except (ValueError, IndexError):
        print("Invalid number. Try again.\n")

# --- Toggle task done/undone ---
def toggle_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to toggle done/undone: "))
        idx = num - 1
        tasks[idx]["done"] = not tasks[idx].get("done", False)
        save_tasks(tasks)
        state = "done ✅" if tasks[idx]["done"] else "not done ❌"
        print(f"Task is now {state}.\n")
    except (ValueError, IndexError):
        print("Invalid number. Try again.\n")

# --- Edit task ---
def edit_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to edit: "))
        idx = num - 1
        new_title = input("Enter new title: ").strip()
        if not new_title:
            print("Title cannot be empty.\n")
            return
        tasks[idx]["title"] = new_title
        save_tasks(tasks)
        print("Task updated!\n")
    except (ValueError, IndexError):
        print("Invalid number. Try again.\n")

# --- Delete task ---
def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        deleted = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {deleted['title']}\n")
    except (ValueError, IndexError):
        print("Invalid number. Try again.\n")

# --- Clear completed tasks ---
def clear_completed(tasks):
    completed = [t for t in tasks if t.get("done")]
    if not completed:
        print("No completed tasks to clear.\n")
        return
    tasks[:] = [t for t in tasks if not t.get("done")]
    save_tasks(tasks)
    print(f"Cleared {len(completed)} completed task(s).\n")

# --- Main menu ---
def main():
    tasks = load_tasks()
    while True:
        print("=== To-Do List App ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Edit task")
        print("6. Toggle done/undone")
        print("7. Clear completed tasks")
        print("8. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            toggle_task(tasks)
        elif choice == "7":
            clear_completed(tasks)
        elif choice == "8":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()