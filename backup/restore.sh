#!/bin/bash
# Réinstalle tous les paquets sauvegardés dans le fichiers liste.txt
LIST="$(cat list.txt)"
for s in $LIST; do yum -y install $s; done 
