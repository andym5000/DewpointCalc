#-- coding: utf-8 --

def convertTemperature(varTemperature, varSourceTemperatureSystem, varTargetTemperatureSystem):
    """varTargetTemperatureSystem: 'K' = Kelvin, 'C' = Celsius, 'F' = Fahrenheit
    """
    constCelsius = 273.15
    constFahrenheit1 = 1.8
    constFahrenheit2 = 459.67
    #varTargetTemperature = 273.15

    #Großbuchstaben
    ##varSourceTemperatureSystem = Py_UNICODE_TOUPPER(varSourceTemperatureSystem)
    ##varTargetTemperatureSystem = s.upper(varTargetTemperatureSystem)

    #Quellsystem nach Kelvin
    if varSourceTemperatureSystem == "K":
        varTemperatureKelvin = varTemperature
    elif varSourceTemperatureSystem == "C":
        varTemperatureKelvin = varTemperature + constCelsius
    elif varSourceTemperatureSystem == "F":
        varTemperatureKelvin = (varTemperature + constFahrenheit2) / constFahrenheit1
        #varTemperatureKelvin = (varTemperature * constFahrenheit1) - constFahrenheit2
    else:
        varTemperatureKelvin = 0.00

    #Kelvin ins Zielsystem
    if varTargetTemperatureSystem == "K":
        return varTemperatureKelvin
    elif varTargetTemperatureSystem == "C":
        return varTemperatureKelvin - constCelsius
    elif varTargetTemperatureSystem == "F":
        return (varTemperatureKelvin * constFahrenheit1) - constFahrenheit2
    else:
        return 0.00
        #convertTemperature(100, "C", "K")