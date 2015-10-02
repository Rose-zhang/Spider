# encoding: UTF-8
import requests
from bs4 import BeautifulSoup
import re

__author__ = 'Jason-Zhang'


class Item:
	def __init__(self, url):
		self.url = url

	def parse(self):
		s = requests.session()
		r = s.get(self.url)
		soup = BeautifulSoup(r.text, "html.parser")
		# pattern = re.compile(r'".*"')
		content = soup.find_all("script")[0].contents[0]
		description = self.get_item_description(content)
		title = self.get_item_title(soup)
		print title
		# print description

	def get_item_description(self, content):
		pattern = re.compile(r'//desc\.alicdn.com.*"')
		match = pattern.findall(content)
		if len(match) != 1:
			raise Exception(u"没有找到宝贝描述页URL")
		description = match[0].split(":")[0]
		description = description.replace('"', '')
		description = description.replace(' ', '')
		return description

	def get_item_title(self, soup):
		title = soup.select("[class~=tb-main-title]")
		if len(title) != 1 or not title[0].has_attr('data-title'):
			raise Exception(u"无法定位title")
		return title[0].attrs['data-title']

	def get_item_cid(self, soup):
		return

	def get_item_price(self, soup):
		return

	def get_item_picture(self, soup):
		return

	def get_item_inputPids(self, soup):
		return

	def get_item_inputValues(self, soup):
		return

	def get_item_subtitle(self, soup):
		return

if __name__ == '__main__':
	url = "https://item.taobao.com/item.htm?spm=a230r.1.14.150.Ui4Azt&id=43676300251&ns=1&abbucket=8#detail"
	item = Item(url)
	item.parse()
