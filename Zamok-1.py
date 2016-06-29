import re

f = open('/Users/student/Desktop/Камилова/file.txt', 'r', encoding='utf8')
text = f.read()
f.close()
result = re.findall(r'[А-Я]. [А-Я][а-я]+', text)
for item in result:
    print(item)
    
