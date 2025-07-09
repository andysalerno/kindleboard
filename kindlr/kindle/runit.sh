#!/bin/sh
# Name: ShowImage
# Author: tiny
# _DontUseFBInk

killall screenControl &> /dev/null
killall screenControlHF &> /dev/null


which curl
which wget

# chmod 777 /mnt/us/documents/kindlr

rm /mnt/us/documents/image.png

# sleep forever:
sleep_count=0
while true; do
    # eips -i > /mnt/us/documents/eipsout.txt
    wget http://192.168.1.179:8000/image -O /mnt/us/documents/image.png
    # eips -g /mnt/us/documents/image.png -w gc16
    # echo 'sleeping... ' $sleep_count
    # /mnt/us/documents/kindlr
    sleep_count=$((sleep_count + 1))
    sleep 30
done
exit 0