import sys
import urllib


def get_page(url):
    page = urllib.urlopen(url)
    content = page.read()
    page.close()
    return content


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    print get_page(sys.argv[1])
