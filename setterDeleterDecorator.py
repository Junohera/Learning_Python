class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):             # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):      # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter               # name = name.deleter(name)
    def name(self):
        print('remove...')
        del self._name

bob = Person('Bob Smith')
print(bob.name)                 # name getter(name 1)를 실행
bob.name = 'Robert Smith'       # name setter(name 2)를 실행
print(bob.name)
del bob.name                    # name deleter를 실행함(name 3)

print('-' * 20)
sue = Person('Sue Jones')       # sue도 프로퍼티를 상속받음
print(sue.name)
print(Person.name.__doc__)      # 혹은 help(Person.name)