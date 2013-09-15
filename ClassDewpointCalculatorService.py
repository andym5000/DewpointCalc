#-- coding: utf-8 --

#Abstraktionsschicht zwischen Geschaeftsprozess und GUI

import DewpointCalculatorDTO
import ClassDewpointCalculator


class DewpointCalculatorService(object):
    """stellt Service fuer Darstellung bereit"""


def __init__(self, dewpointCalculatorDTO):
    self.__varInputTemperature = None
    self.__varInputRelativeHumidity = None
    self.__varInputTemperatureSystem = None
    self.__varOutputTemperatureSystem = None


def setVarInputTemperature(self, dewpointCalculatorDTO.


getVarTemperatureInput())
:
self.__varInputTemperature = varInputTemperature


def setVarInputRelativeHumidity(self, dewpointCalculatorDTO.


getVarRelativeHumidity())

:
self.__varInputRelativeHumidity = varInputRelativeHumidity


def setVarInputTemperatureSystem(self, dewpointCalculatorDTO.


getVarTemperatureSystem())

:
self.__varInputTemperatureSystem = varInputTemperatureSystem

# Diese Methode wird aus der GUI-Schicht heraus aufgerufen


def receiveInput(dewpointCalculatorDTO):
    pass


# Diese Methode ruft den Rechner auf und uebergibt die geforderten Parameter
def invokeDewpointCalculator(dewpointCalculator.


calculateDewpoint(self.getVarInputTemperature(), self.getVarInputRelativeHumidity,
                  self.getVarInputTemperatureSystem)):
setVarDewpoinTemperature(self.__varDewpointTemperature = dewpointCalculator.getVarDewpointTemperature())
setVarAbsoluteHumidity(Self.__varAbsoluteHumidity = dewpointCalculator.getVarAbsoluteHumidity()
return True