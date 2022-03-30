import xlrd

url=input("ExcelURL:")
with open("data.txt","r",encoding='utf-8') as d: #读入数据库
    datalistr=d.readlines()
    datalist=[]
    result=[]
    for i in datalistr:
        datalist.append(i.strip())
ex=xlrd.open_workbook(url.strip('"')) #读入excel
table = ex.sheets()[1]
nrows = table.nrows
name=table.col_values(0, start_rowx=0, end_rowx=nrows)
satus=table.col_values(2, start_rowx=0, end_rowx=nrows)
e=[]
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
print(result)
input("按回车键以退出...")
