class Name:
    "name descriptor docs"

    def __get__(self, instance, owner):
        """
        - self : Name 클래스 인스턴스
        - instance : Person 클래스 인스턴스
        - owner : Person 클래스
        """
        print('fetch...')
        return instance._name

    def __set__(self, instance, value):
        print('change...')

    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:
    def __init__(self, name):
        self._name = name
    name = Name()                           # 디스크립터를 속성에 할당

bob = Person('Bob Smith')
print(bob.name)                             # Name.__get__ 실행
bob.name = 'Robert Smith'                   # Name.__set__ 실행
print(bob.name)                             # Name.__get__ 실행
del bob.name                                # Name.__delete__ 실행

print('-'*20)
sue = Person('Sue jones')
print(sue.name)
print(Name.__doc__)
help(Name)