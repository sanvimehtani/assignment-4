import random
for i in range(1,11):
   a = random.randint(1,11)
   b = random.randint(1,11)
   c = int(input("{a} x {b} = ".format(a = a,b = b)))
   if c == a * b:
        print ("Right!")
   else:
        print("Wrong.The correct answer is", a * b)


