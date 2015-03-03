import sys
import urllib # R: в питоне между блоками верхнего уровня принято ставить 2 пустых строки

def get_page(argument):
    # R: эта проверка не имеет отношения к этой функции и должна выполняться снаружи.
    #    Общее правило: одна функция - одна задача. Сейчас тут 2.
    if len(argument) == 1:
        # R: а если на странице написано "Please, enter url", то мы не почувствуем разницы :)
        #    Такие приколы как раз причина общего правила выше.
        return "Please, enter url" 
    else:
        url = argument[1] 
        page = urllib.urlopen(url)
        content = page.read()
        page.close()
    return content # R: по логике это должно быть в else
# R: на следующей строке 4 пробела, и кое-где ещё они разбросаны
    

print get_page(sys.argv) 
