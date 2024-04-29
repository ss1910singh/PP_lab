try:
    a = 10
    b = 0
    c = a/b
    print(c)
except ZeroDivisionError:
    print("Divide by zero error")
except:
    print("Some error")
finally:
    print("Finally block")
