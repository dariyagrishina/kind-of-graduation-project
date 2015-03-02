# -*- coding: utf-8 -*-
import sys
import urllib

# R: в этой функции для отступов используются табы, используй пробелы,
#    также настрой Sublime, чтобы конвертировал их автоматически 
def get_page(url):
	page = urllib.urlopen(url)
	content = page.read()
	page.close()
	return content

# R: нет проверки, что урл передан, просто `python get_page.py` вызовет ошибку
print get_page(sys.argv[1])
