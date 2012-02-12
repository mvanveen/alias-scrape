from sqlite import Alias, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()

items = session.query(Alias).all()

print len(items)
#for x in items:
#  try:
#    print x
#  except:
#    continue
