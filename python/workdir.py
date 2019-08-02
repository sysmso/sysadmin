import os
import sys
import subprocess
from hurry.filesize import size,si
import logging
from logging.handlers import RotatingFileHandler

#Gestion des logs
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
file_handler = RotatingFileHandler('util-workdir.log', 'a', 1000000, 1)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

dirpath = "/workdir/"

logger.info("Occupation workdir \n")

for f in os.listdir(dirpath):
    fp = os.path.join(dirpath, f)
    s = int(subprocess.check_output(['du', '-sb', fp]).split()[0].decode('utf-8'))
    sr = s/(1024*1024)
    sr = round(sr, 2)
    siz = size(s, system=si)
    logger.info("%s %s" % (f, siz))
