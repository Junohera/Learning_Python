# 동일한 코드와 범용적인 __getattr__을 이용한 정의되지 않은 속성 가로채기

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr: ' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)             # 3 ** 2 = 9
print(X.cube)               # 4 ** 3 = 64
X.square = 5
print(X.square)             # 5 ** 2 = 25