# coding=utf-8
import excelOperarion

#论文题目和关键字
with open("paper.dat","w",encoding='UTF-8') as w:
	table = excelOperarion.excel_table_byindex(file="paper.xlsx",byIndex=0)
	for i in range(len(table)):
		if table[i]["title_cn"] != '':
			print(table[i]["title_cn"], '\t', table[i]["keywords_cn"])
			w.write(table[i]["title_cn"] + ',' + table[i]["keywords_cn"] + '\n')
