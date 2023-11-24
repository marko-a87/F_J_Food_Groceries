# System_UI verifies the login information of each customer class


class System_UI:
    def __init__(self, status):
        self.status = status

    # Verfies customer information based on whats stored in datebase
    def verifyLogin(self):
        # You can implement the code to verify customer login information here
        print("Login successful")


def main():
    system_ui = System_UI("true")
    system_ui.verifyLogin()
    print("Running")


if __name__ == "__main__":
    main()
