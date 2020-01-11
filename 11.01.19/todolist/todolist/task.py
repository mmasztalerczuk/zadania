import datetime


class Task:
    def __init__(self, desc, piority, date=None):
        self.description = desc
        self.piority = piority
        self.finish = False
        self.date = date

    def getDescription(self):
        return self.description

    def getPiority(self):
        return self.piority

    def setFinish(self, status):
        self.finish = status

    def getFinish(self):
        return self.finish

    def getDate(self):
        return self.date


class ToDo():
    def __init__(self):
        self.tasks = []

    def write(self, f):
        for task in self.tasks:
            f.write(task.getDescription())
        f.flush()

    def add(self, task):
        self.tasks.append(task)

    def getTasks(self):
        return self.tasks

    def getFinishTasks(self):

        return [task for task in self.tasks if task.getFinish()]

    def getTodayTasks(self):
        y = datetime.datetime.utcnow().year
        d = datetime.datetime.utcnow().day
        m = datetime.datetime.utcnow().month
        return [task for task in self.tasks if task.getDate().day==d and task.getDate().year==y and task.getDate().month==m]
