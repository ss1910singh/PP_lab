class Parent:
    def method(self):
        print("Parent Method")

class Child(Parent):
    def method(self):
        print("Child Method")

child = Child()
child.method()
