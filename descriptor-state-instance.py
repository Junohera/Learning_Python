class InstState:
    def __def__(self, instance, owner):
        print('InstState get')
        return instance._X * 10
    def __set__(self, instance, value):
        print('InstState set')
        instance._X = value