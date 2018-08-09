# Basic connect to wifi and mqtt

the scripts were created to be ran on linux(Ubuntu) computers

## Required packages
  * picocom  `sudo apt install picocom`
  * python3 `sudo apt install python3 python3-pip`
  * ampy.py `sudo pip install nodemcu-uploader`

## Getting started
  * `cp settings.example.py settings.py`
  * populate your settings
  * connect esp8266, if our esp does not connect to /dev/ttyUSB0 you'll have to findout what it connects to and update the scripts to reflect that.

After you have created the settings.py file and puplated your wifi ssid and password and mqtts host username and password you should be good to connect the esp to your computer and run ./flash-all.sh
 
## Things to note
  * after running flash-all you don't need to re-run the full flash all command you can just run ./copy-all.sh at the end of that script it will auto open picocom with the ./connect.sh command
  * if you need to kill the boot.py file on your esp just run `./connect.sh` and after your connected in picocom press ctrl+c
    * that should drop you to the repl terminal where you can run `import boot.py; kill()` I created that function to remove boot.py and settings.py
    * then you can press ctrl+a ctrl+x to exit picocom and then run ./copy-all.sh

It took me a while to find all the parts to create these scripts and files. I hope it helpe someone out there. Please feel free to contribute if possible. Just keep the code as simple as possible.
  
## Sources
  * I downloaded the framework to this project to make it easy to download and flash new esp chips.
    * http://micropython.org/download#esp8266
    * in my scripts and for my experience I used 1.9.4 because it's the one that worked with my esps but feel free to change it.
  * http://docs.micropython.org/en/v1.9.1/esp8266/library/index.html#python-standard-libraries-and-micro-libraries
  * umqtt/simple.py
    * https://github.com/micropython/micropython-lib/tree/master/umqtt.simple

import os; os.remove("boot.py")

