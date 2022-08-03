import logging
from i_need_this_module.and_i_love_it import FakeADC
# This module generates the root logger
import i_need_this_module.and_it_destroys_logging 


#########
# Setup #
#########

 # basicConfig only works if root logger hasn't been generated
logging.basicConfig(filename='./logs/5_basic_broken_app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')


################
# Main Program #
################

logging.info('Beginning ADC reading')
value = FakeADC.averageReading()