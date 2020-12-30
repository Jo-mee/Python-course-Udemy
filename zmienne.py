classroom = "English:mamba"
print(classroom.upper())
print(classroom.split(':'))
WartoscPi = 3.14
PromienOkregu = 5
PoleKola = ('Pole Koła wynosi', WartoscPi * PromienOkregu ** 2)
print(PoleKola)

print(1,2,3)
print(1,2,3, sep='-')
print(1,2,3, sep='\n') #rodzielone nową linia
print(1,2,3, sep='\t') #rozdzielone tabem

print("bell: \a") # dodawanie dzwieku??
print("\u03A3") # wartości z kodu ASCI
print("backlash: \\")

print("TVP1, TVP2, TVN, Polsat, BBC, HBO, MTV")
print("TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV", sep=';')
print("I like computers","TVP1", "TVP2", "TVN", "Polsat", "BBC", "HBO", "MTV", sep=" but better is ")
ProgramName = 'BBC'
Item = 'News'
Time = '18:00'
print("I like watching ", ProgramName, " at ", Time, " on ", Item, ".", sep='')


text = 'mikołaj nadchodzi'
text2 = text.upper()
print(text)
print(text2)
print(text.replace('aj', 'ajek'))


text3='A good programmer is someone who always looks both ways before crossing a one-way street'

print(text3.upper().isupper())
print(text3.lower())
print(text3.endswith('street'))
print(text3.isupper())
print(text3.split())
print(text3.replace('one', '1'))
print(text3.find('one'))