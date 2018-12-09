"""
PhoneRepository realisation
"""

import os
import yaml
from pymongo import MongoClient
from lab2.PhoneRepository import PhoneRepository
from .Phone import Phone


class PhoneRepositoryImpl(PhoneRepository.PhoneRepository):
    '''
    Implementation of PhoneRepository
    '''
    @staticmethod
    def connect_to_db():
        '''
        Create connection to MongoDB database
        :return: None
        '''
        configfile = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        with open(configfile+"/configs/configs.yml", "r") as ymlfile:
            cfg = yaml.load(ymlfile)
            mode = "mongodb_" + os.environ.get("MODE")
            client = MongoClient(cfg[mode]["host"])
            database = client[cfg[mode]["database"]]
            myphone = database[cfg[mode]["table"]]

            return myphone

    def create_phone(self, phone_name, phone_price):
        """Add new phone"""

        myphone = self.connect_to_db()
        phone = Phone(phone_name, phone_price)
        try:
            myphone.insert_one({"name": phone.get_name(), "price": phone.get_price()})
            return True
        except:
            return False

    def get_phones(self):
        """Get phone by name"""

        myphone = self.connect_to_db()
        phones = myphone.find({})
        return phones

    def update_phone(self, updated_phone_id, updated_phone_name, updated_phone_price):
        """Edit phone with new data"""
        myphone = self.connect_to_db()
        phone = myphone.find_one({"_id": updated_phone_id})
        #myphone.insert_one({"name": updated_phone_name, "price": updated_phone_name})
        phone['name'] = updated_phone_name
        phone['price'] = updated_phone_price
        myphone.save(phone)

    def delete_phone(self, id):
        """Delete phone by id"""

        myphone = self.connect_to_db()
        myphone.delete_one({"id": id})

    def get_phone(self, phone_id):
        myphone = self.connect_to_db()
        phone = myphone.find_one({"_id": phone_id})
        return phone

    def get_phone_by_name(self, phone_name):
        myphone = self.connect_to_db()
        phone = myphone.find_one({"name": phone_name})
        return phone
