class Wrapper:
    def __init__(self, object):
        self.wrapped = object                   # object 저장

    def __getattr__(self, attrname):
        print('Trace: ' + attrname)             # 호출 추적
        return getattr(self.wrapped, attrname)  # 호출 위임