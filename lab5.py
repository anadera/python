import requests
import re
import webbrowser
import random

def save_page(url):
  url = 'https://www.biographyonline.net/people/famous-100.html'
  r = requests.get(url)
  with open('test.html', 'w') as output_file:
    output_file.write(r.text)

def extr_name(filename):
    f = open(filename,'r')
    read_data = f.read()
    f.close()
    res = re.findall(r'<li><a href="\D*">([A-Z][a-z]+ [A-Z][a-z]+)</a>',read_data)
    return res

def level(lvl):
  list = extr_name('test.html')
  if lvl == 1:
    return list[:10]
  if lvl == 2:
    return list[:50]
  if lvl == 3:
    return list[:100]

def search(name):
  webbrowser.open_new_tab('https://www.google.ru/search?q=' + name + '&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X')

def main():
  save_page('https://www.biographyonline.net/people/famous-100.html')
  list = level(1)
  search(random.choice(list))
  return 0

if __name__ == '__main__':
    main()