# System_UI verifies the login information of each customer class


class System_UI:
    def __init__(self, status: bool):
        self.status = status

    # Verfies customer information based on whats stored in database
    def verifyLogin(self):
        # You can implement the code to verify customer login information here
        print("Login successful")
