'''
PhoneRepository abstract class
'''

from abc import ABCMeta, abstractmethod


class PhoneRepository:
    '''
    PhoneRepository
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_phone(self, phone_name, phone_price):
        """Add new phone"""

    @abstractmethod
    def get_phone(self, phone_id):
        """Get phone by id"""

    @abstractmethod
    def update_phone(self,
                     updated_phone_id,
                     updated_phone_name,
                     updated_phone_price):
        """Edit phone with new data"""

    @abstractmethod
    def delete_phone(self, phone_id):
        """Delete phone by id"""


