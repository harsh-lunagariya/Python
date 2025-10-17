import logging
import employee

"""
DEBUG: Detailed information, typically of interest only when diagnosing problems.

INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
"""

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('Modules/tset.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)


stream_handler = logging.StreamHandler()    #create streame handler

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        logger.error("Try to divide by zero")   #if we use logger.exception it also log the traceback
    else:
        return result 

num1=20
num2=0

# logging.basicConfig(filename='Modules/test.log', level = logging.DEBUG,
#                     format='%(asctime)s:%(levelname)s:%(message)s')


result = add(num1,num2)
logging.debug(f'num1 + num2 = {result}')
result = sub(num1,num2)
logging.debug(f'num1 - num2 = {result}')
result = mul(num1,num2)
logging.debug(f'num1 * num2 = {result}')
result = div(num1,num2) 
logging.debug(f'num1 / num2 = {result}')