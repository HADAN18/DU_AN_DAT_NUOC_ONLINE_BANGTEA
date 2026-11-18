import unittest
from customers.auth import Auth


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth()

    def test_register_success(self):
        result = self.auth.register("khachhang01", "123456")
        self.assertTrue(result)

    def test_register_duplicate(self):
        self.auth.register("khachhang01", "123456")
        result = self.auth.register("khachhang01", "abcdef")
        self.assertFalse(result)

    def test_login_success(self):
        self.auth.register("khachhang01", "123456")
        result = self.auth.login("khachhang01", "123456")
        self.assertTrue(result)

    def test_login_wrong_password(self):
        self.auth.register("khachhang01", "123456")
        result = self.auth.login("khachhang01", "1234567")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()

import unittest
from customers.auth import Auth


class TestAuth(unittest.TestCase):

    def setUp(self):
        self.auth = Auth()

    def test_register_success(self):
        result = self.auth.register("khachhang01", "123456")
        self.assertTrue(result)

    def test_register_duplicate(self):
        self.auth.register("khachhang01", "123456")
        result = self.auth.register("khachhang01", "abcdef")
        self.assertFalse(result)

    def test_login_success(self):
        self.auth.register("khachhang01", "123456")
        result = self.auth.login("khachhang01", "123456")
        self.assertTrue(result)

    def test_login_wrong_password(self):
        self.auth.register("khachhang01", "123456")
        result = self.auth.login("khachhang01", "1234567")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()