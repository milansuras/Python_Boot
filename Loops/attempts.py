attempt=0

while True:
    pin=input("Enter your pin := ")

    attempt+=1

    if pin=="1234":
     sucess=True
     break
    if attempt==3:
     sucess=False
     break

    print("Incorrect pin try again")

if sucess:
  print("Corrected PIN ")
else:
  print("Too many attempts")