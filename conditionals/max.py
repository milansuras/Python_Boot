a=int(input("Enter a := "))
b=int(input("Enter b := "))
c=int(input("Enter c:= "))

if a>=b and a>=c:
    print(f"{a} Is greatest among {b} and {c}")
elif b>=c:
    print(f"{b} Is greatest among {a} and {c}")
else:
    print(f"{c} Is greatest among {a} and {b}")