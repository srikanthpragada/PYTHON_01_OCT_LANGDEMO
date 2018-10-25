sum = 0
count = 0
while True:
    try:
        num = int(input("Enter a number [0 to stop] :"))
        if num == 0:
            break
        if num < 0:
            continue

        sum += num
        count += 1
    except ValueError:
        print("Sorry! Invalid number.")

if count > 0:
    print("Average  = ", sum / count)
