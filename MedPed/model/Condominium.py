class Condominium:
    def __init__(self, idCondominium, nameCondominium, city):
        self.__id = idCondominium
        self.__name = nameCondominium
        self.__city = city

    def get_id(self):
        return self.__id

    def set_id(self, idCondominium):
        self.__id = idCondominium

    def get_name(self):
        return self.__name

    def set_name(self, nameCondominium):
        self.__name = nameCondominium

    def get_city(self):
        return self.__city

    def set_city(self, city):
        self.__city = city
        