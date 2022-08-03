import logging
from i_need_this_module.and_i_love_it import FakeADC
from logging.handlers import TimedRotatingFileHandler
from time import sleep


#########
# Setup #
#########

logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(name)s]', datefmt='%H:%M:%S')
handler_file = TimedRotatingFileHandler(filename='./logs/8_advanced_time_managed.log', when='s', interval=3, backupCount=3) #'s', 'm', 'h', 'd', etc
#handler_file = logging.FileHandler('./logs/advanced_fixed_alternative_app.log', mode='a')
handler_file.setLevel(logging.DEBUG)
handler_file.setFormatter(formatter)

logger.addHandler(handler_file)


################
# Main Program #
################

for i in range(100):
    logger.info('Beginning ADC reading')
    value = FakeADC.averageReading()
    sleep(0.1)