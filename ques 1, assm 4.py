a = int(input("Enter marks: "))
if a < 25:
    print ("Your grade is F")
elif 25 <= a < 45:
    print ("Your grade is E")
elif 45 <= a < 50:
    print ("Your grade is D")
elif 50 <= a < 60:
    print("Your grade is C")
elif 60 <= a < 80:
    print("Your grade is B")
else:
    print ("Your grade is A")
