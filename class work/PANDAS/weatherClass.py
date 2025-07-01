class weather:
    def  __init__(self):
        
        self.__month = []
        self.__temperature = []
        self.__humidity = []

    def set_month(self, month):
        self.__month.append(month)
    def set_temperature(self, temperature):
        self.__temperature.append(temperature)
    def set_humidity(self, humidity):
        self.__humidity.append(humidity)
    def get_month(self):
        return self.__month
    def get_temperature(self):
        return self.__temperature
    def get_humidity(self):
        return self.__humidity
    