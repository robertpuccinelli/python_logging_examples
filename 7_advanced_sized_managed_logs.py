import logging
from i_need_this_module.and_i_love_it import FakeADC
from logging.handlers import RotatingFileHandler
from time import sleep


#########
# Setup #
#########

# Reclaim access to root logger and add new handlers to it
logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(name)s]', datefmt='%H:%M:%S')
handler_file = RotatingFileHandler(filename='./logs/7_advanced_sized_managed.log',backupCount=3,maxBytes=1000)
#handler_file = logging.FileHandler('./logs/advanced_fixed_alternative_app.log', mode='a')
handler_file.setLevel(logging.DEBUG)
handler_file.setFormatter(formatter)

logger.addHandler(handler_file)


################
# Main Program #
################

for i in range(10):
    logger.info('Beginning ADC reading')
    value = FakeADC.averageReading()
    sleep(1)