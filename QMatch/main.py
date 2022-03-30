import xlrd
url=input("ExcelURL:")
with open("data.txt","r") as d:
    datalistr=d.readlines()
    datalist=[]
    result=[]
    for i in datalistr:
        datalist.append(i.strip())
        result.append(i.strip())
# 这里插入excel读入
ex=xlrd.open_workbook(url)
table = ex.sheets()[1]
nrows = table.nrows
name=table.col_values(0, start_rowx=0, end_rowx=nrows)
satus=table.col_values(2, start_rowx=0, end_rowx=nrows)
e=[]
for i in range(nrows):
    if satus[i]=="--":
        e.append(name[i])
for i in datalist:
    for a in e:
        b=a.find(i)
        if b!=-1:
            result.remove(i)
print(result)
# print(datalist)
input()