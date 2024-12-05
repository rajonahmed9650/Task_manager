
from storage import save_tasks,load_tasks

def add_task(title,description,due_date):
    tasks = load_tasks()
    task = {
        'title' : title,
        'description' : description,
        'due_date' : due_date,
        'status' : 'pending'
    }
    tasks.append(task)
    save_tasks(tasks)
def view_tasks():
    tasks = load_tasks()
    print('Tasks list:')
    for i, task in enumerate(tasks,start=1):
        print(f"{i}. Title: {task['title']},Description: {task['description']},Due_date:{task['due_date']}")
def remove_task(index):
     tasks = load_tasks()
     if 0 <index<len(tasks):
        del tasks[index-1]
        save_tasks(tasks)
     else:
        print("Invalid Index")   
def search_task(query):
    tasks = load_tasks()
    results = []
    for task in tasks:
        if query.lower() in task['title'] or query.lower() in task["description"]:
            results.append(task)
    print("Search result")
    for i, task in enumerate(results,start=1):
        print(f"{i}. Title: {task["title"]}, Description:{task["description"]},Due_date: {task["due_date"]}")        
