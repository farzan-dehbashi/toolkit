class MailService:
    def __init__(self, name) -> None:
        self.__name = name
    
    def get_name(self):
        return self.__calculate_name('Mail server name is: ')

    def __calculate_name(self, var):
        return var + self.__name