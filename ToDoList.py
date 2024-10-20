import os

# Function to clear the terminal screen          
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initializes the Task class with title and status attributes
class Task:
    def __init__(self, title, status="Incomplete"):
        self.title = title
        self.status = status

# Initializes the ToDoList class with tasks list
class ToDoList:

    # Initializes the tasks list
    def __init__(self):
        self.tasks = []

    # Function to add a task to the list
    def add_task(self, title):
        """Add a task to the list"""
        self.tasks.append(Task(title))
        print(f"Task '{title}' has been added to the list.")

    # Function to view all tasks in the list
    def view_tasks(self):
        """View all tasks in the list"""
        if not self.tasks:
            print("The list is empty.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task.title} - {task.status}")

    # Function to mark a task as complete
    def mark_complete(self, index):
        """Mark a task as complete"""
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1].status = "Complete"
            print(f"Task '{self.tasks[index - 1].title}' marked as complete.")
        else:
            print("Invalid task number. Please try again.")
    
    # Function to remove a task from the list
    def remove_task(self, index):
        """Remove a task from the list"""
        if 1 <= index <= len(self.tasks):
            remove_task = self.tasks.pop(index - 1)
            print(f"Task '{remove_task.title}' has been removed from the list.")
        else:
            print("Invalid task number. Please try again.")

# Main function to run the To-Do List App
def main():
    # Initialize the ToDoList object
    todo_list = ToDoList()

    # Main loop for the To-Do List App
    while True:
        clear_screen()
        print("Welcome to the To-Do List App!")
        print("\nMenu")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")

        # Try block to handle user input
        try:
            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                title = input("Enter the task title: ")
                todo_list.add_task(title)
            elif choice == "2":
                todo_list.view_tasks()
            elif choice == "3":
                todo_list.view_tasks()
                index = int(input("Enter the task number to mark as complete: "))
                todo_list.mark_complete(index)
            elif choice == "4":
                todo_list.view_tasks()
                index = int(input("Enter the task number you want to delete: "))
                todo_list.remove_task(index)
            elif choice == "5":
                break
            else:
                print("Invalid choice between 1 and 5. Please try again.")

        # Exception handling for invalid input
        except ValueError:
            print("Invalid input. Please enter a number.")

        # if no exceptions are raised
        else:
            print("Operation completed successfully.")
        
        # Will always run after the try block
        finally:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
