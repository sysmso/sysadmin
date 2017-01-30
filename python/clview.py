#!/usr/bin/env python
# Utilisation en temps réel du cluster
# Instant utilisation of the cluster (Node name, State, Power State, queue allocation, numbers of core and jobs
# Martin Souchal 2017

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
    for id in nodes:
        try:
            queue = nodes[id].properties[0]
            state = nodes[id].state[0]
            power = nodes[id].power_state[0]
            np = nodes[id].np[0]
            name = nodes[id].name
            if hasattr(nodes[id],"jobs"):
                jobs = nodes[id].jobs[0].split('/')
                jobs = jobs[1]
            else:
                jobs = "none"
            l.append([name,state,power,queue,np,jobs])
        except PBSError, detail:
            print detail
        pass
    l.sort()
    print tabulate(l, headers=["Node","State", "Power state", "Queue", "CPU", "jobs"], tablefmt="rst")
    
main()
