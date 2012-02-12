"""get_aliases.py

Grabs alias files from github, parses output, and dups it all into sqlite.

"""
import json
from multiprocessing import Pool
import re

import requests
from sqlalchemy.orm import Session, sessionmaker
from sqlite import Alias, engine
from test_alias import test_alias

Session = sessionmaker(bind=engine)


class AliasFile(object):
  """Container for all the UNIX aliases in a file"""

  def __init__(self, raw_url=None, repo_url=None):
    super(AliasFile, self).__init__()

    self._raw_url  = raw_url
    self._repo_url = repo_url

    self._pattern = re.compile('.*')

    response = requests.get(self._raw_url)
    self._content = response.content if response.status_code == 200 else ''

    self._results = self.parse()

  def parse(self):
    # grab out all the alias files
    results = filter(None, [x for x in re.findall(self._pattern, self._content)])
    results = [x.replace('alias', '').lstrip().rstrip().split('=') for x in results]
    return results

  def put(self):
    session = Session()
    for item in self._results:
      if len(item) == 2:
        print item
        alias = Alias(item[0], item[1], self._raw_url, self._repo_url)
        session.add(alias)
      else:
        pass

    try:
      session.commit()
    except:
      session.rollback()
      raise

with open('items.json', 'r') as items:
  _json = json.loads(items.read())

def load_item(dict_item):
  alias = AliasFile(**(dict_item))
  alias.put()

if __name__ == '__main__':
  #print load_item(1)
  p = Pool(4)
  p.map(load_item, _json)
