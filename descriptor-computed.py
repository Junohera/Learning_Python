class DescSquare:
    def __init__(self, start):
        self.value = start                  # 각 디스크립터는 자신만의 상태를 가짐(인스턴스 변수에 정의 및 할당)
    def __get__(self, instance, owner):     # 속성 가져올 때
        return self.value ** 2
    def __set__(self, instance, value):     # 속성 할당 시
        self.value = value
        