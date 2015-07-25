__author__ = 'think'
# this module is for dealing with the rootURL and get a bunch of the links to each item

import re
import urllib2
from bs4 import BeautifulSoup


class RootPage:
    def __init__(self, page_url):
        self.pageURL = page_url
        content = urllib2.urlopen(page_url)
        html = content.read()
        content = html.decode('gbk', 'ignore')
        print(html)
        content = re.sub('&nbsp;', ' ', content)
        content = re.sub('\n', ' ', content)

        self.soup = BeautifulSoup(content, "html.parser")
        # self.soup = BeautifulSoup(open(page_url), "html.parser")

    def getLinks(self):
        # pattern = re.compile('item?line?')
        # get all the link in the root page <1>
        # link_pool = self.soup.select('a[href]')
        link_pool = self.soup.find_all('a')
        href_container = []
        pattern = re.compile(r'.*item\.taobao\.com.*')
        # print(link_pool.__len__())
        for link in link_pool:
            if link.get('href') and re.match(pattern, link.get('href')):
                href_container.append(link.get('href'))
                # print link.prettify('gbk')
        # print href_container.__len__()


if __name__ == '__main__':
    page_url = "http://chengxinshudian88.taobao.com/search.htm?q=%BD%F0%C8%FD%C1%B7&searcy_type=item&s_from=newHeader&source=&ssid=s5-e&search=y&spm=a1z10.1.1996643285.d4916905&initiative_id=shopz_20150725"
    # page_url = "index.html"
    instance = RootPage(page_url)
    instance.getLinks()
