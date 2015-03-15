#import scraperwiki
#import lxml.html
import utils
import os
import sys
#html = scraperwiki.scrape("https://scraperwiki.com/")
#root = lxml.html.fromstring(html)
#el = root.cssselect("div#footer_inner strong")[0]
#print el

def save(url):
    file_name = ""
    for character in url:
        file_name = file_name + str(ord(character)) + "_"
    #content = utils.get_page(sys.argv[1])
    os.chdir("/home/dariya/Documents/Code/kind-of-graduation-project/contents")
    file_ = open(file_name, "w+")
    content = utils.get_page(url)
    file_.write(content.encode('utf8'))
    file_.close
    #return file_name

save("http://www.filmz.ru/film/17/")

