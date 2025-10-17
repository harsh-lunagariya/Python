import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('Modules/employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# for basic use
# logging.basicConfig(filename='Modules/employee.log',level=logging.INFO,
#                     format='')

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname,self.email))
    
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
emp1 = Employee('John','Smith')
emp2 = Employee('Cherry','Sheferd')
emp3 = Employee('Jane','Doe')
