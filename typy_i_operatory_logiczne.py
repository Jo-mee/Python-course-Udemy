#operatory

isAutomaticMode = False # True oznacza, że kierowca ustawił pokrętło sterujące światłem na tryb automatyczny
is80PercentLight = True # wartość True oznacza, że "chyba" mamy dzień, bo jest dość dużo światła. False, tzn. że jest dość ciemno i światła powinny się zaświecić
isDirectLight = False # True oznacza, że nisko położone słońce świeci wprost w oczy kierowcy.
isRainy = True # True oznacza, że pada deszcz, jest mgła lub mamy do czynienia z innymi niekorzystnymi warunkami atmosferycznymi.

turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)


print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)


