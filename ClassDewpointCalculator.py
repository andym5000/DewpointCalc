#-- coding: utf-8 --
#Festlegung konkreten Klasse Taupunktrechner
#Eingaben: RelativeHumidity, InputTemperature, InputTemperatureSystem
#Rückgaben: RelativeHumidity, OutputTemperature, OutputTemperatureSystem, DewpointTemperature, AbsoluteHumidity

import FuncTempCalc


class Dewpointcalculator(object):
    """Eingaben: RelativeHumidity, Temperature, InputTemperatureSystem Rueckgaben:RelativeHumidity, Temperature,
       TemperatureSystem, DewpointTemperatur, AbsolutHumidity; Berechnung unstetig mit Formeln"""


def __init__(self, varRelativeHumidity, varInputTemperature, varInputTemperatureSystem, varOutputTemperatureSystem, varDewpointTemperature, varAbsoluteHumidity):
    """Defaultconstructor"""
    #Speicherplatz den Variablen zuweisen
    self.__varRelativeHumidity = None
    self.__varInputTemperature = None
    self.__varInputTemperatureSystem = None
    self.__varOutputTemperatureSystem = None
    self.__varDewpointTemperature = None
    self.__varAbsoluteHumidity = None


def getVarRelativeHumidity(self):
    return self.__varRelativeHumidity


def setVarRelativeHumidity(self, varRelativeHumidity):  #Setter fuer __varRelativeHumidity
    self.__varRelativeHumidity = varRelativeHumidity


def getVarInputTemperature(self):
    return self.__varTemperature


def setVarInputTemperature(self, varTemperature):  #Setter fuer __varTemperature
    self.__varTemperature = varTemperature


def getVarInputTemperatureSystem(self):
    return self.__varInputTemperatureSystem

def setVarInputTemperatureSystem(self, varInputTemperatureSystem):  #Setter fuer __varInputTemperatureSystem
    self.__varInputTemperatureSystem = varInputTemperatureSystem

def setOutputTemperatureSystem(self, varOutputTemperatureSystem):   #Setter für varOutputTemperatureSystem
    self.__varOutputTemperatureSystem = varOutputTemperatureSystem

def getVarOutputTemperatureSystem(self):
    return self.__varOutputTemperatureSystem


def getVarDewpointTemperature(self):
    #return self.__varDewpointTemperature
    return self.__varTemperature


def getVarAbsoluteHumidity(self):
    #return self.__varAbsoluteHumidity
    return self.__varRelativeHumidty

FuncTempCalc.convertTemperature(getVarTemperature(),getVarTemperatureSystem(),)
"""varTargetTemperatureSystem: 'K' = Kelvin, 'C' = Celsius, 'F' = Fahrenheit
:param self:
:param varTemperature:
:param varSourceTemperatureSystem:
:param varTargetTemperatureSystem:
"""


def calculateDewpoint(self, ):
    pass