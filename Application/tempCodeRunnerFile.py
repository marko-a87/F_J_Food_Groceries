import os


os.chdir("C:/Users/Shamar/Documents/JandJ_Food_Groceries")
from ...JandJ_Food_Groceries.Authentication.Customer import Customer
from ...JandJ_Food_Groceries.Authentication.System_UI import System_UI


class App:
    def __init__(self):
        self.customer = Customer()
        self.system_ui = System_UI()
