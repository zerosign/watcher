#!/usr/bin/env python

from multiprocessing import Process, Manager
import psutil
import json
from datetime import timedelta


class Watcher():
	
	def __init__(self, config=()):
		self.pid = config[0][0]
		self.name = config[0][1]
		self.config = config[1]
		self.output = open(self.pid + '.output', 'a')

	@staticmethod
	def watch(watcher):
		output = watcher.output
		pid = watcher.pid
		timespan = TimeHelper.parse(watcher.config["timespan"])
		
		while True:
			state = State(watcher.name, pid, )
			output.write(str(state))
		output.close()

	def start(self):
		self.process = Process(target=Watcher.watch, args=(self))
		self.process.start()
		
		return self.process

	@staticmethod
	def parse(config={}):
		config_new = ()
		proc_names = [proc_name[0] for proc_name in config.items()]
		for proc in psutil.process_iter():
			if proc.name in proc_names:
				config_new = config_new + ((proc.pid, proc.name), config[proc.name])
		return config_new


