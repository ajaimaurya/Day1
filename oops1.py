class Person:
    def __init__(self,name,dept):
        self.name=name
        self.dept=dept
        
    def get_details(self):
        return f"{'name=',self.name}:{'dept=',self.dept}"
p=Person("Ravi","sales")
print(p.get_details())

    