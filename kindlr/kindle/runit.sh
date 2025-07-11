#!/bin/sh
# Name: ShowImage
# Author: tiny
# DontUseFBInk

URL="http://192.168.1.214:8000/image"
IMAGE_PATH="/mnt/us/documents/image.png"
SLEEP_SEC=30

prepare() { 
    # stop frameworks
    killall screenControl &> /dev/null
    killall screenControlHF &> /dev/null

    stop framework
    stop lab126_gui
    initctl stop webreader >/dev/null 2>&1

    # Reduce power consumption and disable screensaver
    echo powersave >/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
    lipc-set-prop com.lab126.powerd preventScreenSaver 1

    # remove any old images from previous runs
    rm $IMAGE_PATH
}

download_image() {
    wget "$URL" -O "$IMAGE_PATH"
}

refresh_display() {
    eips -g "$IMAGE_PATH" -w gc16
}

# chmod 777 /mnt/us/documents/kindlr
# eips -i > /mnt/us/documents/eipsout.txt

deep_sleep() {
    duration=$1
    sleep $duration
}

prepare

sleep_count=0
while true; do
    # wget "$URL" -O "$IMAGE_PATH"
    download_image
    refresh_display
    # eips -g "$IMAGE_PATH" -w gc16
    # echo 'sleeping... ' $sleep_count
    # /mnt/us/documents/kindlr
    sleep_count=$((sleep_count + 1))
    deep_sleep $SLEEP_SEC
done


exit 0