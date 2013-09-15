#-- coding: utf-8 --

class DewpointCalculator(object):
    """
    Eingaben: RelativeHumidity, Temperature, TemperatureSystem
    Rueckgaben:RelativeHumidity, Temperature, TemperatureSystem, DewpointTemperatur, AbsolutHumidity;
    Berechnung unstetig mit Formeln
    """
    ##    def __init__(self):
    ##        pass

    def convertTemperature(self, varTemperature, varSourceTemperatureSystem, varTargetTemperatureSystem):
        """
        varTargetTemperatureSystem: 'K' = Kelvin, 'C' = Celsius, 'F' = Fahrenheit
        """
        constCelsius = 273.15
        constFahrenheit1 = 1.8
        constFahrenheit2 = 255.3722
        varTemperatureKelvin = 0.00
        varTargetTemperature = 273.15

        #Quellsystem nach Kelvin
        if varSourceTemperatureSystem == "K":
            varTemperatureKelvin = varTemperature
        elif varSourceTemperatureSystem == "C":
            varTemperatureKelvin = varTemperature + constCelsius
        elif varSourceTemperatureSystem == "F":
            varTemperatureKelvin = (varTemperature / constFahrenheit1) + constFahrenheit2
        else:
            varTemperatureKelvin = 0.00

        #Kelvin ins Zielsystem
        if varTargetTemperatureSystem == "K":
            varTargetTemperature = varTemperatureKelvin
        elif varTargetTemperatureSystem == "C":
            varTargetTemperature = varTemperatureKelvin + constCelsius
        elif varTargetTemperatureSystem == "F":
            varTargetTemperature = (varTemperatureKelvin + constFahrenheit2) + constFahrenheit1
        else:
            varTargetTemperature = 0.00
        return varTargetTemperature


d = DewpointCalculator()
print(d.convertTemperature(100.00, "C", "K"))
print(d.convertTemperature(-32.00, "C", "F"))