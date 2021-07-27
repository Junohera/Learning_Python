class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value

# 클라이언트 클래스
class CalcAttrs:
    X = InstState()
    Y = 3
    def __init__(self):
        self._X = 2
        self.Z = 4
