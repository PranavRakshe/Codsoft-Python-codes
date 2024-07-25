class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{idx + 1}. {task.description} - {status}")

    def update_task(self, task_index, new_description):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].description = new_description
            print("Task updated successfully.")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            task = Task(description)
            todo_list.add_task(task)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            try:
                task_number = int(input("Enter task number to update: ")) - 1
                new_description = input("Enter new task description: ")
                todo_list.update_task(task_number, new_description)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            try:
                task_number = int(input("Enter task number to mark as completed: ")) - 1
                todo_list.mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            try:
                task_number = int(input("Enter task number to delete: ")) - 1
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '6':
            print("Exiting the To-Do List Manager.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
