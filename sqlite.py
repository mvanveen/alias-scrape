import os

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base  = declarative_base()

engine = create_engine(
  'sqlite:///' + os.path.dirname(os.getcwd()) + '/aliases.sql',
  echo=True
)

class Alias(Base):
  """Represents a UNIX Alias found from Github"""
  __tablename__ = 'alias'

  id       = Column(Integer, primary_key=True)
  key      = Column(String(255), nullable=False)
  command  = Column(String(255), nullable=False)
  raw_url  = Column(String(255), nullable=False)
  repo_url = Column(String(255), nullable=False)

  def __init__(self, *args):
    super(Alias,self).__init__ ()
    self.key, self.command, self.raw_url, self.repo_url = args

  def __repr__(self):
    return 'Alias(%s: %s [%s])' % (self.key, self.command, self.raw_url)


if __name__ == '__main__':
  Base.metadata.create_all(engine)
