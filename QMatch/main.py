import xlrd

with open("data.txt","r") as d:
    datalistr=d.readlines()
    datalist=[]
    for i in datalistr:
        datalist.append(i.strip())
# # 这里插入excel读入
# ex=xlrd.open_workbook(r"示例.xlsx")
# table = ex.sheets()[1]
# nrows = table.nrows
# name=table.col_values(0, start_rowx=0, end_rowx=nrows)
# satus=table.col_values(3, start_rowx=0, end_rowx=nrows)
# e=[]
# for i in range(nrows):
#     if satus[i]=="--":
#         e.append(name[i])
# result=[]
# for i in datalist:
#     r=e.find(i)
#     if r==-1:
#         result.append(i)
# print(result)
print(datalist)