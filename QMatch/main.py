import xlrd
from tkinter import Tk

print("QMatch v0.1.1 Preview Version")
print("Code by github@CottonCandy2004")
print("*If you want to the Source Code, please view github@CottonCandy2004")
url=input("ExcelURL:")
print("读入校对库...")
with open("data.txt","r",encoding='utf-8') as d: #读入数据库
    datalistr=d.readlines()
    datalist=[]
    result=[]
    for i in datalistr:
        datalist.append(i.strip())
print("读入Excel...")
ex=xlrd.open_workbook(url.strip('"')) #读入excel
table = ex.sheets()[1]
nrows = table.nrows
name=table.col_values(0, start_rowx=0, end_rowx=nrows)
satus=table.col_values(2, start_rowx=0, end_rowx=nrows)
e=[]
print("正在校对...")
for i in range(nrows): #筛出在会议室的人员
    if satus[i]=="--":
        e.append(name[i])
result=datalist[:]
for i in datalist: #比对
    for a in e:
        b=a.find(i)
        if b!=-1:
            result.remove(i)
            break
print("\n以下人员未在当前会议室：")
print(result)
r = Tk()
r.withdraw()
r.clipboard_append(result)
r.update()
r.destroy()
print("结果已推送到剪贴板。")
input("按回车键以退出...")
