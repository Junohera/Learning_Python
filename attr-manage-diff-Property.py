# 두 개의 동적으로 연산되는 속성(프로퍼티 사용)

class Powers(object):
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube
    
    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

X = Powers(3, 4)
print(X.square)             # 3 ** 2 = 9
print(X.cube)               # 4 ** 3 = 64
X.square = 5
print(X.square)             # 5 ** 2 = 25