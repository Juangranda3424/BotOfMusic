from House import House

class WaterMeter(House):
    def __init__(self, idCondominium, nameCondominium, city, idHouse, typeHouse, lastReading, statusWaterMeter, meterNumber, modelWaterMeter):
        super().__init__(idCondominium, nameCondominium, city, idHouse, typeHouse)
        self.__lastReading = lastReading
        self.__statusWaterMeter = statusWaterMeter
        self.__meterNumber = meterNumber
        self.__model = modelWaterMeter  
    
    def get_last_reading(self):
        return self.__lastReading

    def set_last_reading(self, lastReading):
        self.__lastReading = lastReading

    def get_status_water_meter(self):
        return self.__statusWaterMeter

    def set_status_water_meter(self, statusWaterMeter):
        self.__statusWaterMeter = statusWaterMeter

    def get_meter_number(self):
        return self.__meterNumber

    def set_meter_number(self, meterNumber):
        self.__meterNumber = meterNumber

    def get_model(self):
        return self.__model

    def set_model(self, modelWaterMeter):
        self.__model = modelWaterMeter