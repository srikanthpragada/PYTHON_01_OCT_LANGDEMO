try:
    f = open(r"e:\classroom\python\oct1\employees.txt", "rt")
    lines = f.readlines()
    employees = {}
    for line in lines:
        # Ignore blank lines
        if len(line.strip("\n")) == 0:
            continue

        parts = line.strip("\n").split(",")
        dept = parts[0]
        if dept in employees:
            # get list for dept
            lst = employees[dept]
        else:
            # create a new entry in dict
            lst = []
            employees[dept] = lst

        # Add names of employees to list in dept
        for i in range(1,len(parts)):
                lst.append(parts[i])

    f.close()

    # Print dept and employees
    for d,e in sorted(employees.items()):
        print("%-10s  %s"  % (d, ",".join(sorted(e))))

except Exception as ex:
    print("Sorry! Error : ", ex)
