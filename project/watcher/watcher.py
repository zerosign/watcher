#!/usr/bin/env python

from multiprocessing import Process, Manager
import psutil
import time
import os
from datetime import timedelta, datetime
from .helper import TimeHelper
from .stats import Stats, EmptyStats

class Watcher():

    output_folder = None

    def __init__(self, config=()):
        self.pid = int(config[0][0])
        self.name = config[0][1]
        self.config = config[1]
        filename =  "%s/%s-%d.output" % (Watcher.output_folder, 
                                         self.name, self.pid)
        existed = os.path.exists(filename)
        self.output = open(filename, 'a')

        if not existed:
            self.output.write(Stats.header())

    @staticmethod
    def fetch(watcher):
        stats = EmptyStats()
        try: 
            p = psutil.Process(watcher.pid)
            mem_usage_total = sum(p.get_memory_info())
            stats = Stats(watcher.name, watcher.pid,
                          mem_usage_total, 
                          p.get_cpu_percent(1), 
                          len(p.get_threads()), p.get_num_fds(),
                          len(p.get_connections()), time.time())

        except Exception as ex:
            print(ex)
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
            if not isinstance(stats, EmptyStats):
                # print( "%s\n" % str(stats) )
                watcher.output.write("%s\n" % str(stats))
                watcher.output.flush()
            else:
                break

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
                config_new.append(((proc.pid, proc.name), 
                                   config[proc.name]))
                return config_new


    def __str__(self):
        return ",".join([self.pid, self.name, self.config])
