import threading


def print_nums():
    for i in range(1, 11):
        print(i)


t = threading.Thread(target=print_nums, name="Child1")
t.start()
