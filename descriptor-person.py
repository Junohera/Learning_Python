class Person:
    def __init__(self, name):
        self._name = name

    class Name:                                 # 중첩된 클래스
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
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()

bob = Person('Bob Smith')
print(bob.name)                             # Name.__get__ 실행
bob.name = 'Robert Smith'                   # Name.__set__ 실행
print(bob.name)                             # Name.__get__ 실행
del bob.name                                # Name.__delete__ 실행

print('-'*20)
sue = Person('Sue jones')
print(sue.name)
print(Person.Name.__doc__)                  # 외부에 있던 Name이 Person의 내부 중첩 클래스이므로, Person.Name으로 접근하게 변경
# help(Name)