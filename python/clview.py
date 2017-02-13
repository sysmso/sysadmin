#!/usr/bin/env python

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
		if len(jobs) > 1:
                    jobs = jobs[1]
	        else:
		    jobs = jobs[0]	
            else:
                jobs = "none"
            l.append([name,state,power,queue,np,jobs])
        except PBSError, detail:
            print detail
        pass
    l.sort()
    print tabulate(l, headers=["Node","State", "Power state", "Queue", "CPU", "jobs"], tablefmt="rst")
    
main()
