import requests
import re
import webbrowser
import random
from http.server import HTTPServer, CGIHTTPRequestHandler

def save_page(url, file):
  r = requests.get(url)
  with open(file, 'w') as output_file:
    output_file.write(r.text)

def extr_name(filename, rgx):
    f = open(filename,'r')
    read_data = f.read()
    f.close()
    res = re.findall(rgx,read_data)
    return res

def level(lvl):
  rgx_ref = r'<li><a href="\D*">([A-Z][a-z]+\s*[A-Z]*[a-z]*\s*[A-Z]*[a-z]*)</a>'
  list = extr_name('test.html', rgx_ref)
  return list[:lvl]

def search(name):
  save_page('https://www.google.ru/search?q=' + name + '&newwindow=1&espv=2&source=lnms&tbm=isch&sa=X', 'tmp.html')
  rgx = r'img height="\d+" src="(\S+)" width="\d+"'
  pics = extr_name('tmp.html',rgx)
  return random.choice(pics)

def show_pic(url):
  webbrowser.open(url)

def guess(name, list, lvl):
  answers = []
  answers.append(name)
  i=0
  while i<3:
    x = random.randint(0, int(lvl-1))
    print('x ', x)
    print('length ', len(list))
    if list[x] not in answers:
      answers.append(list[x])
      i = i + 1
  random.shuffle(answers)
  return answers

def check_answer(answer, name):
  return True if answer == name else False

"""def create_webpage():
  server_address = ("", 8000)
  httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
  httpd.serve_forever()
  print("Content-type: text/html")
  print()
  print("<h1>Hello world!</h1>")"""

def main():
  #create_webpage()
  save_page('https://www.biographyonline.net/people/famous-100.html', 'test.html')
  print("Select level (1,2,3):")
  lvl = int(input())
  levels = ['10', '50', '100']
  print(levels[lvl-1])
  lvl = int(levels[lvl-1])
  list = level(lvl)
  state = True
  while state:
    name = random.choice(list)
    pic = search(name)
    show_pic(pic)
    print(guess(name,list,lvl))
    answer = input()
    print(check_answer(answer,name))
    if check_answer(answer, name) == False:
      exit()
  return 0

if __name__ == '__main__':
    main()