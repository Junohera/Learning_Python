"""
__getattr__과 __getattribute__의 코딩 차이점을 알기 위해

    상황
        __getattr__과 __getattribute__의 두 가지 방법을 모두 이용해 세 가지 속성을 구현해본다.
        이때,
            attr1은 클래스 변수
            attr2는 인스턴스 변수
            attr3은 가져올 때 계산되는 가상의 관리 속성
"""

class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):                        # 귀에 피가 날수도 있지만, 여전히 __getattr__은 정의되지 않은 속성에 대해서만 호출된다.
        "나는 __getattr__라서 attr3만 가로챈다."
        print('get: ' + attr)                           # attr1 제외: 클래스에서 상속함
        if attr == 'attr3':                             # attr2 제외: 인스턴스에서 저장됨
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-'*20)

class GetAttribute():
    attr1 = 1

    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr):                   # 이미 귀에 피가났겠지만, 여전히 __getattribute__는 모든 속성을 가져온다
        "나는 __getattribute__라서 모든 속성 다 가로채주는 대신 루프발생해도 모름 ㅋ"
        print('get: ' + attr)
        if attr == 'attr3':
            return 3
        else:
            # __getattribute__의 문제는 ? 모든 속성을 가로채므로 루프 발생
            # -> 방지하기 위해서는 ? 수퍼클래스인 object를 이용
            # -> 좀 더 정확히는 ? 내가 관리하지 않는 속성에 대한 가져오기는 수퍼클래스로 라우팅해서 루프를 방지해야한다.
            return object.__getattribute__(self, attr)  

X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)