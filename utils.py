import urllib


def get_page(url):
    page = urllib.urlopen(url)
    # TODO: detect encoding
    content_cp1251 = page.read()
    content = content_cp1251.decode('cp1251')
    page.close()
    return content
