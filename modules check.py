from pathlib import Path
import os,pprint,shutil

Py3_11 = Path(r'C:\Users\Anjal\AppData\Local\Programs\Python\Python311\Lib\site-packages')
Py3__8 = Path(r'C:\Python38\Lib\site-packages')

files_in_Py3_11 = list(Py3_11.glob('*'))
files_in_Py3_8 = list(Py3__8.glob('*'))
filesofpy11 = []
filesofpy8 = []
notin11 =[]
notin8 = []
for bruh in files_in_Py3_11:
    filesofpy11.append(bruh.name)

for paper in files_in_Py3_8:
    filesofpy8.append(paper.name)


for file in filesofpy8:
    if  not file in filesofpy11:
        notin11.append(file)

for file in filesofpy11:
    if  not file in filesofpy8:
        notin8.append(file)


if notin11 == []:
    notin11 = 'nothing'

if notin8 == []:
    notin8 = 'nothing'
print(f"Files that are not in python 3.11 but in python 3.8 are:")

pprint.pp(notin11)
if notin11 != 'nothing':
    for i in notin11:
        pathoffile = Path(f'C:\\Python38\\Lib\\site-packages\\{i}')
        shutil.move(pathoffile,r'C:\Users\Anjal\AppData\Local\Programs\Python\Python311\Lib\site-packages')

# print(f"Files that are not in python 3.8 but in python 3.11 are:")
# pprint.pp(notin8)

# if notin8 != 'nothing':
#     if notin8 != 'nothing':
#         for i in notin8:
#             pathoffile = Path(f'C:\\Users\\Anjal\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\{i}')
#             shutil.copy(pathoffile,r'C:\Python38\Lib\site-packages')