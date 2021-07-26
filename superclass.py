class Employee:

    def __init__(self):
        print('Employee init')
    
    def computeSalary(self):
        print("Employee computeSalary")
    
    def giveRaise(self):
        print("Employee giveRaise")

    def promote(self):
        print("Employee promote")

    def retire(self):
        print("Employee retire")

class Engineer(Employee):

    def __init__(self):
        super().__init__()
        Employee.__init__(self)
        print('Enginieer init')

    def computeSalary(self):
        super().computeSalary()
        print("Engineer computeSalary")
        
bob = Employee()
sue = Employee()
tom = Engineer()

bob.computeSalary()
sue.computeSalary()
tom.computeSalary()

print('*'*10)

company = [bob, sue, tom]
for emp in company:
    print(emp.computeSalary())