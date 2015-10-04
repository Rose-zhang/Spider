# encoding: UTF-8
import re

import requests
from bs4 import BeautifulSoup

from errcode import *
from constants import *
import hashlib

__author__ = 'Jason-Zhang'


# Acknowledge
# http://ar.newsmth.net/thread-b99daa8fc0a336.html
def parse_js(expr):
	import ast
	m = ast.parse(expr)
	a = m.body[0]

	def parse(node):
		if isinstance(node, ast.Expr):
			return parse(node.value)
		elif isinstance(node, ast.Num):
			return node.n
		elif isinstance(node, ast.Str):
			return node.s
		elif isinstance(node, ast.Name):
			return node.id
		elif isinstance(node, ast.Dict):
			return dict(zip(map(parse, node.keys), map(parse, node.values)))
		elif isinstance(node, ast.List):
			return map(parse, node.elts)
		else:
			raise NotImplementedError(node.__class__)

	return parse(a)


class Item:
	def __init__(self, url):
		self.url = url

	def parse_and_save(self, path):
		# s = requests.session()
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, "html.parser")
		# pattern = re.compile(r'".*"')

		description = self.__get_item_description(soup)
		title = self.__get_item_title(soup)
		cid = self.__get_item_cid(soup)
		price = self.__get_item_price(soup)
		inputValues = self.__get_item_inputValues(soup)
		subtitle = self.__get_item_subtitle(soup)
		picture = self.__get_item_picture(soup)
		item_info = {
			'title': title,
			'cid': cid,
			'price': price,
			'inputValues': inputValues,
			'subtitle': subtitle,
			'description': description,
			'picture': picture
		}
		self.__download_acution_pictures(picture, path)

	@staticmethod
	def __get_item_description(soup):
		pattern = re.compile(r'//desc\.alicdn.com.*"')
		scripts = soup.find_all("script")
		for script in scripts:
			match = pattern.findall(script.contents[0])
			if len(match) != 1:
				continue
			description = match[0].split(":")[0]
			description = description.replace('"', '')
			description = description.replace(' ', '')
			return description
		raise Exception(ERROR_DESCRIPTION_URL)

	@staticmethod
	def __get_item_title(soup):
		title = soup.select("[class~=tb-main-title]")
		if len(title) != 1 or not title[0].has_attr('data-title'):
			raise Exception(ERROR_TITLE_LOCATION)
		return title[0].attrs['data-title']

	@staticmethod
	def __get_item_cid(soup):
		J_Pine = soup.select("[class~=tb-pine]")
		if len(J_Pine) != 1:
			raise Exception(ERROR_CID_LOCATION)
		return J_Pine[0].attrs['data-catid']

	@staticmethod
	def __get_item_price(soup):
		J_PromoPriceNum = soup.select("[class~=tb-rmb-num]")
		if len(J_PromoPriceNum) != 1:
			raise Exception(ERROR_PRICE_LOCATION)
		return J_PromoPriceNum[0].contents[0]

	# FIXME improve this stupid parsing
	@staticmethod
	def __get_item_picture(soup):
		pattern = re.compile(r'g_config\.idata=.*}')
		scripts = soup.find_all("script")
		for script in scripts:
			match = pattern.findall(script.contents[0].replace('\n', '').replace('\r', ''))
			if len(match) != 1:
				continue
			config_data = match[0]
			pattern = re.compile(r'{.*}')
			description = pattern.findall(config_data)[0][:-1]
			# json_data = json.loads(description, encoding='GB2312')
			json_data = parse_js(description)
			# print type(json_data)
			return json_data['item']['auctionImages']
		raise Exception(ERROR_DESCRIPTION_URL)

	@staticmethod
	def __download_acution_pictures(pic_list, path):
		pic_md5_list = []
		protocol = "http:"
		for pic_url in pic_list:
			pic = requests.get(protocol + pic_url)
			pic_content = pic.content
			m = hashlib.md5()
			m.update(pic_content)
			m_hexdigest = m.hexdigest()
			pic_md5_list.append(m_hexdigest)
			f = open(path + '\\' + m_hexdigest + '.tbi', 'wb')
			f.write(pic_content)
			f.flush()
			f.close()

	@staticmethod
	def __get_item_inputPids():
		return ISBN_KEY

	@staticmethod
	def __get_item_inputValues(soup):
		attribute_list = soup.select('[class~=attributes-list]')
		if attribute_list is None:
			return None
		contents = attribute_list[0].contents
		pattern = re.compile(r'ISBN')
		for content in contents:
			if pattern.match(content.string):
				str = content.string
				return str.split(':')[1].replace(' ', '')
		return None

	@staticmethod
	def __get_item_subtitle(soup):
		subtitle = soup.select('[class~=tb-subtitle]')
		# print subtitle
		if len(subtitle) == 0:
			return None
		return subtitle[0].contents[0].replace('\n', '')


if __name__ == '__main__':
	url = "https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-5537852711.32.bjyZhS&id=45815446244"
	item = Item(url)
	item.parse_and_save('C:\\Users\\think\\Desktop\\123')
