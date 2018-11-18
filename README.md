# pyfi-player

Dependencies:
* VLC binaries (version 3.0.3 was tested)
* For audio, just use ALSA. It's better if pulseaudio isn't installed - VLC defaults to this and causes jutter on raspi
* python3-spidev
* https://github.com/lthiery/SPI-Py.git

Config:
* Install vlc
* Set up venv
* Install modules from requirements.txt
* Install python3-spidev
* Install SPI-Py ('python setup.py install' after cloning repo in venv)

Dev:
* yapf used for formatting with default settings

Reference:
* https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/
* https://github.com/mxgxw/MFRC522-python.git (note that this is python2, need to update the print statements to python3)

Notes:
* Audio jutter over hdmi, no issue over headphone output
* Tested on raspberry pi 3 B