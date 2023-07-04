import pickle

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter a title for the task: ")
        description = input("Enter a description for the task: ")
        status = "Incomplete"
        task = Task(title, description, status)
        self.tasks.append(task)
        print("Task added successfully!")

    def remove_task(self):
        title = input("Enter the title of the task to delete: ")
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task removed successfully!")
                return
        print("Task not found in the list.")

    def view_tasks(self):
        print("To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. Title: {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Status: {task.status}")
            print()

    def save_tasks(self, filename):
        try:
            with open(filename, "wb") as file:
                pickle.dump(self.tasks, file)
            print("Tasks saved successfully!")
        except Exception as e:
            print(f"An error occurred while saving tasks: {str(e)}")

    def load_tasks(self, filename):
        try:
            with open(filename, "rb") as file:
                self.tasks = pickle.load(file)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("File not found. No tasks loaded.")
        except Exception as e:
            print(f"An error occurred while loading tasks: {str(e)}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n========== TO-DO LIST MENU ==========")
        print("1. Add a task")
        print("2. remove a task")
        print("3. View tasks")
        print("4. Save tasks")
        print("5. Load tasks")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.remove_task()
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter a filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter a filename to load tasks from: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
