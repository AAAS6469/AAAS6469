#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic/album')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in3f
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
import random

try:
    logging.info("epd7in3f Demo")

    epd = epd7in3f.EPD()   
    logging.info("init and Clear")
    epd.init()
    epd.Clear()  
    import weather
    time.sleep(1800) # 30min
# read jpg file 10min 6sec
    for  x in range(5):
        epd.init()
        epd.Clear() 
        logging.info("s-#.read jpg 800*480 file")
        picname='s-'+str(random.randint(0,350))+'.jpg'
        Himage = Image.open(os.path.join(picdir, picname))
        epd.display(epd.getbuffer(Himage))
        time.sleep(600)
        
    import weather  
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in3f.epdconfig.module_exit(cleanup=True)
    exit()