# coding=utf-8
import json

partitionKey = dict()
CommunityAndCount = dict()
print(partitionKey)
with open("neo4jNode.dat",encoding='UTF-8') as r:
	lines = r.readlines()
	for line in lines:
		# print(type(line))
		dictline = json.loads(line)
		# print(type(dictline))
		if dictline['partitionKey'] in partitionKey.keys():
			CommunityAndCount[dictline['partitionKey']] += 1
			partitionKey[dictline['partitionKey']]['count'] += 1
			partitionKey[dictline['partitionKey']]['keywords'].append(dictline['name'])
		else:
			CommunityAndCount[dictline['partitionKey']] = 1
			dict = {}
			dict['count'] = 1
			dict['keywords'] = [dictline['name']]
			partitionKey[dictline['partitionKey']] = dict

		# print(line)
import random
import json
rand =random.seed(47)
print(len(partitionKey))
print(partitionKey)
print(partitionKey.keys())
dict = {}
dict["name"] = "community"
anslist = []
for key in partitionKey.keys():
	# print(key)
	# print(partitionKey[key]["keywords"])
	tempdict = {}
	list = partitionKey[key]["keywords"]
	tempdict["name"] = list[0]
	templist = []
	if len(list) > 20:
		print(len(list))
		for keyword in list:
			temp = {}
			temp["name"] = keyword
			temp["size"] = random.randint(1,200)
			templist.append(temp)
		tempdict["children"] = templist
		# print(tempdict)
		anslist.append(tempdict)
print(anslist)
dict["children"] = anslist
with open("Communityjson1.json","w",encoding='UTF-8') as w:
	w.write(json.dumps(dict))
	# for tdict in anslist:
	# 	w.write(json.dumps(tdict))
	# 	# w.write(",")
	# 	print(tdict)



	# dict["name"] = partitionKey[key][["keywords"][1]]
# {
#      "name": "graph",
#      "children": [
#       {"name": "BetweennessCentrality", "size": 3534},
#       {"name": "LinkDistance", "size": 5731},
#       {"name": "MaxFlowMinCut", "size": 7840},
#       {"name": "ShortestPaths", "size": 5914},
#       {"name": "SpanningTree", "size": 3416}
#      ]
#     }
