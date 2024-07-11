class Task():

    def __init__(self, description, due_date, is_done=False):
        self.description = description
        self.due_date = due_date
        self.is_done = is_done

    def task_completed(self):
        if not self.is_done:
            self.is_done = True
            print("Task marked as completed!")
        else:
            print("Task is already completed!")


class Tasks():
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = Task(input("Enter task description: "), input("Enter due date: "), False)
        self.tasks.append(task)

    def list_current_tasks(self):
        for task in self.tasks:
            if not task.is_done:
                print(task.description)


# Test code

list1 = Tasks()

list1.add_task()
list1.add_task()
list1.add_task()

list1.tasks[1].task_completed()

list1.list_current_tasks()
