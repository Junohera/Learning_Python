"""
__slots__을 사용(할당)하면

    - 일어나는 일
        1. __dict__ 제거
        2. __slost__에 할당된 집합만 속성으로 사용 가능

    - 장점
        1. 더 빠른 속성 접근
        2. 메모리 공간 절약
    
    - 단점
        1. 동적 할당 불가 -> 파이썬 철학에 어긋나는 행위. 
    
    - 사용할 상황
        클래스에 속성이 제한되어 있고, 향후에 단 하나라도 동적인 속성을 관리해야할 포인트가 없을거라 판단될 때
        클래스의 트리가 깊지 않아야함.
        동일한 클래스가 여러개 사용될 때(딕셔너리보다는 셋형태가 조금 더 메모리적으로 가볍)

    + 속성 관리하는 자료구조가 기본값 dictionary에서 set형태로 바뀐거라 생각하면 편함.
    + 상속을 하게되면 모든 트리에 __slots__를 넣어야 함.
"""

class Person:
    __slots__ = ('name', 'job', 'age')

    def __init__(self, name, job=None, age=20):
        self.name = name
        self.job = job
        self.age = age

    def __repr__(self):
        return '[Person: %s, %s, %d]' % (self.name, self.job, self.age)

if __name__ == '__main__':
    bob = Person('Bob Smith', age=40)
    sue = Person('Sue Jones', job='engineer', age=35)

    print(bob)
    print(sue)

    # bob.pay = 50000 # AttributeError: 'Person' object has no attribute 'pay'
    # sue.pay = 500000 # AttributeError: 'Person' object has no attribute 'pay'

    # __dict__과 __slots__를 확인해보자
    print("\n".join([item for item in dir(bob) if item.startswith('__d') or item.startswith('__s')])) # __d 또는 __s로 시작하는 키 출력 --> __dict__는 보이지않고, __slots__는 있다.
    # print(bob.__dict__) # AttributeError: 'Person' object has no attribute '__dict__'
    # print(sue.__dict__) # AttributeError: 'Person' object has no attribute '__dict__'
    