import re
import os

f = open('/Users/student/Desktop/Камилова/file.txt', 'r', encoding='utf8')

text = f.read()

f.close()

result = re.findall(r'[А-Я]. [А-Я][а-я]+', text)

for item in result:
    list1 = item.split()
    dirname = list1[1]
    print(dirname)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = item
    f = open(dirname+'/'+filename, 'w')
    f.write(item)
    f.close()


result = re.findall(r'[А-Я]. [А-Я]. [А-Я][а-я]+', text)

for item in result:
    list2 = item.split()
    dirname = list2[2]
    print(dirname)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = item
    f = open(dirname+'/'+filename, 'w')
    f.write(item)
    f.close()

result = re.findall(r'[А-Я][а-я]+ [А-Я][а-я]+', text)

for item in result:
    list3 = item.split()
    dirname = list3[1]
    print(dirname)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    filename = item
    f = open(dirname+'/'+filename, 'w')
    f.write(item)
    f.close()
    

