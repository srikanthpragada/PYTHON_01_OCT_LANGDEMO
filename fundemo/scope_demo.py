v1 = 10  # Global variable
g = 100

def fun1():
    global g
    g = 200
    v2 = 20  # Enclosing variable
    v3 = 30
    print(v1, v2)

    # Local function
    def fun2():
        print(v1, v2, v3)

    fun2()
    print("After fun2", v3)


fun1()
print(v1)

print