#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import utils
import os
import os.path


# R: правильно, что вынесла это в отдельную функцию (молодец!)
# R: лучше get_file_name() или get_cache_filename()
def define_file_name(url):
    # R: return '_'.join(str(ord(c)) for c in url)
    file_name = ""
    for character in url:
        file_name = file_name + str(ord(character)) + "_"
    return file_name

# R: эта функция делает два дела: закачивает страницу и сохраняет её.
#    Поэтому и название не соответствует, сейчас это save_page()
#    или даже fetch_and_save_page() - очевидно, что-то пошло не так.
def save(url):
    file_name = define_file_name(url)
    content = utils.get_page(url)
    # R: абсолютные пути будут работать только у тебя, относительные это так:
    #       os.chdir('contents')
    # R: к сожалению относительные пути считаются от текущей папки, а не от скрипта,
    #    которая может быть произвольной, поэтому можно отталкиваться от константы __file__:
    #       http://stackoverflow.com/questions/918154/relative-paths-in-python
    # R: на самом деле os.chdir() делать не нужно, можно открывать файл с указанием пути:
    #       file = open("path/to/filename", "w")
    # R: contents - плохое имя для директории, означает просто содержания (чего?),
    #    директорию можно было бы назвать pages, cached_pages или просто cache
    os.chdir("/home/dariya/Documents/Code/kind-of-graduation-project/contents")
    # R: что за странное имя file_?
    # R: "w+" не нужно, достаточно "w". "w+" открывает файл для чтения и записи одновременно.
    file_ = open(file_name, "w+")
    file_.write(content.encode('utf8'))
    file_.close()

def load(url):
    file_name = define_file_name(url)
    # R: повторение константы
    os.chdir("/home/dariya/Documents/Code/kind-of-graduation-project/contents")
    file_ = open(file_name, "r")
    content = file_.read()
    file_.close()
    # R: функции должны возвращать уже декодированные строки во внутренний мир программы.
    #    Также можно на это смотреть как на симметрию: save() кодирует, load() - декодирует.
    return content


if len(sys.argv) < 2:
    print "\nUSAGE: python get_page.py <page-url>\n"
    sys.exit(1)
else:
    url = sys.argv[1]
    # R: добычу нужно было вынести в функцию, что-то вроде cached_get_page() и унести её в utils.
    #    Таким образом, эту функцию можно было бы использовать везде вместо get_page().
    #    Она стала бы так называемым drop-in replacement или прозрачной заменой для get_page().
    if os.path.isfile(define_file_name(url)):
        print load(url)
    else:
        # R: как-то глупо сначала сохранять, а потом загрузить из файла.
        #    Так получилось потому что save() слишком много на себя берёт.
        save(url)
        print load(url)
