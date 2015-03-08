#!/usr/bin/python -tt
# -*- coding: utf-8 -*-


import sys
import urllib # R: это не нужно
import mymodule


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    print mymodule.get_page(sys.argv[1])
