#!/usr/bin/env python3

from datetime import timedelta
import re

# regex using capture group
TIME_REGEX = re.compile(r'((?P<hours>\d+?)hr)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)s)?')

DEFAULT_TIMESPAN = "1hr"

class TimeHelper():

	@staticmethod
	def parse(timestr):
		group = TIME_REGEX.match(timestr)
		if not group:
			print("Error in parsing timespan, using default timespan %s" % (DEFAULT_TIMESPAN))
			return parse(DEFAULT_TIMESPAN)
		
		time_group = group.groupdict()
		time_params = {}
		timespan = 0
		print(str(time_group))
		for key in time_group:
			value = time_group[key]
			if value:	
				time_params[key] = int(value)

		return timedelta(**time_params)


