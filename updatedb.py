# updatedb.py : 파일시스템 데이터베이스의 Person 객체를 업데이트

import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()