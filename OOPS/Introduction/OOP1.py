class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def introduction(self):
        print(f"My name is {self.name}")

student1=Student("milan",25,77)

print(f"The name of student1 {student1.name}")
print(f"The age of student1 is {student1.age}")
print(f"The marks of student1 is {student1.marks}")
student1.introduction()
