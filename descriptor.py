class Descriptor:
    "docstring goes here"
    def __get__(self, instance, owner): # str
        print(self, instance, owner, sep = '\n')
    def __set__(self, instance, value): # void
        pass
    def __delete__(self, instance):     # void
        pass

class Subject:
    attr = Descriptor()

X = Subject()
X.attr

Subject.attr