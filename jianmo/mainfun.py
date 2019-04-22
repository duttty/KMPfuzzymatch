#主函数,dataDuan为母文本
#目录下需要有名为d-30的文本
import os,math,re,time
# from test import kmp_match   #速度慢于kmp
from kmpAgr import kmp
start = time.time()

dataDuan = r'C:\Users\DUTONG\Desktop\jianmo\data\d1.txt'
pian = ''
duan = ''
duan2 = ''
fitDic = set()
dict_1 = {}
myIndex = 5
cutLen = 1
with open(dataDuan,'r',encoding=('utf-8')) as f:
    duan = f.read()

newpath = dataDuan
for i in range(1,30):
    newpath = newpath.replace(str(i),str(i+1))
    print(i)
    with open(newpath,'r',encoding='utf-8') as s:
        pian = s.read()
        # print(len(pian))
    lenPian = len(pian)-myIndex+cutLen
    for j in range(lenPian):            #遍历A段，切片为符合长度的片,这里取长度为6的单词,考虑替换为1
        preFitWord = pian[j:j+myIndex-cutLen]
        fit = kmp(duan,preFitWord)
        if fit:
            # fitDic.add(preFitWord)  #写入单词中缀
            dict_1.setdefault(duan[fit-cutLen:fit+myIndex-cutLen],0)  #写入满足条件单词到字典value为出现次数
            dict_1[duan[fit-cutLen:fit+myIndex-cutLen]] =  dict_1[duan[fit-cutLen:fit+myIndex-cutLen]] + 1
            dict_1.setdefault(duan[fit:fit+myIndex],0)
            dict_1[duan[fit:fit+myIndex]] = dict_1[duan[fit:fit+myIndex]] + 1
            # print(duan[fit:fit+4])
# with open('fitdic.txt','w',encoding='utf-8') as di1:
#     data = '\n'.join(dict_1)
#     di1.write(data)


# newpath = dataDuan
# for i in range(2,30):
#     newpath = newpath.replace(str(i-1),str(i))
#     print(newpath)
#     duan2 = ''
#     with open(newpath,'r',encoding='utf-8') as f:
#         duan2 = f.read()#读取新段落
#     testDic = dict_1.copy()#拷贝中缀 fitDic  拷贝字典dict_1
#     for ci in testDic:
#         fit = kmp(duan2,ci)
#         if not fit:
#             print(ci,'is not in d'+str(i))
#             dict_1.remove(ci)
d_order=sorted(dict_1.items(),key=lambda x:x[1],reverse=True)
d_order = str(d_order)
d_order = re.sub(r'\)',r'\n',d_order)
d_order = d_order.replace(r',','').replace(r'(','').replace(r'[','').replace(r']','')
with open('fitdic.txt','w',encoding='utf-8') as y:
    y.write(str(d_order))#写入满足条件的单词

end = time.time()
print("it  cost %s s for func running " %(round((end - start),4)))
