import unittest
import src.users as users
class TestUserMethods(unittest.TestCase):

    def test_login_happy_flow(self):
        user_list = []

        user_list.append(users.User('Test','Test2'))
        retval = users.check_if_user_exists('Test', user_list)
        self.assertTrue(retval)
    def test_login_invalid_user(self):
        user_list = []
        user_list.append(users.User('Test','Test2'))
        retval = users.check_if_user_exists('TestF', user_list)
        self.assertFalse(retval)
    def test_login_happy_flow_pass(self):
        user_list = []
        user_list.append(users.User('Test','Correct'))
        retval = users.authenticate_user('Test','Correct', user_list)
        self.assertTrue(retval)    
    def test_login_incorrect_passkey(self):
        user_list = []
        user_list.append(users.User('Test','Correct'))
        retval = users.authenticate_user('Test','Incorrect', user_list)
        self.assertFalse(retval)
    def test_login_auth_for_no_user_raises(self):
        with self.assertRaises(KeyError):
            users.authenticate_user('Test','Incorrect', [])

if __name__ == "__main__":
    unittest.main()