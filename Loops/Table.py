number=int(input("Enter a number to print table:= "))
table_range=int(input("Enter range to print the table:=  "))

for i in  range(1,table_range+1):
    print(f"{number} * {i} = {number*i} \n")