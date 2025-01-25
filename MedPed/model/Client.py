class Client:
    def __init__(self, nameClient, lastNameClient, email, idClient, phone, statusClient, dateOfBirth):
        self.__id = idClient
        self.__name = nameClient
        self.__lastName = lastNameClient
        self.__email = email
        self.__phone = phone
        self.__status = statusClient
        self.__dateOfBirth = dateOfBirth
    
    def get_id(self):
        return self.__id
    
    def set_name(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, nameClient):
        self.__name = nameClient

    def get_last_name(self):
        return self.__lastName

    def set_last_name(self, lastNameClient):
        self.__lastName = lastNameClient

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_status(self):
        return self.__status

    def set_status(self, statusClient):
        self.__status = statusClient

    def get_date_of_birth(self):
        return self.__dateOfBirth

    def set_date_of_birth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth
    

        