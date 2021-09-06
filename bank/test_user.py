import unittest

from user import User
from user import UserApproved
from user import UserCreated


class TestUser(unittest.TestCase):

    def test_user_has_id(self) -> None:
        user1 = User.create(id=17, first_name="Kinga", last_name="Teresa")
        user2 = User.create(id=15, first_name="Piotr", last_name="Kopalko")
        user3 = User.create(id=180, first_name="Ada", last_name="Banaszak")
        self.assertEqual(17, user1.id())
        self.assertEqual(15, user2.id())
        self.assertEqual(180, user3.id())

    def test_user_has_a_name(self) -> None:
        user = User.create(id=15, first_name="Kinga", last_name="Teresa")
        User.create(85, "Piotr", "Kopalko")
        self.assertEqual(user.name(), "Kinga Teresa")

    def test_user_needs_approval_after_creation(self) -> None:
        user = User.create(id=17, first_name="Kinga", last_name="Teresa")
        self.assertFalse(user.is_approved())
        user.approve()
        self.assertTrue(user.is_approved())

    def test_user_has_creation_history(self) -> None:
        user = User.create(id=10, first_name="Kinga", last_name="Teresa")
        self.assertEqual(user.history(), [
            UserCreated(id=10, first_name="Kinga", last_name="Teresa")])

    def test_user_has_all_own_events_history(self) -> None:
        user = User.create(id=10, first_name="Kinga", last_name="Teresa")
        user.approve()
        self.assertEqual(user.history(), [
            UserCreated(id=10, first_name="Kinga", last_name="Teresa"), UserApproved(id=10)])
