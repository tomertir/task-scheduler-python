import copy
class Task:

    def __init__(self, task_id, description, urgency, importance, time_window, needed_skills):
        if isinstance(task_id,int):
            self.task_id=task_id
        else:
            raise ValueError("task_id must be a non-empty int.")
        if description and isinstance(description,str) :
            self.description= description
        else:
            raise ValueError("Description must be a non-empty string.")
        if urgency and isinstance(urgency, int):
            if urgency>0:
                self.urgency= urgency
            else:
                raise ValueError("Urgency must be greater then zero.")
        else:
            raise TypeError("Urgency must be a non-empty int.")
        if importance and isinstance(importance, int):
            if importance>0:
                self.importance= importance
            else:
                raise ValueError("importance must be greater then zero.")
        else:
            raise ValueError("importance must be a non-empty int.")

        if time_window and isinstance(time_window,tuple) and isinstance(time_window[0],int) and isinstance(time_window[1],int):
            if 0 <= time_window[0] <= 23 and 0 <= time_window[1] <= 23 and time_window[0] < time_window[1]:
                self.time_window=time_window
            else:
                raise ValueError("time_window: starting time need to be before ending time.")
        else:
            raise TypeError("time_window must be a non-empty Tuple of ints.")

        if needed_skills and isinstance(needed_skills,dict) :
            for key,value in needed_skills.items():
                if key and isinstance(key,str):
                    if value and isinstance(value,int) and value >0:
                        pass
                    else:
                        raise ValueError("needed_skills- value must be a non-empty int greater than zero.")
                else:
                    raise TypeError("needed_skills- key must be a non-empty string.")
            self.needed_skills=needed_skills
        else:
            raise ValueError("needed_skills must be a non-empty Dict.")


    def __repr__(self):
     return f"Task ID: {self.task_id}, Description: {self.description}, Urgency: {self.urgency}, Importance: {self.importance}, Time Window: {self.time_window}, Needed skills: {self.needed_skills}"

    def get_task_id(self):
        return copy.copy(self.task_id)

