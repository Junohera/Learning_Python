class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job                                               # 'Get: job'
X.pay                                               # 'Get: pay'
X.pay = 99                                          # 'Set: pay 99'

class Wrapper:
    def __init__(self, object):
        self.wrapped = object                       # object 저장
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)                 # 가져오기를 추적
        return getattr(self.wrapped, attrname)      # 가져오기 위임

X = Wrapper([1, 2, 3])
X.append(4)                                         # "Trace: append"
print(X.wrapped)                                    # "[1, 2, 3, 4]"