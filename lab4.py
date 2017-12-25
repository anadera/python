import random
import sys


def mem_dict(filename):
    f = open(filename, 'r')
    read_data = f.read()
    f.close()
    print(read_data)


def main():
    args = sys.argv[1:]
    if not args:
        print('use: [--file] file [file ...]')
        sys.exit(1)
    for x in args:
        ret = mem_dict(x)
        print("\n")
    return 0

if __name__ == '__main__':
  main()