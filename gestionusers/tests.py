from django.test.testcases import TestCase

from gestionusers.services import UserService


class UserServiceTestCase(TestCase):

    def setUp(self):
        self.service = UserService()

    def test_get_by_type_user(self):
        type_user = 'school'
        schools = self.service.filter_by({'type_user': type_user})
        print(schools)
        self.assertIsInstance(list(schools), list)
