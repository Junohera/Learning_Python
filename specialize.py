# specialize.py : 클래스 인터페이스 기법

"""
Super
    Method 함수와 서브클래스의 action에 대응하는 delegate를 정의한다.

Inheritor
    어떤 새로운 이름도 제공하지 않기 때문에 Super에 정의된 모든 것을 상속받는다.

Replacer
    Super의 method를 자체 버전으로 오버라이드한다.

Extender
    Super의 method를 오버라이드하고, 기본 동작을 실행하기 위해 콜백을 호출한다.

Provider
    Super의 delegate 메서드에 대응하는 action 메서드를 구현한다.
"""

class Super:
    def method(self):
        print('in Super.method')

    def delegate(self): # ( 자바의 Interface 정의 )
        self.action()

class Inheritor(Super): # 메서드를 그대로 상속
    pass

class Replacer(Super): # 메서드를 완전히 대체
    def method(self):
        print('in Replacer.method')

class Extender(Super): # 메서드의 동작을 확장
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super): # 필요한 메서드를 채워넣음 ( 자바의 Interface 구현 )
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
