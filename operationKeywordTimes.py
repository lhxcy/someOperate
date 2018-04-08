# coding=utf-8
import json
import random
def getKWDict():
	kwTimesdict = {}
	with open("keywordTimes.dat",encoding='UTF-8') as r:
		lines = r.readlines()
		for line in lines:
			# print(line)
			# print(type(line))
			listline = line.strip('\n').split("\t")
			kwTimesdict[listline[0]] = listline[1]
	return kwTimesdict
	# print(kwTimesdict)
	# for key in kwTimesdict:
	# 	print(key," ",kwTimesdict[key])

def getCommunityPartitionKeyDict():
	partitionKey = {}
	CommunityAndCount = {}
	# print(partitionKey)
	with open("neo4jNode.dat", encoding='UTF-8') as r:
		lines = r.readlines()
		for line in lines:
			dictline = json.loads(line)
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
	return partitionKey

			# print(line)

def writeCommunityJsonNoRandom(partitionKey,kwTimesdict):
	print(len(kwTimesdict))
	dict = {}
	dict["name"] = "community"
	anslist = []
	countUp20 = 0
	for key in partitionKey.keys():
		# print(key)
		# print(partitionKey[key]["keywords"])
		tempdict = {}
		list = partitionKey[key]["keywords"]
		tempdict["name"] = list[0]
		templist = []
		if len(list) > 20:
			countUp20 += 1
			# print(len(list))
			# print(list)
			for keyword in list:
				temp = {}
				temp["name"] = keyword
				temp["size"] = kwTimesdict[keyword]
				templist.append(temp)
			tempdict["children"] = templist
			# print(tempdict)
			anslist.append(tempdict)
	# print(anslist)
	print(countUp20)
	dict["children"] = anslist
	with open("CommunityjsonNoRandom.json", "w", encoding='UTF-8') as w:
		w.write(json.dumps(dict))

def writeCommunityJsonRandom(partitionKey):
	random.seed(47)
	# print(len(partitionKey))
	# print(partitionKey)
	# print(partitionKey.keys())
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
			# print(len(list))
			for keyword in list:
				temp = {}
				temp["name"] = keyword
				temp["size"] = random.randint(1, 300)
				templist.append(temp)
			tempdict["children"] = templist
			# print(tempdict)
			anslist.append(tempdict)
	# print(anslist)
	dict["children"] = anslist
	with open("CommunityjsonRandom.json", "w", encoding='UTF-8') as w:
		w.write(json.dumps(dict))


if __name__ == "__main__":
	#
	kwTimesdict = getKWDict()
	partitionKey = getCommunityPartitionKeyDict()
	writeCommunityJsonRandom(partitionKey)
	writeCommunityJsonNoRandom(partitionKey,kwTimesdict)


