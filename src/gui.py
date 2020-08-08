import PySimpleGUI as sg

class GUI:
    def __init__(self):

        self.login_layout = [[sg.Text("Login Page")], sg.Input]


        self.layout = [  [sg.Text("Login Here")],
        [sg.Text("Create new User")],
        [sg.Text("Login Existing User")],
        [sg.Button("Login", key = '_LOGIN_KEY_')]]
    def start_gui(self):
        self.window = sg.Window('Window Title', self.layout)
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel':
                break
            print(event)
            if(event == '_LOGIN_KEY_'):
                print("something happened")
                self.login()
    def login(self):
        self.layout = [[sg.Text("This is the quiz screen")]]
        self.window.close()
        self.window = sg.Window('Play screen', self.layout)

