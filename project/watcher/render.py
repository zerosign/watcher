import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as mplot
from .stats import Stats
import csv


class Renderer():
    output_folder = None
    def render_single(self, name, label, x=[], y=[]):
        print(len(x))
        print(len(y))
        plot = mplot.plot(x, y, label=label)
        mplot.legend()

    def renders(self, paths=[]):
        for path in paths:
            self.render(path=path)

        mplot.show()

    def render(self, path=None):
        print("Rendering the output of %s" % (path))
        headers = []
        data = {}
        times = []


        with open(path, "r") as f:
            headers = Stats.get_header(f)
            for h in headers:
                if not h == 'timestamp':
                    data[h] = []

            print(data)
            first_time = 0

            reader = csv.reader(f, delimiter=',')
            for cols in reader:
                for ii in range(0, len(headers)):
                    if ii < len(headers)-1:
                        data[headers[ii]].append(cols[ii])
                    else:
                        if first_time == 0:
                            first_time = float(cols[ii])
                        times.append(float(cols[ii])-first_time)
            f.close()


            size = len(data.keys())

            ii = 1
            for header in headers[0:len(headers)-1]:
                p = mplot.subplot(len(headers), 1, ii)
                p.set_title(header)
                self.render_single(header, path, times, data[header])
                ii += 1
