list1 = [10, 20, 30, 40]
list2 = [20, 20, 10, 30, 40, 45]


def compare_lists(l1, l2):
    for n in l1:
        if n not in l2:
            return False

    for n in l2:
        if n not in l1:
            return False

    return True


print(compare_lists(list1, list2))
