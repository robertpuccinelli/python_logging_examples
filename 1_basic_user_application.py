import logging
from i_need_this_module.and_i_love_it import FakeADC


#########
# Setup #
#########

logging.basicConfig(filename='./logs/1_basic_app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s [%(name)s]', level=logging.INFO, datefmt='%H:%M:%S')


################
# Main Program #
################

logging.info('Beginning ADC reading')
value = FakeADC.averageReading()
