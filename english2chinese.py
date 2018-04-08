#coding :utf-8
import json
i = 1
j = 1

with open("C:\\Users\\XCY\\Desktop\\en-zh\\src-val.txt","w", encoding='UTF-8') as w:
	with open("C:\\Users\\XCY\\Desktop\\en-zh\\train.en.txt","r", encoding='UTF-8') as r:
		for line in r.readlines():
			if i <= 1000:
				print(line)
				w.write(line)
				i += 1
	print("Done")

with open("C:\\Users\\XCY\\Desktop\\en-zh\\tgt-val.txt","w", encoding='UTF-8') as w:
	with open("C:\\Users\\XCY\\Desktop\\en-zh\\train.zh.txt","r", encoding='UTF-8') as r:
		for line in r.readlines():
			if j <= 1000:
				print(line)
				w.write(line)
				j += 1
	print("Done")

		# src - train.txt
		# tgt - train.txt
		# src - val.txt
		# tgt - val.txt