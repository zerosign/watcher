#!/usr/bin/env python3
import sys
import os
import json
import argparse
import glob

from watcher.watcher import Watcher
from watcher.render import Renderer


parser = argparse.ArgumentParser(description="Watcher for a process")

def init_args():
    parser.add_argument('--action', nargs='?', default='watch',
            help='an action to do (watch|render)')
    parser.add_argument('--config', nargs='?', default="config.json",
            help='file config to be parsed')
    parser.add_argument('--output', nargs='?', default="output",
            help='default output folder')
    parser.add_argument('--input', nargs='?', help='file to be rendered')

if __name__ == "__main__":
    init_args()
    args = vars(parser.parse_args())

    if not os.path.exists(args['config']):
        sys.exit(-1)
 
    if not os.path.exists(args['output']):
        os.mkdir(args['output'])   
 
    Watcher.output_folder = args['output']
    Renderer.output_folder = args['output']


    if args['action'] == 'watch':
        config = Watcher.parse(json.loads("".join(open(args['config'], 'r').readlines())))
        watchers = [Watcher(conf) for conf in config]
        processes = [watcher.start() for watcher in watchers]

            # join all process
        for process in processes:
            process.join()

    elif args['action'] == 'render':
        renderer = Renderer()
        renderer.renders(paths=glob.glob(args['input']))
