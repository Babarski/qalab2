"""
ApplicationService realisation
"""

import copy
from lab2.ApplicationService import ApplicationService
from lab2.PhoneRepository.PhoneRepositoryImpl import PhoneRepositoryImpl


class ApplicationServiceImpl(ApplicationService.ApplicationService):
    '''
    Application service
    '''
    def get_phones_with_same_names(self):
        phone_repository = PhoneRepositoryImpl()
        phones = phone_repository.get_phones()
        phones_copy = copy.copy(phones)
        names = {}
        for phone in phones:
            try:
                names[phone['name']] = names[phone['name']] + 1
            except KeyError:
                names[phone['name']] = 1

        phones_with_same_names = []

        for phone in phones_copy:
            if names[phone['name']] > 1:
                phones_with_same_names.append(phone)

        return phones_with_same_names

    def change_symbol(self, id, symbol, symbol_to_change):
        phone_repository = PhoneRepositoryImpl()
        phone = phone_repository.get_phone(phone_id=id)
        name_as_list = list(phone['name'])

        for i in range(len(name_as_list)):
            if name_as_list[i] == symbol_to_change:
                name_as_list[i] = symbol

        final_name = ''.join(name_as_list)
        phone_repository.update_phone(id, updated_phone_name=final_name, updated_phone_price=phone['price'])



