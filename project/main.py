#!/usr/bin/env python3
import sys
import os

from watcher.watcher import Watcher
from watcher.stats import Stats
from watcher.helper import TimeHelper

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error : Argument needs more")
		sys.exit(-1)

	path = sys.argv[1]
	print("Using config path : %s " % path) 
	if not os.path.exists(path):
		sys.exit(-1)
	
	config = open(path, 'r').readlines()
	config = Watcher.parse(config)

	#watchers = map[Watcher(conf) for conf in config]
	#processes = map[lambda watcher: watcher.start(), watchers]
	
	# join all process
	#for process in processes:
		#process.join()

