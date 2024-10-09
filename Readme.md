# drumPi

Fun little project for making a raspberry pi drum module, no more need for draggin out your expensive laptop to a show just to put at the drummers feet under the high hat! now you load this up, modify the samples keeping the naming convention the same and you have a stupid simple sound module that is triggered via midi messages. 

## Pre-requisites
first need to install pygame
pip install pygame
second need to install etc mixer dependencies
sudo apt-get install libsdl2-mixer-2.0-0
python3 -m pip install mido
python3 -m pip install mido[ports-rtmidi]

run app with python drumpi.py

can also add to rc.local for startup headless.
paste the below line before the exit
in /etc/rc.local
sudo -H -u pi /usr/bin/python3 /home/pi/drumPi/drumpi.py &


view logs via  tail -f /var/log/syslog



