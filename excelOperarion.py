# coding=utf-8
# import xlrd
#
# # 打开Excel文件读取数据
# data = xlrd.open_workbook("/home/yxj/Downloads/xcy/antuor.xlsx")
#
# # 获取一个工作表
# table = data.sheets()[0]  #通过索引顺序获取
# # table = data.sheet_by_index(0) #通过索引顺序
# # table = data.sheet_by_name("") #通过名称获取
#
# #获取整行整列的值（数组）
# # table.row_values(0)   #获取第0行数据
# # table.col_values(0)   #获取第0列数据
# print(table.row_values(0))
# print(table.row_values(1))
# print(table.row_values(2))
#
# #获取行数和列数
# rows = table.nrows #行数
# print(rows)
# cols = table.ncols #列数
# print(cols)
#
# #循环行列表数据
# # for i in range(rows):
# #     print(table.row_values(i))
#
# #单元格
# cell_A = table.cell(0,0).value
# print(cell_A)
# cell_C4 = table.cell(2,3).value
# print(cell_C4)
#
#
# #使用行索引
# cell_A1 = table.row(0)[0].value
# print(cell_A1)
# cell_A2 = table.row(1)[0].value
# print(cell_A2)
#
#
# # #简单的写入
# # row = 0
# # col = 0
# # #类型 0 empty, 1 Sreing, 2 number. 3 date, 4 boolean, 5 error
# # ctype = 1
# # value = "单元格的值"
# # xf = 0 #扩展的格式
# # table.put_cell(rowx=row, colx=col, ctype=ctype, value=value, xf_index=xf)
# # table.cell(0,0) #单元格的值
# # table.cell(0,0).value #单元格的值
#


#demo
import xdrlib,sys
import xlrd
def open_excel(file = "/home/yxj/Downloads/xcy/antuor.xlsx"):
    try:
        data = xlrd.open_workbook(filename=file)
        return data
    except Exception as e:
        print(e)

#根据索引获取excel表中的数据， 参数 file：Excel路径    colnameIndex：表头列名所在的行   byIndex： 表的索引
def excel_table_byindex(file = "author.xlsx", colnameIndex = 0, byIndex = 0):
    data = open_excel(file)
    table = data.sheets()[byIndex]
    rows = table.nrows
    cols = table.ncols
    colnames = table.row_values(colnameIndex)
    print(colnames)
    list = []
    for rownum in range(1, rows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list


#根据名称获取excel表中的数据， 参数 file：Excel路径    colnameIndex：表头列名所在的行   byIndex： Sheet名称
def excel_table_byName(file = "author.xlsx", colnameIndex = 0, byName = "Sheet1"):
    data = open_excel(file)
    table = data.sheet_by_name(byName)
    rows = table.nrows
    colnames = table.row_values(colnameIndex)
    print(colnames)
    list = []
    for rownum in range(1,rows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    return list

def main():
    table = excel_table_byindex(byIndex=0)
    for i in range(0,10):
        print(table[i])

    print("-------------------------------------------------")
    tables = excel_table_byName(byName="Sheet3")
    for i in range(1, 10):
        print(tables[i])


if __name__ == "__main__":
    main()




