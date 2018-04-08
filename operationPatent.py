# coding=utf-8
import excelOperarion

#专利名字和作者
with open("patent.dat","w",encoding='UTF-8') as w:
	table = excelOperarion.excel_table_byindex(file="paper.xlsx",byIndex=1)
	# for i in range(10):
		# print(table[i])
		# print(table[i]['name'].split('|')[0],'\t',table[i]['inventors'].replace('；','|'))
	for i in range(len(table)):
		if table[i]["name"] != '':
			print(table[i]['name'].split('|')[0],'\t',table[i]['inventors'].replace('；','|'))
			w.write(table[i]['name'].split('|')[0] + ',' + table[i]['inventors'].replace('；','|') + '\n')
