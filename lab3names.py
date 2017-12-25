import sys
import re

def two(list1, list2):
    new = []
    new.extend(list1)
    new.extend(list2)
    new.sort()
    return new

def extr_name(filename):
    """
    Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
    '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
    """
    year = filename[4:8]
    f = open(filename,'r')
    read_data = f.read()
    f.close()
    new=[]
    new.append(year)
    res = re.findall(r'<tr align="right"><td>([0-9]+)</td><td>([A-Z][a-z]+)</td><td>([A-Z][a-z]+)</td>',read_data)
    women = []
    men = []
    for x in res:
        men.append(x[1] + ' ' + x[0])
        women.append(x[2] + ' ' + x[0])
    new.extend((two(women,men)))
    return new

#def top(filename):



def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    for x in args:
        ret = extr_name(x)
        print(ret)
    return 0

        # для каждого переданного аргументом имени файла, вывести имена  extr_name

        # напечатать ТОП-10 муж и жен имен из всех переданных файлов


if __name__ == '__main__':
    main()