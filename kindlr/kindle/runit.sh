#!/bin/sh
# Name: ShowImage
# Author: tiny
# DontUseFBInk

killall screenControl &> /dev/null
killall screenControlHF &> /dev/null


which curl
which wget

# chmod 777 /mnt/us/documents/kindlr
# eips -i > /mnt/us/documents/eipsout.txt

rm /mnt/us/documents/image.png

URL="http://192.168.1.214:8000/image"
IMAGE_PATH="/mnt/us/documents/image.png"
SLEEP_SEC=30

# sleep forever:
sleep_count=0
while true; do
    wget "$URL" -O "$IMAGE_PATH"
    eips -g "$IMAGE_PATH" -w gc16
    # echo 'sleeping... ' $sleep_count
    # /mnt/us/documents/kindlr
    sleep_count=$((sleep_count + 1))
    sleep $SLEEP_SEC
done
exit 0