class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):     # 속성을 가져올 때 실행됨
        print('DescState get')
        return self.value * 10

    def __set__(self, instance, value):     # 속성을 할당할 때 실행됨
        print('DescState set')
        self.value = value