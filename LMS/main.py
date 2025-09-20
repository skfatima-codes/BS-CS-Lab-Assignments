from models.student import Student
from models.instructor import Instructor
from models.course import Course
from system.lms import LMS

if __name__ == "__main__":
    # Initialize LMS
    lms = LMS()

    # Create course and instructor
    c1 = Course(501, "OOP")
    i1 = Instructor(101, "Dr. Humaira Tariq")

    # Add to LMS
    lms.add_course(c1)
    lms.add_instructor(i1)
    i1.assign(c1)  # association

    # Create 5 students (
    students = [
        Student(1, "Ali"),
        Student(2, "Fatima"),
        Student(3, "Osaja"),
        Student(4, "Zara"),
        Student(5, "Bilal")   # extra student
    ]

    # Add students to LMS and try enrolling them
    for s in students:
        lms.add_student(s)
        lms.enroll_student(s.student_id, 501)

    # Show enrolled students
    print("\nFinal Enrollment:")
    for s in c1.students:
        print( s.name)
