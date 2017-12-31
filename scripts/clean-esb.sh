#!/bin/bash
#DIRNAME=`date | awk '{print $2$6}' `
DEST=/srv/jboss-eap-6.2/standalone/log/ugo-wallet
#if [ ! -e "$DEST/$DIRNAME" ]; then
#mkdir $DEST/$DIRNAME;
#fi
cd $DEST
find . -type f -mtime +90 -exec rm -f {} \;
find . -maxdepth 1 -type f -name "*.gz" -exec mv {} Archived_logs/ \;
find . -maxdepth 1 -type f -name "*.bz" -exec mv {} Archived_logs/ \;
for k in `find . -maxdepth 1 -type f -mtime +3 `;
do
tar -czf $DEST/Archived_logs/$k.tar.gz $k;
rm -f $k;
done

 
