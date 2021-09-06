import unittest

from user import User


class TestUser(unittest.TestCase):

    def test_user_has_a_name(self) -> None:
        user = User.create("Kinga", "Teresa")
        self.assertEqual(user.name(), "Kinga Teresa")

    def test_user_needs_approval_after_creation(self) -> None:
        user = User.create("Kinga", "Teresa")
        self.assertFalse(user.is_approved())
        user.approve()
        self.assertTrue(user.is_approved())

    def test_user_has_empty_history(self) -> None:
        user = User.create("Kinga", "Teresa")
        self.assertEqual(user.history(), [])
