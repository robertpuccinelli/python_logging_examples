import logging
from i_need_this_module.but_i_hate_it import FakeAnnoyingADC


#########
# Setup #
#########

logging.basicConfig(filename='./logs/2_basic_annoying_app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s [%(name)s]', level=logging.DEBUG, datefmt='%H:%M:%S')


################
# Main Program #
################

logging.info('Beginning ADC reading')
value = FakeAnnoyingADC.averageReading()
