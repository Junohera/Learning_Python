# 동일하지만 범용적인 __getattribute__를 이용해 모든 속성을 가로챔

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value)       # or __dict__도 사용가능
        else:
            object.__setattr__(self, name, value)

X = Powers(3, 4)
print(X.square)             # 3 ** 2 = 9
print(X.cube)               # 4 ** 3 = 64
X.square = 5
print(X.square)             # 5 ** 2 = 25