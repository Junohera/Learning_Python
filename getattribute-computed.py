class AttrSquare:
    def __init__(self, start):
        self.value = start                                  # __setattr__ 발동
    
    def __getattribute__(self, attr):                       # 모든 속성 가져오기를 캐치
        if attr == 'X':
            return object.__getattribute__(self, 'value') ** 2 # 바로 object의 속성을 접근해 불필요한 재귀적 호출을 제거

    def __setattr__(self, attr, value):                     # 모든 속성 할당을 캐치
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)               # object로 접근해 루프 방지

A = AttrSquare(3)                                           # 두 개의 오버로드된 클래스 인스턴스
B = AttrSquare(32)                                          # 각각은 다른 상태 정보를 가짐

print(A.X)                                                  # 3 ** 2
A.X = 4
print(A.X)                                                  # 4 ** 2
print(B.X)                                                  # 32 ** 2(1024)