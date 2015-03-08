#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    print utils.get_page(sys.argv[1])
