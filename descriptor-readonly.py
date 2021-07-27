class D:
    def __get__(*args):
        print('get')

class C:
    a = D()

X = C()
X.a

C.a

X.a = 99
X.a

list(X.__dict__.keys())

Y = C()

Y.a

C.a

# __set__을 정의해야만 읽기전용
class D:
    def __get__(*args):
        print('get')
    def __set__(*args):
        raise AttributeError('cannot set')

class C:
    a = D()

X = C()
X.a

X.a = 99 # __set__이 정의되어있기 때문에 할당 시점에 정의된 __set__이 실행되어 에러를 발생