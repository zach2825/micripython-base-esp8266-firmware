#!/usr/bin/env bash

prompt="Which firmware would you like to flash: "
options=( $(find ./firmwares/ -maxdepth 1 -type f -print0 | xargs -0) )

PS3="$prompt "
select opt in "${options[@]}" "Quit" ; do
    if (( REPLY == 1 + ${#options[@]} )) ; then
        exit

    elif (( REPLY > 0 && REPLY <= ${#options[@]} )) ; then
        echo  "You picked $opt which is file $REPLY"
        break

    else
        echo "Invalid option. Try another one."
    fi
done

#read -p "Enter Baud rate to flash : " name
#name=${name:-460800}
baud_rate=460800

## Do flash
echo "erasing flash" &&
esptool.py --port /dev/ttyUSB0 erase_flash && sleep 1 &&
echo "writing flash" &&
esptool.py --port /dev/ttyUSB0 --baud "${baud_rate}" write_flash -fm=dio -fs=32m --flash_size=detect 0x00000 "${opt}" &&

# flashing completed wait for chip reboot and then copy files
echo "done. waiting 13 seconds " && sleep 13 &&

echo "Copying libs" &&
./copy-libs.sh &&
sleep .5
echo "copying all the things" &&
./copy-all.sh
