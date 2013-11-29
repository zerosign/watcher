#!/usr/bin/env python3
import sys
import os
import json

from watcher.watcher import Watcher

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Error : Argument needs more")
		sys.exit(-1)

	path = sys.argv[1]
	
	print("Using config path : %s " % path) 
	
	if not os.path.exists(path):
		sys.exit(-1)
	
	config = Watcher.parse(json.loads("".join(open(path, 'r').readlines())))
	watchers = [Watcher(conf) for conf in config]
	processes = [watcher.start() for watcher in watchers]
	
	# join all process
	for process in processes:
		process.join()

