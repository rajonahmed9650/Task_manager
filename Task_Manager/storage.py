import json

def save_tasks(tasks):
    with open('task.json','w') as file:
        json.dump(tasks,file,indent=4)


def load_tasks():
    with open('task.json' ,"r") as file:
        return json.load(file)       