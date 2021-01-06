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

#zmienne

v1 = 126
v2 = '126'
v3 = 126.0
v4 = '126.0'
print(v1, type(v1))
print(v2, type(v2))
print(v3, type(v3))
print(v4, type(v4))
print(v1 + v3, type(v1+v3))
print(v2 + v4, type(v2+v4))
print(7-1*0+3+3)
print(4**5/2**3)


#9 +- * /

print(9/9+99)
# string jako tablica znaków

q = 'THE EYES'
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
print(q[0]+q[1]+q[2]+q[5]+q[3]+q[7]+q[4]+q[6])


q = "a gentleman"
print(q[3]+q[6]+q[7]+q[2]+q[0]+q[4]+q[5]+q[1]+q[8])

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[line.find(":")+2:]
print(time)
tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title)

print(((39*5+50)*20+1021)-1986)

print(349182*2+10/2-349182)
print(2*2+10/2-2)
print(7+7/7+7*7-7)


#LISTY
hitList = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitList.append('CHILD IN TIME')
hitList.append('AGAIN')
hitList.insert(3, 'HOTEL CALIFORNIA')
hitList.insert(0, 'THE SOUND OF SILENCE')
print(hitList.index('HOTEL CALIFORNIA'))
hitList.remove('HOTEL CALIFORNIA')
hitList[0] = 'Enjoy the silence'
hitsToRead = hitList.copy()
hitsToRead.sort()

print(hitList)
print(hitsToRead)