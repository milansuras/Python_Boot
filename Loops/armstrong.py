num1=int(input("Enter a digit to check armstrong := "))
num2=num1

sum=0
while num1!=0:
      rem=num1%10
      sum+=rem*rem*rem
      num1=int(num1/10)

if num2==sum:
    print(f"Entered {num2} is an armstrong number")
else:
    print(f"Entered {num2} is not an armstrong number ")

