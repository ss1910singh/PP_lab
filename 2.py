class ParentOne:
    def __init__(self):
        print("ParentOne Constructor")
    def parent_one_method(self):
        print("ParentOne Method")
class ParentTwo:
    def __init__(self):
        print("ParentTwo Constructor")
    def parent_two_method(self):
        print("ParentTwo Method")

class Child(ParentOne, ParentTwo):
    def __init__(self):
        print("Child Constructor")
        super().__init__()
    def child_method(self):
        print("Child Method")

child = Child()
child.parent_one_method()
child.parent_two_method()
child.child_method()


