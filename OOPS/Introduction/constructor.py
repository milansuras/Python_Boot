class Student:
    
    def __init__(self,name,age,mark):
        self.name=name
        self.age=age
        self.mark=mark

    def greeting(self):
        print(f"Hello {self.name}")

milan=Student("MILAN SURAS",25,100)
print(milan.name)
print(milan.age)
print(milan.mark)

milan.greeting()