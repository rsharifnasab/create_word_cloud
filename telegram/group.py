
# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import os
import glob
list_of_files = glob.glob('./*.html')
all = ""
for file_name in list_of_files:
    print("read file:", file_name)
    FI = open(file_name, 'r')

    for line in FI:
        all += line


db = []
for i in range(24):
    db.append(0)
final = ""
soup = BeautifulSoup(all, 'html.parser')
metas = soup.find_all("div")
sender = ""
for meta in metas:

    if "text" in meta.attrs['class']:
        final += (meta.get_text())
    if "from_name" in meta.attrs['class']:
        sender = (meta.get_text())
        final += sender
    if "date" in meta.attrs['class']:
        time = (meta.get_text())
        final += time
        # if "f_name" in sender.lower() and "l_name" in sender.lower() :
        db[int(time[1:3])] += 1


out = open("out.txt", "w")
out.write(final)
dbs = ""
for i in range(24):
    if i < 13:
        hour = str(i) + " AM"
    else:
        hour = str(i-12) + " PM"
    dbs = dbs + str(db[i])+" : " + hour + "\n"
db_c = open("dbs.txt", "w")
db_c.write(dbs)
#os.system("sort -nr dbs.txt > sorted.txt")
