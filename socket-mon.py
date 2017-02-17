import psutil
import sys

conn = psutil.net_connections()

listOfConn = []

for c in conn:
    if c[3] != () and c[4] != ():
        listOfConn.append((str(c[6]) + " " + str(c[3][0])+'@'+str(c[3][1]) + " " + str(c[4][0])+'@'+str(c[4][1]) + " " + c[5]).split())

dict = {}

for item in listOfConn:
    if item[0] in dict:
        dict[item[0]] += 1
    else:
        dict[item[0]] = 1

listOfConn.sort(key = lambda x: -dict[x[0]])

for item in listOfConn:
    for i in item:
        if i != item[-1]:
            sys.stdout.write('"' + i + '"' + ",")
        else:
            print '"' + i + '"'
