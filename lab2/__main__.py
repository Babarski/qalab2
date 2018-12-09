"""
#2. Mobile phone in market
#6. Show all entities with same names
#4. Для заданного идентификатора функции заменить один символ на другой
#4. MongoDB + Morphia (http://mongodb.github.io/morphia/)
"""

import os
import coverage
from lab2.ApplicationService.ApplicationServiceImpl import ApplicationServiceImpl
from lab2.PhoneRepository.PhoneRepositoryImpl import PhoneRepositoryImpl


if __name__ == "__main__":
    COV = coverage.Coverage()
    COV.start()
    APPLICATION_SERVICE = ApplicationServiceImpl()
    PHONE_REPOSITORY = PhoneRepositoryImpl()
    # application_service.set_phone(name="samsung", price="100")
    # application_service.set_phone(name="samsung", price="1300")
    # application_service.set_phone(name="iphone", price="100")
    # phone_repository.create_phone(phone_name="xiaomi", phone_price="100")
    print("Enviroment - "+os.environ.get("MODE"))
    RESULT = APPLICATION_SERVICE.get_phones_with_same_names()

    for phone in RESULT:
        print(phone)

    COV.stop()
    COV.save()

    COV.html_report()
