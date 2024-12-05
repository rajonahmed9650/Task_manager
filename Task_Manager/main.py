
from task_manager import add_task,view_tasks,remove_task,search_task
while True:
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Tasks")              
    print("4.Search Tasks")
    print("5.Update Tasks")
    print("6.Exit")

    choice = input("Enter your choice: ")
    if choice =="1":
        title = input("Enter task title:")
        description = input("Enter task description: ")
        due_date = input("Enter due date (YYY-MM-DD):")
        add_task(title,description,due_date)
        print("Task added successfully")
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
        print("Task removed successfully")   
    elif choice == "4":
        query = input("Enter the search query: ")
        print("Search Resultes:")
        search_task(query)    
