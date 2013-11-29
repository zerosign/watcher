#!/usr/bin/env python

from multiprocessing import Process, Manager
import psutil
import time
import os
from datetime import timedelta, datetime
from .helper import TimeHelper
from .stats import Stats

class Watcher():
	
	def __init__(self, config=()):
		self.pid = int(config[0][0])
		self.name = config[0][1]
		self.config = config[1]
		filename =  "%d.output" % (self.pid)
		existed = os.path.exists(filename)
		self.output = open(filename, 'a')

		if not existed:
			self.output.write(Stats.header())

	@staticmethod
	def fetch(watcher):
		p = psutil.Process(watcher.pid)

		stats = Stats(watcher.name, watcher.pid, p.get_memory_percent(), p.get_cpu_percent(1), 
				len(p.get_threads()), p.get_num_fds(),
				len(p.get_connections()), time.time())

		return stats

	@staticmethod
	def watch(watcher):
		timespan = TimeHelper.parse(watcher.config["timespan"])
		start = datetime.now()
		while True:
			result = (datetime.now() - start) < timespan
			# print(result)
			if not result:
				break
			stats = Watcher.fetch(watcher)
			# print( "%s\n" % str(stats) )
			watcher.output.write("%s\n" % str(stats))
			watcher.output.flush()
		watcher.output.close()

	def start(self):
		self.process = Process(target=Watcher.watch, args = [self])
		self.process.start()
		return self.process

	@staticmethod
	def parse(config={}):
		config_new = []
		proc_names = [proc_name[0] for proc_name in config.items()]
		for proc in psutil.process_iter():
			if proc.name in proc_names:
				config_new.append(((proc.pid, proc.name), config[proc.name]))
		return config_new

	
	def __str__(self):
		return ",".join([self.pid, self.name, self.config])
