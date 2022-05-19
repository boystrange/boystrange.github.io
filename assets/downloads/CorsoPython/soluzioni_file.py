#!/usr/bin/env python3

import sys

def collect(filename):
    d = dict()
    f = open(filename)
    for line in f:
        ip = line.split()[0]
        d[ip] = d.get(ip, 0) + 1
    return d

def show_results(d):
    l = [ (c, ip) for (ip, c) in d.items() ]
    l.sort(reverse=True)
    for (c, ip) in l:
        print(ip.ljust(15), '#'*c)

show_results(collect(sys.argv[1]))
