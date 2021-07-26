class AlreadyGotOne(Exception):
    pass

def grail():
    raise AlreadyGotOne()

try:
    grail()
except AlreadyGotOne:
    print('got exception')