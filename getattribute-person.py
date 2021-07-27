class Person:
    def __init__(self, name):                           # Person의 생성자
        self._name = name                               # 이곳에서도 마찬가지로 __setattr__ 호출!

    def __getattribute__(self, attr):                   # 객체의 모든 속성에 대해 동작
        print('get: ' + attr)
        if attr == 'name':                              # 모든 이름을 가로챔
            attr = '_name'                              # 내부 이름에 매핑
        return object.__getattribute__(self, attr)      # 루프 방지

    def __setattr__(self, attr, value):                 # [obj.any = value] 실행시 호출
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                              # 내부 이름 설정
        self.__dict__[attr] = value                     # 루프 방지
    
    def __delattr__(self, attr):                        # [del obj.any] 실행시 호출
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                              # 루프 방지
        del self.__dict__[attr]                         # 일반적으로는 사용되지 않으나 예시를 위해 

bob = Person('Bob Smith')                               # bob은 관리 속성을 가짐
print(bob.name)                                         # __getattr__ 실행
bob.name = 'Robert Smith'                               # __setattr__ 실행
print(bob.name)                                         # __getattr__ 실행
del bob.name                                            # __delattr__ 실행

print('-' * 20)
sue = Person('Sue Jones')                               # sue는 프로퍼티도 상속받음
print(sue.name)
# print(Person.name.__doc__)                            # 관리 속성은 개별적인 객체가 아닌 우리가 작성한 가로채기 메서드 코드 안에 존재하기에 프로퍼티 및 디스크립터와 달리 여기서는 우리의 속성에 대한 명시적인 문서화 방법이 없다.