# ecoding=utf-8
#批量去除文本空格和标点符号
import re

dataDuan = r"C:\Users\DUTONG\Desktop\jianmo\train\xw1.txt"
ofn = r"C:\Users\DUTONG\Desktop\jianmo\data\d1.txt"#存放去除标点符号的文件路径
newpathxw = dataDuan
newpathda = ofn
for i in range(1,31):#文件名为xw1-31含30个文件
    stringWith = ''
    with open(newpathxw,encoding='utf-8') as f:
        for line in f:
            stringWith += line.lower()

    num = re.sub(r'[^a-z]', "", stringWith)
    with open(newpathda, 'w',encoding='utf-8') as f:
        f.write(num)
    newpathxw = newpathxw.replace(str(i),str(i+1))
    newpathda = newpathda.replace(str(i),str(i+1))
    print('text',i,'is','ok')
