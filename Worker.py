import  copy

class Worker:
    def __init__(self, worker_id, name, skills, availability, salary):
        if isinstance(worker_id, int):
            self.__worker_id = worker_id
        else:
            raise ValueError("worker_id must be a non-empty int.")
        if name and isinstance(name,str) :
            self.name= name
        else:
            raise ValueError("name must be a non-empty string.")
        if skills and isinstance(skills,dict) :
            for key,value in skills.items():
                if key and isinstance(key,str):
                    if value and isinstance(value,int) and value >0:
                        pass
                    else:
                        raise ValueError("skills- value must be a non-empty int greater than zero.")
                else:
                    raise TypeError("skills- key must be a non-empty string.")
            self.__skills=skills
        else:
            raise TypeError("skills must be a non-empty Dict.")

        if availability and isinstance(availability,list):
            for i in availability:
                if isinstance(i,tuple) and isinstance(i[0],int) and isinstance(i[1],int):
                    if 0 <= i[0] <= 23 and 0 <= i[1] <= 23 and i[0] < i[1]:
                        pass
                    else:
                        raise ValueError("availability: starting time need to be before ending time.")
                else:
                    raise TypeError("availability list must be a non-empty Tuple of ints.")
            self.__availability=availability
        else:
            raise TypeError("availability must be a non-empty list.")
        if salary and isinstance(salary, int):
            if salary>0:
                self.__salary= salary
            else:
                raise ValueError("salary must be greater then zero.")


    def __repr__(self):
        worker_id=self.get_worker_id()
        availability=self.get_availability()
        salary=self.get_salary()
        skills=self.get_skills()
        return f"Worker ID: {worker_id}, Name: {self.name}, Skills: {skills}, Availability: {availability}, Salary: {salary}"
    
    def update_salary(self, additional_salary):
        if isinstance(additional_salary,int):
            if additional_salary>0:
                self.__salary+=additional_salary
            else:
                raise ValueError("additional_salary must be greater then zero.")
        else:
            raise TypeError("additional_salary must be an integer.")


    def update_skills(self, new_skills):
        if new_skills and isinstance(new_skills,list):
            for skill in new_skills:
                if not isinstance(skill,str):
                    raise ValueError("skill in new_skills list must a string.")
                elif skill=="":
                    raise ValueError("skill in new_skills list can not be empy string.")
            d_skills=self.__skills
            for i in new_skills:
                if i in d_skills:
                    d_skills[i]+=1
                else:
                    d_skills[i]= 1
        else:
            raise TypeError("new_skills must be a non-empty list.")

    def update_availability(self, new_availability):
        if new_availability and isinstance(new_availability, tuple) and isinstance(new_availability[0], int) and isinstance(new_availability[1], int):
            if 0 <= new_availability[0] <= 23 and 0 <= new_availability[1] <= 23 and new_availability[0] < new_availability[1]:
                start, end = new_availability
                new_lst_availability = []
                for existing_start, existing_end in self.__availability:
                    if existing_end < start or existing_start > end:
                        new_lst_availability.append((existing_start, existing_end))
                    else:
                        start = min(start, existing_start)
                        end = max(end, existing_end)
                new_lst_availability.append((start, end))
                self.__availability = new_lst_availability

            else:
                raise ValueError("new_availability: starting time need to be before ending time.")
        else:
            raise TypeError("new_availability must be a non-empty Tuple of ints.")

    def get_availability(self):
        return copy.deepcopy(self.__availability)
    
    def get_skills(self):
        return copy.deepcopy(self.__skills)

    def get_salary(self):
        return copy.deepcopy(self.__salary)
    
    def get_worker_id(self):
        return copy.deepcopy(self.__worker_id)

    def helper_yearly_update(self):
        skills=self.__skills
        for key,value in skills.items():
            skills[key]=value+1



