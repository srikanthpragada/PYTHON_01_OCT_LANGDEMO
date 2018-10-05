# Program to display whether a number is prime

num = int(input("Enter a number :"))
found = False
for i in range(2, num // 2 + 1):
    if num % i == 0:
       found = True
       break
else:
    pass

if found:
   print("Not a prime number")
else:
   print("Prime number")



