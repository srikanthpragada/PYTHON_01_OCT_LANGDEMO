
nums = []   #empty lits

while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break
    if num % 2 == 0:
        nums.insert(0,num)    #insert at the beginning
    else:
        nums.append(num)     #insert at the end


for n in nums:
    print(n, end= ' ')

