import logging
from .and_i_love_it import FakeADC
logging.basicConfig(format='%(msecs)s%(threadName)s%(msg)s%(filename)s', level=logging.DEBUG, datefmt='%H:%M:%S')

FakeADC.averageReading()