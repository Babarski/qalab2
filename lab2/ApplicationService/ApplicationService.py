"""
Application service abstract method
"""

from abc import ABCMeta, abstractmethod


class ApplicationService:
    '''
    Application Service
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_phones_with_same_names(self):
        '''Return list of objects "Phone" with same name'''

    @abstractmethod
    def change_symbol(self, id, symbol, symbol_to_change):
        '''Return list of objects "Phone" with same name'''