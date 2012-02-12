from scrapy.http import Request
from scrapy.spider import BaseSpider

from alias_scrape.items import AliasScrapeItem
from beautiful_soup import BeautifulSoup as bs

class AliasScrapeSpider(BaseSpider):
  name = "alias_scrape"
  allowed_domains = ["github.com"]

  start_urls = [
      ''.join((
        'https://github.com/search?langOverride=&language=Shell&q=alias&repo'
        '=&start_value=', str(x), '&type=Code&x=12&y=18'
      )) for x in range(1, 20)
  ]



  def parse(self, response):
    filename = response.url.split("/")[-2]
    soup = bs(response.body)

    raw_links = [x.findChildren()[0].findChildren()[0].get('href') for x in
      soup.findAll('ul', {'class':'actions'})
    ]
    if raw_links:
      item = AliasScrapeItem()
      item['raw_url'] = 'http://github.com' + raw_links[0]
      item['repo_url'] = response.url
      yield item

    else:
      children = soup.findAll('h2', {'class':'title'})
      children = [x.findChildren()[0].get('href') for x in children]
      #open(filename, 'wb').write(response.body)

      for url in children:
        yield Request('http://github.com' + url, callback=self.parse)
