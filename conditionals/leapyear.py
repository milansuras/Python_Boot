year=int(input("Enter an year to check an year is leap year or not :="))

if year%4==0:
    print(f"Entered year {year} is an Leap year")
    if year%100==0:
        print(f"Entered year {year} is an leap year")
        if year%400==0:
            print(f"Entered year {year} is an Leap year")
else:
    print(f"Entered year {year} is not an leap year")