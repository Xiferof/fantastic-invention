from src.const import VERSION_STR
import PySimpleGUI as sg
import src.users as users
import os
import copy
def add_user_to_list(user:users.User):
    filepath = os.getcwd() + '\\data\\user.pickle'
    user_list = users.load_user_list(filepath)
    if users.check_if_user_exists(user.name, user_list):
        return False
    else:
        user_list.append(user)
        users.write_users_to_file(filepath,user_list)
        return True
def auth_user_from_data_base(username:str, passkey:str):
    filepath = os.getcwd() + '\\data\\user.pickle'
    user_list = users.load_user_list(filepath)
    if users.check_if_user_exists(username, user_list):
        if (users.authenticate_user(username, passkey, user_list)):
            return True
        else:
            return False
    else:
        return False
class GUI:
    def __init__(self):


        self.welcome_screen = [[sg.Text("Welcome to Fantastic-Invention")],
                                [sg.Text("Version" + VERSION_STR)],
                                [sg.Button('Login', key='_GOTO_LOGIN_'), sg.Button('SignUp', key='_GOTO_SIGNUP_')]
        ]

        self.login_layout = [[sg.Text("Login Page")],
                            [sg.Text(' '*80, key = '_LOGIN_INFO_')], 
                            [sg.Text("Username"), sg.InputText(key='_USERNAME_')],
                            [sg.Text("Password"), sg.InputText(key='_PASSKEY_', password_char='*')],
                            [sg.Button("Login", key='_LOGIN_')]]

        self.signup_layout = [[sg.Text("Signup Page")],
                              [sg.Text(' '*80, key='_SIGNUP_INFO_' ,text_color='red')],
                              [sg.Text("Username"), sg.InputText(key='_USERNAME_')],
                              [sg.Text("Password"), sg.InputText(key='_PASSKEY_1_', password_char='*')],
                              [sg.Text("Confirm Password"), sg.InputText(key='_PASSKEY_2_', password_char='*')],
                              [sg.Button("Create User", key = '_CREATE_USER_')]]
        self.post_signup_layout = [[sg.Text("User Created successfully, Goto login and start testing")]]

        self.layout = [ [sg.Text("Login Here")],
        [sg.Text("Create new User")],
        [sg.Text("Login Existing User")],
        [sg.Button("Login", key = '_LOGIN_KEY_')]]
    def start_gui(self):
        self.window = sg.Window('Main Window', copy.deepcopy(self.welcome_screen))
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            if(event == '_GOTO_LOGIN_'):
                self.login()
            if(event == '_GOTO_SIGNUP_'):
                self.signup()
            if(event == '_LOGIN_'):
                username = values['_USERNAME_']
                passkey= values['_PASSKEY_']
                if auth_user_from_data_base(username, passkey):
                    self.quiz(username)
                else:
                    self.window['_LOGIN_INFO_'].update("Password mismatch! OR User does not exist")
            if event == '_CREATE_USER_':
                if(values['_PASSKEY_1_'] != values['_PASSKEY_2_']):
                    self.window['_SIGNUP_INFO_'].update("Password mismatch!")
                else:
                    if add_user_to_list(users.User(values['_USERNAME_'], values['_PASSKEY_1_'])):
                        self.welcome()
                    else:
                       self.window['_SIGNUP_INFO_'].update("User Already Exisits!") 
                    
    def welcome(self):
        self.window.close()
        self.window = sg.Window('Main Window', copy.deepcopy(self.welcome_screen))
    def login(self):
        self.window.close()
        self.window = sg.Window('Login Window', copy.deepcopy(self.login_layout))
    def signup(self):
        self.window.close()
        self.window = sg.Window('Signup Window', copy.deepcopy(self.signup_layout))
        

