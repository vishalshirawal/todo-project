tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Search Task")
    print("5. complete Task")
    print("6. edit Task")
    print("7. task priority")
    print("8. undo complete Task")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            task_number = int(input("Enter task number to delete: "))

            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Deleted: {deleted_task}")
            else:
                print("Invalid task number.")
    elif choice == "4":
        search_term = input("Enter task to search: ")
        found_tasks = [task for task in tasks if search_term.lower() in task.lower()]

        if found_tasks:
            print("\nFound Tasks:")
            for index, task in enumerate(found_tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No matching tasks found.")

    elif choice == "5":
        task_number = int(input("Enter task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            if tasks[task_number - 1].startswith("[X] "):
                print("Task is already completed!")
            else:
                tasks[task_number - 1] = f"[X] {tasks[task_number - 1]}"
                print("Task marked as complete!")
        else:
            print("Invalid task number.")

    elif choice == "6":
        task_number = int(input("Enter task number to edit: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_number - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    elif choice == "7":
        task_number = int(input("Enter task number to set priority: "))
        if 1 <= task_number <= len(tasks):
            priority = input("Enter priority (High/Medium/Low): ")
            tasks[task_number - 1] = f"[{priority}] {tasks[task_number - 1]}"
            print("Task priority set successfully!")
        else:
            print("Invalid task number.")

    elif choice == "8":
        task_number = int(input("Enter task number to undo completion: "))
        if 1 <= task_number <= len(tasks):
            if tasks[task_number - 1].startswith("[X] "):
                tasks[task_number - 1] = tasks[task_number - 1][4:]  # Remove "[X] " prefix
                print("Task marked as incomplete!")
            else:
                print("Task is not completed.")
        else:
            print("Invalid task number.")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")