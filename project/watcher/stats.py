#!/usr/bin/env python3

class Stats():

	pid = None
	name = None
	memory = None
	cpu = None
	connection = None
	timestamp = None


	def __init__(self, name, pid, memory, cpu, connection, timestamp):
		self.name = name
		self.pid = pid
		self.memory = memory
		self.cpu = cpu
		self.connection = connection
		self.timestamp = timestamp

	@property
	def pid(self):
		return self.pid

	@pid.setter
	def pid(self, value):
		self.pid = value

	@property
	def name(self):
		return self.name
	
	@name.setter
	def name(self, value):
		self.name = value

	@property
	def memory(self):
		return self.memory

	@memory.setter
	def memory(self, value):
		self.memory = value

	@property
	def cpu(self):
		return self.cpu

	@cpu.setter
	def cpu(self, value):
		self.cpu = value
	
	@property
	def connection(self):
		return self.connection

	@connection.setter
	def connection(self, value):
		self.connection = value

	@property
	def timestamp(self):
		return self.timestamp

	@timestamp.setter
	def timestamp(self, value):
		self.timestamp = value

	@staticmethod
	def header():
		return "name, pid, memory, cpu, connection, timestamp"

	def __str__(self):
		return ",".join([self.name, self.pid, self.memory, self.cpu, self.connection, self.timestamp])


