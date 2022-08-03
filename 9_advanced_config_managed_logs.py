import logging
from i_need_this_module.and_i_love_it import FakeADC
from logging.config import fileConfig
from time import sleep


#########
# Setup #
#########

fileConfig(fname="logger.config",disable_existing_loggers=False)
logger = logging.root

################
# Main Program #
################

for i in range(10):
    logger.info('Beginning ADC reading')
    value = FakeADC.averageReading()
    sleep(0.2)