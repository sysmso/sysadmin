#!/bin/sh
REPOSITORY=/mnt/save
#REPOSITORY=/bkp/repo
/usr/bin/sshfs souchal@apcnis01.in2p3.fr:/portables/comput/apcnb170 /mnt/
# Backup all of /home and /etc except a few
# excluded directories
borg create -v --stats --compression lz4 --progress       \
    $REPOSITORY::'{hostname}-{now:%Y-%m-%d}'    \
    /home                                       \
    /etc                                        \
    --exclude '/home/*/.cache'                  \
    --exclude '/home/*/Videos'                  \
    --exclude '/home/*/Pictures'                \
    --exclude '/home/*/Music'                   \
    --exclude /home/ssysmso/AUR                 \
    --exclude '*.avi'                           \
    --exclude '*.mkv'                           \
    --exclude '*.mp4'                           \
    --exclude '*.iso'                           \
    --exclude '*.mp3'

# Use the `prune` subcommand to maintain 7 daily, 4 weekly and 6 monthly
# archives of THIS machine. The '{hostname}-' prefix is very important to
# limit prune's operation to this machine's archives and not apply to
# other machine's archives also.
borg prune -v $REPOSITORY --prefix '{hostname}-' \
    --keep-daily=7 --keep-weekly=4 --keep-monthly=6
/usr/bin/umount /mnt
