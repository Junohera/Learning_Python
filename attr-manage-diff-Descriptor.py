# 동일한 코드와 디스크립터 사용(인스턴스 단위 상태)

class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

X = Powers(3, 4)
print(X.square)             # 3 ** 2 = 9
print(X.cube)               # 4 ** 3 = 64
X.square = 5
print(X.square)             # 5 ** 2 = 25