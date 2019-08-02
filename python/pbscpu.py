#!/usr/bin/env python
#
# Author: Martin Souchal <souchal@apc.in2p3.fr>
# Date  : 20 oct 2016
# Desc. : CPU slot report for APC Cluster
#
#
#
#
import pbs
from PBSQuery import PBSQuery
from PBSQuery import PBSError
import sys
import re

def countcpu(queue):
    p = PBSQuery()
    p.new_data_structure()
    nodes = p.getnodes()
    nptot = 0
    for id in nodes:
        if nodes[id].properties == [queue]:
            try:
                np = nodes[id].np
                np = int(np[0])
                nptot = nptot + np
            except PBSError, detail:
                print detail
            pass
    return nptot

def countppn(queue):
    p = PBSQuery()
    p.new_data_structure()
    jobs = p.getjobs()
    nptot = 0
    for id in jobs:
        try:
            if jobs[id].queue[0] == queue and jobs[id].job_state[0] == 'R':
                np = jobs[id].Resource_List.nodes
                if 'ppn' not in np[0]:
                    np = 1
                else:
                    npptot = 0
		    ct = [m.start() for m in re.finditer('ppn', np[0])]
                    for val in ct:
                        char = np[0]
                        vals = val+4
                        valf = val+6
                        npp = char[vals:valf]
			npp = re.sub('[!@#+:$]', '', npp)
                        npp = int(npp)
			npptot = npp + npptot
                    np = npptot
                nptot = np + nptot
        except PBSError, detail:
            print detail
        pass
    return nptot

def main():
    print "CPU cluster usage :"
    p = PBSQuery()
    queues = p.getqueues()
    for queue in queues.keys():
        np = countcpu(queue)
        npp = countppn(queue)
        print "%s : [ %s / %s ] " % (queue,npp,np)

main()
