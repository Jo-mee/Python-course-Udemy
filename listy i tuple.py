marketing = ['loyality program', 'client promotion', 'market research']
print(marketing)
marketing.append('public relations')
print(marketing)
print(marketing[3])
marketing.insert(2, 'investor relations')
print(marketing)

Emailmarketing = marketing.copy()
Emailmarketing.sort()

internalEmails = ['internal communication']
print(internalEmails + Emailmarketing)

#tuple
Emails = tuple(Emailmarketing)
print(Emails)




#Dictionary
chanels = {"Google" : 1480, "Email" : 300, "Natural Traffic" : 440, "TV Spot" : 700}
print(chanels)
print(chanels["Email"])

chanelsUpdate = {"Natural Traffic" : 520, "News" : 600}
chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
print(chanels.pop("Email"))
print(chanels)

#IF

MIN_LIKES = 500
MIN_SHARES = 100
num_likes = 1300
num_shares = 5000

if MIN_LIKES <= num_likes and MIN_SHARES <= num_shares:
    print('obniżamy o 10%')
else:
    print('warunek niespełniony')


isPizzaOrdered = False #czy klient kupił Pizzę
isBigDrinkOrdered = False #czy klient zamówił duży napój
isWeekend = True #czy jest weekend

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('dostajesz kupon')
else:
    print('kupuj dalej')


diskSize = 140 #oznaczająca wielkość dysku w GB
diskSizeUsed = 123 #oznaczająca ilość zajętego miejsca na dysku w GB
fileSize = 10 #oznaczająca wielkość pobieranego pliku w GB

if diskSize > diskSizeUsed + fileSize:
    print('File can be downloaded')
else:
    print('za mało miejsca')
