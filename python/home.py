import os
import sys
import subprocess
from hurry.filesize import size,si

dirpath = "/home/"

sys.stdout.write("Liste des home depassant le quota de 4G : \n")

for f in os.listdir(dirpath):
    fp = os.path.join(dirpath, f)
    s = int(subprocess.check_output(['du', '-sb', fp]).split()[0].decode('utf-8'))
    sr = s/(1024*1024)
    sr = round(sr, 2)
    siz = size(s, system=si)
    if sr > 4000:
        sys.stdout.write(" %s %s \n" % (f, siz))
        sys.stdout.flush()
