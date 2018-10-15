
import sys

if len(sys.argv) < 2:
    print("Usage : python factorial.py <number>")
    sys.exit(1)  # Terminate program


num = int(sys.argv[1])

fact = 1
for i in range(2,num + 1):
    fact *= i

print(f"Factorial of {num} is {fact}")
