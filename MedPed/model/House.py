from Condominium import Condominium

class House(Condominium):
    def __init__(self, idCondominium, nameCondominium, city, idHouse, typeHouse):
        super().__init__(idCondominium, nameCondominium, city)
        self.__idHouse = idHouse
        self.__typeHouse = typeHouse

    def get_id_house(self):
        return self.__idHouse

    def set_id_house(self, idHouse):
        self.__idHouse = idHouse

    def get_type_house(self):
        return self.__typeHouse

    def set_type_house(self, typeHouse):
        self.__typeHouse = typeHouse
        