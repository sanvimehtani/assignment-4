year = int(input("Enter year: "))
if year % 4 == 0 and year % 100 == 0:
    if year % 400:
        print ("Year is a leap year.")
    else:
        print("Year is not a leap year.")
elif year % 4 == 0 and year % 100 != 0:
        print("Year is a leap year.")
else:
    print("Year is a leap year.")
