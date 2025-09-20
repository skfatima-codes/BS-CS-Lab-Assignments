class Course:
    MAX_STUDENTS = 4   # class-method

    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.instructor = None   # association
        self.students = []       # aggregation

    def add_student(self, student):
        if len(self.students) >= Course.MAX_STUDENTS:
            print(f" Cannot add {student.name}: {self.title} is full (limit {Course.MAX_STUDENTS})")
            return
        self.students.append(student)
        student.enroll(self)
        print(f" {student.name} enrolled in {self.title}")

    def remove_student(self, student):
        self.students.remove(student)
        student.drop(self)

    def __str__(self):
        return f"Course({self.course_id}, {self.title}, Students={len(self.students)})"
