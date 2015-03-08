# R: mymodule - абсолютно ничего не говорящее название,
#    можно для начала назвать, например utils.py,
#    можно более специфично назвать, например page_utils.py
import sys # R: это не нужно
import urllib


def get_page(url):
    page = urllib.urlopen(url)
    content_cp1251 = page.read()
    content = content_cp1251.decode('cp1251')
    page.close()
    return content
