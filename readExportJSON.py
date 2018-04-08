# coding=utf-8
import json
with open("neo4jNode.dat","w",encoding='UTF-8') as w:
	with open("result.json",encoding='UTF-8') as r:
		lines = r.readlines()
		for line in lines:
			line = json.loads(line)
			for lin in line['data']:
				# print(type(lin))
				if 'partitionKey' in lin['row'][0].keys():
					w.write(json.dumps(lin['row'][0],ensure_ascii=False))
					w.write('\n')
					# print(str(lin['row']))
					print(lin['row'][0])
