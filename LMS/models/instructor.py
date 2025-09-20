class Instructor:
    def __init__(self,instructor_id , name):
        self.instructor_id = instructor_id
        self.name = name
        
       # Association
    def assign(self,course):
        course.instructor = self
        
    def grade(self, student):
        print(f"{self.name} grading {student.name}")

    def __str__(self):
        return f"Instructor({self.instructor_id}, {self.name})"