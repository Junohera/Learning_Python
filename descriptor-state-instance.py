class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value

# 클라이언트 클래스
class CalcAttrs:
    X = InstState()                 # 디스크립터 클래스 속성(=변수)
    Y = 3                           # 클래스 속성(=변수)
    def __init__(self):
        self._X = 2                 # 인스턴수 속성(=변수)
        self.Z = 4                  # 인스턴스 속성(=변수)

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)          # X가 계산되지만 나머지는 계산되지않음.
obj.X = 5                           # X에 대한 할당 캐치
CalcAttrs.Y = 6                     # 클래스 속성(변수) Y 재할당
obj.Z = 7                           # 인스턴스 속성(변수) Z 재할당
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                  # 이제 Z처럼 X도 다름.
print(obj2.X, obj2.Y, obj2.Z)