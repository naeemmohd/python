class Student:
    def __init__(self, name, grade):                           # initializes the class Student with name and grade
        self.name = name
        self.grade = grade
        self.marks = []
    def __str__(self):                                         # string representation of the class 
        return  "{} from {}:".format(self.name, self.grade)
    def add_marks(self, subject, score):                       # used to add the marks for the student's subject
        self.marks.append({
            'subject': subject,
            'score': score
        })
    def total_marks(self):                                      # totals the score
        total = 0
        for mark in self.marks:
            total += mark['score']
        return total
    @classmethod                                                # use @classmethod decorator, you dont need to use 'self' parameter , instead you use 'cls' meaning class
    def student_info(cls, student):
        return cls(student.name, student.grade)
    @staticmethod                                               # use @staticmethod decorator, you dont need to use 'self' or 'cls' parameters
    def student_reportcard(student):
        return 'Student Name: {}, Grade: {}, Total: {}'.format(student.name, student.grade, student.total_marks())

studNaeem = Student("Naeem", "Grade 10")
studNaeem.add_marks("English", 89)
studNaeem.add_marks("Maths", 93)
studNaeem.add_marks("Science", 92)
print(studNaeem)
# print(studNaeem.total_marks())
# print(Student.student_info(studNaeem))                  # call class method using classname.
print(Student.student_reportcard(studNaeem))              # call static method using classname.

studSophia = Student("Sophia", "Grade 4")
studSophia.add_marks("English", 95)
studSophia.add_marks("Maths", 96)
studSophia.add_marks("Science", 97)
print(studSophia)
# print(studSophia.total_marks())
# print(Student.student_info(studSophia))
print(Student.student_reportcard(studSophia))