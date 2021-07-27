"""
프로퍼티와 디스크립터의 연관 관계
    - 프로퍼티와 디스크립터는 강하게 연관되어 있다.
    - 내장된 프로퍼티는 디스크립터를 만드는 편리한 방법일 뿐이다.
    - 위의 두 요인을 알았으니 디스크립터 클래스로 내장된 프로퍼티를 구현하는 것이 가능하다.
"""

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel                        # 바인드되지 않은 메서드 저장
        self.__doc__ = doc                      # 혹은 다른 호출 가능 객체

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError("cant't get attribute")
        return self.fget(instance)              # 프로퍼티 액세서에서 self에 instance를 전달

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("cant't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self):
        print('getName...')
    def setName(self, value):
        print('setName...')

    name = Property(getName, setName)   # property()처럼 사용

x = Person()
x.name                                  # 속성 가져오기 -> Person 클래스에서 Property 클래스의 __get__ 메서드로 라우팅 -> Person 클래스의 getName 메서드로 라우팅
x.name = 'Bob'                          # 속성 할당하기 -> Person 클래스에서 Property 클래스의 __set__ 메서드로 라우팅 -> Person 클래스의 setName 메서드로 라우팅
del x.name
