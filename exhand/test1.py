try:
    num = int(input("Enter a number :"))
    # process num
    print("Result = " ,100 / num)
except Exception as ex:   # Handle all exceptions
    print("Error : ", ex)
else:
    print("Success!")
finally:
    print("Done!")


print("The End")