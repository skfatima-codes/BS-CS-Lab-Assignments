class Student:
    def __init__(self,student_id,name):
        self.student_id = student_id
        self.name = name
        self.enrolled = []

    def enroll(self,course):
        self.enrolled.append(course)

    def drop(self,course):
        self.enrolled.remove(course)
    
    def __str__(self):
        return f"Student({self.student_id}, {self.name})"            