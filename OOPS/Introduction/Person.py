class Person:
    name="default"
    age="default"
    occupation="default"
    def info(self):
      print(f"My name is {self.name} and i am a {self.occupation}")

a=Person()
print(a.name)
print(a.age)
print(a.occupation)

a.info()

milan=Person()

milan.name="MILAN SURAS"
milan.occupation="DevOps Enginner"

print(milan.name)
print(milan.occupation)
milan.info()