#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
import os
import os.path


def define_file_name(url):
    file_name = ""
    for character in url:
        file_name = file_name + str(ord(character)) + "_"
    return file_name

def save(url):
    file_name = define_file_name(url)
    content = utils.get_page(url)
    os.chdir("/home/dariya/Documents/Code/kind-of-graduation-project/contents")
    file_ = open(file_name, "w+")
    file_.write(content.encode('utf8'))
    file_.close()

def load(url):
    file_name = define_file_name(url)
    os.chdir("/home/dariya/Documents/Code/kind-of-graduation-project/contents")
    file_ = open(file_name, "r")
    content = file_.read()
    file_.close()
    return content


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    url = sys.argv[1]
    if os.path.isfile(define_file_name(url)):
        print load(url)
    else:
        save(url)
        print load(url)
