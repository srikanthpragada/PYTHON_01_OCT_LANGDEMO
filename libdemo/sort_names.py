try:
    f = open(r"e:\classroom\python\oct1\names.txt", "rt")
    sum = 0
    lines = f.readlines()
    for n in sorted(lines):
        sum += len(n.strip('\n'))
        print(n,end='')

    f.close()
    print("Average = ", sum / len(lines))
except Exception as ex:
    print("Sorry! Error : ", ex)
