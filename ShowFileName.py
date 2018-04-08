#coding=utf-8
import os
def GetFileList(dir, fileList):
	for s in os.listdir(dir):
		print(s)
		fileList.append(s)
	return fileList
if __name__ =="__main__":
	str = 'E:\\testName'
	list = GetFileList(str,[])
	count = 0
	print(list)



# str = 'E:\\testName'
# str = 'c.old.wanfangdata.com.cn'
# print(len(os.listdir(str)))

# def GetFileList(dir, fileList):
# count = 0
# def GetFileList(dir, fileList):
# 	# print(dir)
# 	# global count
# 	# newDir = dir
# 	print(len(os.listdir(dir)))
# # GetFileList('c.old.wanfangdata.com.cn', [])
# 	# for s in os.listdir(dir):
# 	# 	# 如果需要忽略某些文件夹，使用以下代码
# 	# 	# if s == "xxx":
# 	# 	# continue
# 	# 	newDir = os.path.join(dir, s)
# 	# 	if os.path.isfile(newDir):
# 	# 		# print(newDir)
# 	# 		count += 1
# 	# 		print(count)
# 		# fileList.append(dir)
# 	# elif os.path.isdir(dir):
# 	# 	for s in os.listdir(dir):
# 	# 		#如果需要忽略某些文件夹，使用以下代码
# 	# 		#if s == "xxx":
# 	# 			#continue
# 	# 		newDir=os.path.join(dir,s)
# 	# 		GetFileList(newDir, fileList)
# 	# return count
#
# GetFileList('E:\\testName', [])
# # count = GetFileList('c.old.wanfangdata.com.cn', [])
# # print(count)
# # # print(list[:5])
# # i = 0
# # for e in list:
# # 	i += 1
# # 	if i < 5:
# # 		print (e)
