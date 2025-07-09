#!/bin/sh
# Name: ShowImage
# Author: tiny
# _DontUseFBInk

killall screenControl &> /dev/null
killall screenControlHF &> /dev/null


which curl
which wget

# sleep forever:
sleep_count=0
while true; do
    # eips -i > /mnt/us/documents/eipsout.txt
    # eips -g /mnt/us/documents/image.png -w gc16
    echo 'sleeping... ' $sleep_count
    chmod 777 /mnt/us/documents/kindlr
    /mnt/us/documents/kindlr
    sleep_count=$((sleep_count + 1))
    sleep 30
done
exit 0