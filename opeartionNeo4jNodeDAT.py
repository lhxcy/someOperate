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

print(len(partitionKey))
print(partitionKey)
# print(partitionKey[5328])
SortList = (sorted(CommunityAndCount.items(),key=lambda x:x[1],reverse=True))
print(SortList)
print(len(SortList))
print(SortList[0])
print(len(SortList))

i = 1
with open("CommunityNode.dat1","w",encoding='UTF-8') as w:
	for index in range(len(SortList)):
		communityIndex = SortList[index][0]
		if partitionKey[communityIndex]['count'] > 10:#83
			print(communityIndex)
			i += 1
			print(partitionKey[communityIndex]['keywords'])
			w.write("CommuniyIndex\t")

			w.write(str(communityIndex))
			w.write("\tCommuniyMember\t")
			w.write(str(partitionKey[communityIndex]['count']))
			w.write('\n')
			w.write('\n')
			for keyword in partitionKey[communityIndex]['keywords']:
				w.write(keyword)
				w.write('\n')
			w.write('\n')


print(i)