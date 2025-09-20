from models.student import Student
from models.instructor import Instructor
from models.course import Course

class LMS:
    
    
    def __init__(self):
        self.students = {}     # composition
        self.instructors = {}  # composition
        self.courses = {}      # composition

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_instructor(self, instructor):
        self.instructors[instructor.instructor_id] = instructor

    def add_course(self, course):
        self.courses[course.course_id] = course

    def enroll_student(self, student_id, course_id):
        student = self.students[student_id]
        course = self.courses[course_id]
        course.add_student(student)
