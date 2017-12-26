import random
import sys
import re

def mem_dict(filename):
    f = open(filename, 'r')
    read_data = f.read()
    f.close()
    text = re.split(r'\W+', read_data)
    dict = {}
    new = []
    for t in text:
        i = text.index(t)
        dict[t] = text[i + 1:]
        if dict[t]:
            new.append(random.choice(dict[t]))
    s = ' '.join(new)
    return s

def gen_output(file):
    f = open(file, 'w')
    data = mem_dict('file_in.txt')
    f.write(data)
    f.close()

def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    for x in args:
        ret = mem_dict(x)
        gen_output('file_out.txt')
        ret2 = mem_dict('file_out.txt')
        print(ret)
        print(ret2)
    return 0

if __name__ == '__main__':
  main()