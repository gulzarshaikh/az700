import os

file = os.system('ls ~gulzarshaikh/Desktop/RDPs/')
for list in file:
    fin = open('list', "rt")
    data = fin.read()
    data = data.replace('mohamed', 'gshaikh')
    fin.close()
   