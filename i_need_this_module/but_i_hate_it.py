
from random import randrange
import logging

logger = logging.getLogger(__name__)


class FakeAnnoyingADC():    
    
    def averageReading():
        captured_values = []
        for i in range(5):
            captured_values.append(FakeAnnoyingADC._readFakeADC())
        avg_reading = sum(captured_values)/len(captured_values)
        logger.info('ADC readings were averaged.')
        return avg_reading


    def _readFakeADC():
        reading = randrange(33)/10
        logger.debug('ADC value recorded.')
        if reading > 0:
            logger.warning('Raw ADC value is > 0, which is out of bounds!!!')
        return reading