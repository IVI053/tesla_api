from getpass import getpass

class Interactive():
    def get_account(self):
        return input('Account: ')

    def get_password(self):
        return getpass('Password: ')
