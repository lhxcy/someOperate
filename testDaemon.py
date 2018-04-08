import time
i=0
while(True):
	i += 1
	print(i)
	time.sleep(1)
	print(i,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


# nohup python3 -u multi_threading.py > spider.out 2>&1 &
# 	11239


# multi_threading.py