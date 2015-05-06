#!/bin/sh
# Sauvegarde systeme via rsync
# répertoire de destination
DEST=/backup/
# Nombre de jours au-delà duquel on supprime les anciens backups
DAYS=300
# Nom de la machine
HOST="sysmso"

RSYNC_OPTIONS="-P -H"
if [ ! -d "$DEST" ]
then
  echo "répertoire inconnu"
  exit 1
fi
# Création du dossier
NOW="${HOST}_`date +%Y%m%d`"
LINKDEST=""
for i in `ls -rt $DEST|tail -3`
do
if [ "$i" != "$NOW" ]
    then
    LINKDEST="$LINKDEST --link-dest $DEST/$i/"
    fi
done

mkdir "$DEST/$NOW"
rsync / $DEST/$NOW/ -a --delete --numeric-ids --exclude "proc/*" --exclude "sys/*" --exclude "dev/*" --exclude "home/sysmso/.gvfs" --exclude "media/*" --exclude "/mnt/" $LINKDEST $RSYNC_OPTIONS
touch "$DEST/$NOW"
 
# Nettoyage des anciens fichiers
echo "Cleanup ..."
find "$DEST" -maxdepth 1 -mindepth 1 -type d -mtime +$DAYS -print -exec rm -rf {} \;

