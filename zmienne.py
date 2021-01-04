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

#.......................................................
#konkatenacja napisów

drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'

path = drive + folder + file
print(path)

#surowy tekst r rzed napisem
text = "text with \n newline"
text2 = r'surowy \n text'
print(text)
print(text2)

#integer a string

article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal 
comedy troupe who created the sketch comedy television show Monty Python\'s Flying Circus, which 
first aired on the BBC in 1969. Forty-five episodes were made over four series. The Python 
phenomenon developed from the television series into something larger in scope and impact, 
including touring stage shows, films, albums, books and musicals.
'''

print(article.upper().lower().replace('monty', 'flying').split(' ').count('python'))

print('to print the \\ you need to put \\ twice in your text like this: \\\\ ')
print("The best hits of \'80s!!!")

#kalkulator

amountPLN = 234

print('cur\t exchange\t amount')
print('USD \t 3.65 \t', amountPLN/3.65)
print('EUR \t 4.23 \t', amountPLN/4.23)

#..............

ValueAsText = "123.45"
factor = 1.23
print('value is', ValueAsText, 'factor is', factor, 'value*factor =', float(ValueAsText)*factor)


#.................

helloMessage = "Hello %s!"
print(helloMessage % ('Kate'))
print(helloMessage % ('Adam'))

helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format('Maggy'))
helloMessag3 = "%s has %d %s"
print(helloMessag3 % ('Kate', 3, 'tadams'))
helloMessage4 = "{0:s} has {1:d} {2:s}"
print(helloMessage4.format('Amy', 133, 'cats'))

#........................................................
name = 'Joanna'
age = 25
daysInYear = 365
message1 = "{0:s} is {1:d} years old, so is about {2:d} days old"
print(message1.format(name, age, age * daysInYear))

message2 = "%s is %d years old, so is about %d days old"
print(message2 % (name, age, age * daysInYear))

print('1234567890 dzielone przez 12345 =', 1234567890//12345)
print('1234567890 dzielone przez 12345 daje resztę =', 1234567890 % 12345)
