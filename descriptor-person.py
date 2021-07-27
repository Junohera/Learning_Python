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

class Super:
    def __init__(self, name):
        self._name = name
    name = Name()

class Person(Super):                        # 클래스 속성으로 디스크립터를 갖고있는 Super를 Person에서 상속(= 클래스 속성 디스크립터 동일하게 적용)
    pass

bob = Person('Bob Smith')
print(bob.name)                             # Name.__get__ 실행
bob.name = 'Robert Smith'                   # Name.__set__ 실행
print(bob.name)                             # Name.__get__ 실행
del bob.name                                # Name.__delete__ 실행

print('-'*20)
sue = Person('Sue jones')
print(sue.name)
print(Name.__doc__)
# help(Name)