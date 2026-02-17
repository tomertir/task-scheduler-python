from id_generator import *
from ADTs import *
from Worker import *
from Task import *
class TaskScheduler:
    def __init__(self):
        self.__tasks=MyQueue()
        self.__workers = MyQueue()
        self.__completed_tasks = Stack()

    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError("task must be a Task type")
        if self.__tasks.is_empty():
            self.__tasks.enqueue(task)
            return
        q = self.__tasks
        temp_q = MyQueue()
        task_inserted = False
        while not q.is_empty():
            curr = q.dequeue()
            if not task_inserted and self.compare_tasks(task, curr):
                temp_q.enqueue(task)
                task_inserted = True
            temp_q.enqueue(curr)
        if not task_inserted:
            temp_q.enqueue(task)
        while not temp_q.is_empty():
            self.__tasks.enqueue(temp_q.dequeue())

    def compare_tasks(self, task1, task2):
        if task1.urgency > task2.urgency:
            return True
        elif task1.urgency == task2.urgency:
            if task1.importance > task2.importance:
                return True
            elif task1.importance == task2.importance:
                if task1.time_window[0] < task2.time_window[0]:
                    return True
                elif task1.time_window[0] == task2.time_window[0]:
                    if task1.time_window[1] < task2.time_window[1]:
                        return True
        return False

    def add_worker(self, worker):
        if not isinstance(worker,Worker):
            raise TypeError("worker must be a Worker type ")
        self.__workers.enqueue(worker)

    def allocate_task(self):
        curr_task=self.__tasks.dequeue()
        task_skill=curr_task.needed_skills
        t_start, t_end=curr_task.time_window
        workers=self.workers_gen()
        for worker in workers:
            worker_skill=worker.get_skills()
            if all(key in worker_skill for key in task_skill):
                for  w_start, w_end in worker.get_availability():
                    if w_start<=t_start and w_end>=t_end:
                        self.__completed_tasks.push(curr_task)
                        return
        self.add_task(curr_task)


    def update_task(self, task_id, **kwargs):
        if not isinstance(task_id,int):
            raise TypeError("task_id must be an int")
        curr_task = None
        flag=False
        l=len(self.__tasks)
        for i in range(l):
            task=self.__tasks.dequeue()
            if task.get_task_id()==task_id:
                curr_task=task
                flag=True
            self.__tasks.enqueue(task)
        if not flag:
            raise ValueError("task_id not exist")
        description=urgency=importance=time_window=needed_skills= None
        for key,value in kwargs.items():
            if key=="description":
                description=value
            elif key=="urgency":
                urgency=value
            elif key=="importance":
                importance=value
            elif key=="time_window":
                time_window=value
            elif key=="needed_skills":
                needed_skills=value
            else:
                raise ValueError("one of kwargs arguments is not match to task arguments")
        if description:
            curr_task.description=description
        if urgency:
            curr_task.urgency=urgency
        if importance:
            curr_task.importance=importance
        if time_window:
            curr_task.time_window=time_window
        if needed_skills:
            curr_task.needed_skills=needed_skills

    def __repr__(self):
       pass

    def completed_tasks_gen(self):
        helper= copy.deepcopy(self.__completed_tasks)
        while not helper.is_empty():
            yield helper.pop()

    def workers_gen(self):
        helper= copy.deepcopy(self.__workers)
        while not helper.is_empty():
            yield helper.dequeue()

    def undo_task(self):
        if self.__completed_tasks.is_empty():
            print("No tasks to undo.")
        else:
            self.add_task(self.__completed_tasks.pop())


    def promote_senior(self):
        senior_worker=self.__workers.dequeue()
        senior_worker.update_salary(1000)
        self.__workers.enqueue(senior_worker)

    def yearly_update(self):
       for i in range(len(self.__workers)):
           curr_worker=self.__workers.dequeue()
           curr_worker.helper_yearly_update()
           self.__workers.enqueue(curr_worker)

    def peek_task(self):
        if self.__tasks.is_empty():
            print("No tasks in waiting tasks.")
        else:
            task=self.__tasks.dequeue()
            self.__tasks.enqueue(task)
            for i in range(len(self.__tasks)):
                helper=self.__tasks.dequeue()
                self.__tasks.enqueue(helper)
            return task


    def get_tasks(self):
        helper = Stack()
        helper2 = Stack()
        while not self.__tasks.is_empty():
            helper.push(self.__tasks.dequeue())
        while not helper.is_empty():
            task = helper.pop()
            helper2.push(task)
            self.__tasks.enqueue(task)
        while not self.__tasks.is_empty():
            helper.push(self.__tasks.dequeue())
        while not helper.is_empty():
            self.__tasks.enqueue(helper.pop())
        return helper2


