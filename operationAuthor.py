# coding=utf-8
import excelOperarion

#写出作者和作者所属机构
with open("authur_address.dat","w",encoding='UTF-8') as w:
	list = []
	table = excelOperarion.excel_table_byindex(byIndex=0)
	for i in range(len(table)):
		list = table[i]['full_address'].split(',')
		if ' 中国' in list:
			print(list)
			w.write(table[i]['full_name']+','+list[0]+'\n')