from django.core.exceptions import ValidationError
from django.test import TestCase

from plygramm.accounts.models import Account


class AccountCreateTests(TestCase):
    def test_teacher_creation(self):
        Account.objects.create(email="random_teacher@world.io", role="Teacher")

    def test_student_creation(self):
        Account.objects.create(email="random_student@world.io", role="Student")

    def test_account_without_password_is_created_with_unusable_one(self):
        account = Account.objects.create(email="random_user@world.io", role="Admin")
        self.assertFalse(account.has_usable_password())

    def test_account_with_capitalized_email_cannot_be_created(self):
        Account.objects.create(email="random_user@world.io", role="Admin")

        with self.assertRaises(ValidationError):
            Account.objects.create(email="RANDOM_user@world.io", role="Admin")

        self.assertEqual(1, Account.objects.count())

    def test_nickname_contains_spaces(self):
        account = Account.objects.create(email="random@world.io", role="Admin", nickname="name")
        self.assertNotContains(account, " ")
