print('hello, hat day is today?')

from datetime import date

date.today()
print('todayis:')
print(date.today().strftime('%A'))
today: object = date.today()
print("Today's date:", today)

test: str = "testujemy"
print(test)

# liczba min na godz i liczba godz w dobie
blinksPerMin = 20
minInHour = 60
HoursInDay = 24
daysInYear = 365

# liczba lat
Years = 50

# liczba mrugniec w ciągu X = 50 lat pomijając godziny snu
print(blinksPerMin * minInHour * HoursInDay * daysInYear * Years)
