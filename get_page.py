import sys
import urllib

def get_page(argument):
    if len(argument) == 1:
        return "Please, enter url"
    else:
        url = argument[1] 
        page = urllib.urlopen(url)
        content = page.read()
        page.close()
    return content 
    

print get_page(sys.argv) 
