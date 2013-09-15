#-- coding: utf-8 --

class DewpointCalculatorDTO(object):
    """ Daten-Transfer-Objekt fuer Benutzerein-/ausgaben """

    def __init__(self, varTemperature, varRelativeHumidity, varInputTemperatureSystem, varOutputTemperatureSystem, varDewpointTemperature, varAbsoluteHumidity):
        self.__varTemperatureInput = None
        self.__varRelativeHumidityInput = None
        self.__varInputTemperatureSystem = None
        self.__varOutputTemperatureSystem = None

        self.__varDewpointTemperature = None
        self.__varAbsoluteHumidity = None

    #Gibt die eingegebne Temperatur an
    def setVarTemperatureInput(self, varTemperature):
        self.__varTemperature = varTemperature

    def getVarTemperatureInput(self):
        return self.__varTemperature

    def setVarRelativeHumidity(self, varRelativeHumidity):
        self.__varRelativeHumidity = varRelativeHumidity

    def getVarRelativeHumidity(self):
        return self.__varRelativeHumidity

    #Gibt das Eingabe-Temperatursystem an
    def setVarInputTemperatureSystem(self, varInputTemperatureSystem):
        self.__varInputTemperatureSystem = varInputTemperatureSystem

    def getInputTemperatureSystem(self):
        return self.__varInputTemperatureSystem

    #Gibt das Ziel-Temperatursystem an
    def setVarOutputTemperatureSystem(self, varOutputTemperatureSystem):
        self.__varOutputTemperatureSystem = varOutputTemperatureSystem

    def getVarOutputTemperatureSystem(self):
        return self.__varOutputTemperatureSystem

    def getVarDewpointTemperature(self):
        return self.__varDewpointTemperature

    def getVarAbsoluteHumidity(self):
        return self.__varAbsoluteHumidity