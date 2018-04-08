import threading
import time

counter = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
	def __init__(self,name):
		threading.Thread.__init__(self)
		self.name = name

	def run(self):
		global counter, mutex
		time.sleep(1);
		if mutex.acquire():
			counter += 1
			print("I am %s, set counter:%s" % (self.name, counter))
			mutex.release()


if __name__ == "__main__":
	for i in range(0, 10):
		my_thread = MyThread("thread "+str(i))
		my_thread.start()
		# nohup python3 -u testDaemon.py > test.out 2>&1 &