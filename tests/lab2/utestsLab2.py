import mock
import unittest
from lab2.ApplicationService.ApplicationServiceImpl import ApplicationServiceImpl
from lab2.PhoneRepository.PhoneRepositoryImpl import PhoneRepositoryImpl
from unittest.mock import MagicMock, patch
import coverage


class TestApplicationServiceImpl(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.cov = coverage.Coverage()
        self.cov.start()

    @classmethod
    def tearDownClass(self):
        self.cov.stop()
        self.cov.save()
        self.cov.html_report()

    @mock.patch.object(PhoneRepositoryImpl, 'get_phones')
    def test_get_all_phones(self, mock_get_phones):

        phone_repository = PhoneRepositoryImpl()
        phone_repository.get_phones.return_value=[
            {'price': '2000', 'name': 'iphone'},
            {'price': '100', 'name': 'samsung'},
            {'price': '1300', 'name': 'samsung'},
            {'price': '100', 'name': 'iphone'},
            {'price': '100', 'name': 'iphone'}]

        application_service = ApplicationServiceImpl()
        self.assertEqual(application_service.get_phones_with_same_names(), [
            {'price': '2000', 'name': 'iphone'},
            {'price': '100', 'name': 'samsung'},
            {'price': '1300', 'name': 'samsung'},
            {'price': '100', 'name': 'iphone'},
            {'price': '100', 'name': 'iphone'}])

    @mock.patch.object(PhoneRepositoryImpl, 'get_phones')
    def test_get_phones_with_same_name(self, mock_get_phones):
        phone_repository = PhoneRepositoryImpl()
        phone_repository.get_phones.return_value = [
            {'price': '2000', 'name': 'iphone'},
            {'price': '100', 'name': 'samsung'},
            {'price': '1300', 'name': 'samsung'},
            {'price': '100', 'name': 'iphone'},
            {'price': '100', 'name': 'iphone'},
            {'price': '1000', 'name': 'meizu'},
            {'price': '100', 'name': 'nokia'}]

        application_service = ApplicationServiceImpl()
        self.assertEqual(application_service.get_phones_with_same_names(), [
            {'price': '2000', 'name': 'iphone'},
            {'price': '100', 'name': 'samsung'},
            {'price': '1300', 'name': 'samsung'},
            {'price': '100', 'name': 'iphone'},
            {'price': '100', 'name': 'iphone'}])

    @mock.patch.object(PhoneRepositoryImpl, 'get_phones')
    def test_empty_array(self, mock_get_phones):
        phone_repository = PhoneRepositoryImpl()
        phone_repository.get_phones.return_value = []

        application_service = ApplicationServiceImpl()
        self.assertEqual(application_service.get_phones_with_same_names(), [])
        self.assertTrue(phone_repository.get_phones.called)

