import sys
import urllib

def get_page(url):
	page = urllib.urlopen(url)
	content = page.read()
	page.close()
	return content

print get_page(sys.argv[1]) 
