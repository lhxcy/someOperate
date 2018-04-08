import numpy as np
# print(np.zeros([1,5]))
# print(np.zeros(5))
# x = [1,2,3,4]
# y = ['a','b','c','d']
# z = list(zip(x,y))
# print(z)
# m,n = zip(*z)
# print(m)
# print(n)
# deleteNs = range(0, 1000, 20)
# print(deleteNs)
# for de in deleteNs:
# 	print(de)
# sumlist = np.ones([1,9])
# print(sumlist)
# print(np.sum(sumlist[0]))
# import random
# with open("剑指offer题目1.txt",'r',encoding='utf-8') as op:
# 	raw = op.readlines()
# 	print(raw)
# 	random.shuffle(raw)
# 	print(raw)
# print(len("我\n".strip('\n').strip('')))
# print(len("\n".strip('\n').strip('')))
import tensorflow as tf
index = tf.range(0,128)-1
print(tf.Session().run(index))