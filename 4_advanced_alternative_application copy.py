import logging
from i_need_this_module.and_i_love_it import FakeADC


#########
# Setup #
#########

logger = logging.getLogger() 
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s [%(name)s]', datefmt='%H:%M:%S')
handler_file = logging.FileHandler('./logs/4_advanced_alternative_app.log', mode='a')
handler_file.setLevel(logging.DEBUG)
handler_file.setFormatter(formatter)

logger.addHandler(handler_file)

# logging.basicConfig(filename='./logs/basic_alternative_app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')


################
# Main Program #
################

logger.info('Beginning ADC reading')
value = FakeADC.averageReading()