# -*- coding: utf-8 -*-
import urllib
import os
import os.pat
from cached_func import cached


@cached
def get_page(url):
    page = urllib.urlopen(url)
    if page.getcode() != 200:
        raise IOError('No page with url %s found' % url)
    # TODO: detect encoding
    content_cp1251 = page.read()
    content = content_cp1251.decode('cp1251')
    page.close()
    return content


def human_readable(data):
    """
    An utility for print and REPL debugging complex data structures with embedded russian text.
    """
    return json.dumps(data, ensure_ascii=False).encode('utf-8')
