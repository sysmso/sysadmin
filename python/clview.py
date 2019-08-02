#!/usr/bin/env python
#
# Author: Martin Souchal <souchal@apc.in2p3.fr>
# Date  : 12 avril 2018
# Desc. : Cluster resources overview
#
#
#

import pbs
from PBSQuery import PBSQuery
from PBSQuery import PBSError
from tabulate import tabulate
import sys
import re

def main():
    p = PBSQuery()
    p.new_data_structure()
    nodes = p.getnodes()
    l=list()
    jobs = "none"
    for id in nodes:
        try:
            queue = nodes[id].properties[0]
            state = nodes[id].state[0]
            power = nodes[id].power_state[0]
            np = nodes[id].np[0]
            name = nodes[id].name
            memory = nodes[id].status.physmem[0]
            memory = memory[:-2]
            memory = int(memory)
            memory = memory/1000000
            load = nodes[id].status.loadave[0]
            display = " "
            if hasattr(nodes[id],"jobs"):
                jobs = nodes[id].jobs
                results = len(jobs)
                for result in range(results):
                    display += "x"
                #result = str()
                #s = ", "
                #result = s.join(jobs)
            else:
                display = "0"
            l.append([name,state,power,queue,np,memory,load,display])
        except PBSError, detail:
            print detail
        pass
    l.sort()
    print tabulate(l, headers=["Node","State", "Power state", "Queue", "CPU", "MEM", "Load", "jobs"], tablefmt="rst")
    
main()
