#!/bin/bash
# Montage CIFS sous linux
mount -t cifs //xxx.xxx.xxx.xxx/Qualite /mnt/cifs/ -o user=sysmso -o domain=workgroup
