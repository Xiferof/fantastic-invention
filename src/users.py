"""This module implements handling users information
"""
import pickle
import hashlib
SECRET_SALT = b'HI SATNAM!'
def load_user_list(filepath:str):
    try:
        with open(filepath, 'rb') as f:
            users = pickle.load(f)
        return users
    except FileNotFoundError:
        return []


def write_users_to_file(filepath:str, users):
    with open(filepath, 'wb+') as f:
        pickle.dump(users, f)


def check_if_user_exists(username, user_list):
    for x in user_list:
        if(x.name == username):
            return True
    return False

def authenticate_user(username, passkey, user_list):
    for x in user_list:
        if(x.name == username):
            if(x.authenticate_user(passkey)):
                return True
            else:
                return False
    raise KeyError("User not found")

class User:
    """Implements a user handling user data and login flows
    """
    def __init__(self, name, passphrase:str):
        self.name = name
        hasher = hashlib.sha256()
        hasher.update(passphrase.encode('ascii'))
        hasher.update(SECRET_SALT)
        self.hashed_pass =  hasher.digest()
        self._test_index = 0
        
    def authenticate_user(self, passkey:str):
        hasher = hashlib.sha256()
        hasher.update(passkey.encode('ascii'))
        hasher.update(SECRET_SALT)
        if (self.hashed_pass == hasher.digest()):
            return True
        else:
            return False
    def get_user_bg_colour(self):
        pass


