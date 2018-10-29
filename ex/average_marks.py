try:
    f = open(r"e:\classroom\python\oct1\marks.txt", "rt")
    count = total = 0
    marks = []
    lines = f.readlines()
    for line in lines:
        for m in line.strip("\n").split(","):
            num = int(m)
            total += num
            marks.append(num)
            count += 1

    f.close()

    avg_marks = total / count
    print("Average marks : ", avg_marks)
    for m in marks:
        if m > avg_marks:
            print(m)

except Exception as ex:
    print("Sorry! Error : ", ex)
