num1=int(input("Enter num1 := "))
num2=int(input("Enter num2 := "))

ch=input("Input an operator like + - / * ")

if ch == "+":
    sum=num1+num2
    print(f"The sum of {num1} + {num2} = {sum}")
elif ch == "-":
    sub=num1-num2
    print(f"The sub of {num1} - {num2} = {sub}")
elif ch == "*":
    multi=num1*num2
    print(f"The multi of {num1} * {num2} = {multi}")

elif ch=="/":
    div=num1/num2
    print(f"The Div of {num1} / {num2} = {div}")
else:
    print("Enter an invalid number and an operator!")