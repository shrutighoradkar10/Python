import re
import requests
from bs4 import BeautifulSoup
#TITLE
url="https://www.imdb.com/list/ls091520106/"
req=requests.get(url)
soup=BeautifulSoup(req.text,'lxml')
img=soup.findAll('h3')
f=open(r"C:\Users\Shruti Ghoradkar\Desktop\pyton\google.txt","w",errors="ignore")
for t in img:
    f.write(str(t))
f.close()
f=open(r"C:\Users\Shruti Ghoradkar\Desktop\pyton\google.txt","r")
l=[]
nl=[]
for i in f.readlines():
    if i.startswith("<a"):
        l.append(i)
#print(l)
for j in l:
    c = re.findall("<a.+>(.+)</a>", j)
    nl.append(c)
print(nl)