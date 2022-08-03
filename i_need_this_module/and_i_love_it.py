
from random import randrange
import logging

logger = logging.getLogger(__name__)


class FakeADC():

    def averageReading():
        captured_values = []
        for i in range(5):
            captured_values.append(FakeADC._readFakeADC())
        avg_reading = sum(captured_values)/len(captured_values)
        logger.info('Average ADC value: {}'.format(avg_reading))
        return avg_reading

    def _readFakeADC():
        reading = randrange(33)/10
        logger.debug('Raw ADC value: {}'.format(reading))
        return reading
