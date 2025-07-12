from matplotlib import pyplot as plt
from numpy import block
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print('====================1===================================')

pd.set_option('display.max_rows', None)
df = pd.read_csv('saldainiai2.txt', delimiter=',', encoding='utf8')
print(df)

print('====================2===================================')

df['Suma'] = None
print(df)

print('====================3===================================')

df['Suma'] = df.Kaina * df.Kiekis
print(df)

print('====================4===================================')

while True:
    tipas = input('Iveskite dominanciu saldainiu tipa (pvz: sokoladiniai/kokosiniai/kavos ar pan). Prasome naudoti lietuviskas raides ir zodi vesti is didziosios raides: ')
    kiek_kainuoja = int(input('Iveskite kaina, kurios ieskote (daugiau uz X): '))
    ats = df.loc[(df['Skonis'].str.contains(tipas) & (df['Kaina'] > kiek_kainuoja))]
    if any (df['Skonis'].str.contains(tipas)):
        print(f'Jus pasirinkote {tipas} saldainiu tipa. Gauti rezultatai:')
        print('Pavadinimas, Skonis, Kiekis, Kaina, Suma')
        for i, eil in ats.iterrows():
           print(f'"{eil["Pavadinimas"]}", "{eil["Skonis"]}", {eil["Kiekis"]}, {eil["Kaina"]}, {eil["Suma"]}')
        break
    if not any(df['Skonis'].str.contains(tipas)):
        print(f'Jus ivedete {tipas} saldainiu tipa. Deja tokio neradome sarase.')



# print('====================5===================================')
#
# while True:
#     saldainis = input('Iveskite dominanciu saldainiu pavadinima. Prasome naudoti lietuviskas raides ir zodi vesti is didziosios raides: ')
#     ats = df.loc[(df['Pavadinimas'].str.contains(saldainis))]
#     if any (df['Pavadinimas'].str.contains(saldainis)):
#         istrinimas = df.drop(df.loc[df['Pavadinimas'].str.contains(saldainis)].index)
#         print('Sekmingai istrinta. Atnaujintas sarasas:')
#         print(istrinimas)
#         break
#     if not any(df['Pavadinimas'].str.contains(saldainis)):
#         print(f'Jus ivedete {tipas} saldainius. Deja tokio pavadinimo neradome sarase. Kartokite.')

print('====================6===================================')

#pagal saldainius skoni ir kieki susideliojam charta saldainius populiarumui nusakyti
#kuris skonis yra populiariausias
#sns.barplot(x='Skonis', y='Kiekis', data=df, ci=False).set_title('Saldainiu skoniu populiarumas')

#populiariausi yra saldainiai, kurie turi kelis skonius, tai =mogus gali pasirinkti "labiausiai patinkanti"
#ir taip pat sampano skonio.
#Dabar pabandysim atsifiltruoti situs du skonius ir pasiziureti siu saldainiu skoniu kainu pasiskirstyma
populiariausi =[]

filtras = df.loc[(df['Skonis'].str.contains('Labiausiai patinkančio') | df['Skonis'].str.contains('Šampano'))]
for i, sald in filtras.iterrows():
   populiariausi.append(sald)
df2 = pd.DataFrame(populiariausi)
print(df2)
#sns.lmplot(x='Kiekis', y='Suma', hue='Skonis', data=df2)

df3 = df2.reset_index()
print(df3)
sns.lmplot(x='index', y='Kaina', col='Skonis', hue='Skonis', data=df3)

#isvada, kad 'labiausiai patinkancio' skonio saldainiai perkami panasiais kiekiais kaip ir sampano skonio saldainiai.
#Bendra isleista suma vieno pirkimo metu 'labiausiai patinkancio' skonio buna nezymiai didesne.
#Taip pat paziurejus saldainiu kainu pasiskirstyma galima matyti, kad 'labiausiai patinkancio' skonio saldainiai yra
#brangesni nei sampano skonio saldainiai.


plt.show() #block=True