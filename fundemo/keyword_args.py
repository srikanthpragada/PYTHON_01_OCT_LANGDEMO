def fun(**args):
    name =  args.get("name","Unknown")
    print(name)
    for k,v in args.items():
        print(k,v)


fun(a=10, b=20, c=30)
fun(name="Srikanth", email="srikanth@gmail.com")
