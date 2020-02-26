# This Python file uses the following encoding: utf-8
from bs4 import BeautifulSoup
import os
from glob import glob as glob_path

list_of_files = glob_path('./chat-datas/*/*.html')
print(list_of_files)

all = ""
for file_name in list_of_files:
    print("read file:", file_name)
    FI = open(file_name, 'r')

    for line in FI:
        all += line

dbp1 = []
dbp2 = []

for i in range(24):
    dbp1.append(0)
    dbp2.append(0)

final = ""
print("load complete.. processing")
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
        # db[int(time[1:3])]+=1;
        if "name1" in sender.lower():
            dbp1[int(time[1:3])] += 1
        elif "name2" in sender.lower():
            dbp2[int(time[1:3])] += 1
        else:
            print("forwarded message detected")

out = open("out.txt", "w")
out.write(final)
dbs = ""
for i in range(24):
    if i < 12:
        hour = str(i) + " AM"
    else:
        hour = str(i-12) + " PM"
    dbs = dbs + str(dbp1[i] + dbp2[i])+" : " + hour + "\n"
    #dbs = dbs + str(dbp2[i])+" : "+ hour+ "\n"
db_c = open("dbs.txt", "w")
db_c.write(dbs)
#os.system("sort -nr dbs.txt > sorted.txt")
