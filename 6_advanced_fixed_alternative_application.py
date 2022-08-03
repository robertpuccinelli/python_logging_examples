import logging
from i_need_this_module.and_i_love_it import FakeADC
# This module generates the root logger
import i_need_this_module.and_it_destroys_logging 


#########
# Setup #
#########

# Reclaim access to root logger and add new handlers to it
logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(name)s]', datefmt='%H:%M:%S')
handler_file = logging.FileHandler('./logs/6_advanced_fixed_alternative_app.log', mode='a')
handler_file.setLevel(logging.DEBUG)
handler_file.setFormatter(formatter)

logger.addHandler(handler_file)

# basicConfig only works if root logger hasn't been generated
# logging.basicConfig(filename='./logs/basic_alternative_app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')


################
# Main Program #
################

logger.info('Beginning ADC reading')
value = FakeADC.averageReading()