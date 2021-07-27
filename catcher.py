class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job                                               # 'Get: job'
X.pay                                               # 'Get: pay'
X.pay = 99                                          # 'Set: pay 99'