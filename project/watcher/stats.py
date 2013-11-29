#!/usr/bin/env python3

class Stats():

	# pid = None
	# name = None
	# memory = None
	# cpu = None
	# connection = None
	# timestamp = None

	
	def __init__(self, name, pid, memory, cpu, thread, fds, connection, timestamp):
		self._name = name
		self._pid = pid
		self._memory = memory
		self._cpu = cpu
		self._connection = connection
		self._timestamp = timestamp
		self._fd = fds
		self._thread = thread
	
	@property
	def fd(self):
		return self._fd

	@fd.setter
	def fd(self, value):
		self._fd = value

	@property
	def thread(self):
		return self._thread

	@thread.setter
	def thread(self, value):
		self._thread = value

	@property
	def pid(self):
		return self._pid

	@pid.setter
	def pid(self, value):
		self._pid = value

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = value

	@property
	def memory(self):
		return self._memory

	@memory.setter
	def memory(self, value):
		self._memory = value

	@property
	def cpu(self):
		return self._cpu

	@cpu.setter
	def cpu(self, value):
		self._cpu = value
	
	@property
	def connection(self):
		return self._connection

	@connection.setter
	def connection(self, value):
		self._connection = value

	@property
	def timestamp(self):
		return self._timestamp

	@timestamp.setter
	def timestamp(self, value):
		self._timestamp = value

	@staticmethod
	def header():
		return "name, pid, memory, cpu, thread, fd, connection, timestamp\n"

	def __str__(self):
		return ",".join([self._name, str(self._pid), str(self._memory), str(self._cpu), 
			str(self._thread), str(self._fd), str(self._connection), str(self._timestamp)])


