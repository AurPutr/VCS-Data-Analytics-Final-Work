failas = open('autoparkas.txt')
failas2 = open('automobilio_marke.txt', 'w')
failas3 = open('senienos.csv', 'w', newline='')
headers = ['valstybinis_numeris', 'gamintojas', 'modelis', 'pagaminimo_metai', 'automobilio amzius']

from csv import reader, DictReader, writer

nuskaitytas = failas.read()
# print(nuskaitytas)
failas.close()
from csv import DictWriter

print('==========================================================')

automobiliai = []
with open('autoparkas.txt') as failas:
    for eilute in failas:
        eilute = eilute.rstrip('\n')
        isskaidyta = eilute.split(',')
        automobilis = dict(
            valstybinis_numeris = isskaidyta[0],
            gamintojas = isskaidyta[1],
            modelis = isskaidyta[2],
            pagaminimo_metai = isskaidyta[3]
        )
        automobiliai.append(automobilis)

print(automobiliai)
print('==========================================================')

automobilio_marke = []
for automobilis in automobiliai:
    automobilio_marke.append(automobilis['gamintojas'])
print(automobilio_marke)
print(len(automobilio_marke))


while True:
    marke = input('Iveskite norima automobilio gamintoja (is didziosios raides): ')
    if marke not in automobilio_marke:
        print(f'{marke} gamintojo automobilių sąraše nėra')
    if marke in automobilio_marke:
        break

for automobilis in automobiliai:
    if automobilis["gamintojas"] == marke:
        print(f"Automobilis {marke} {automobilis['modelis']}, valstybinis numeris: {automobilis['valstybinis_numeris']}, pagamintas {automobilis['pagaminimo_metai']}")
        failas2.write(f"Automobilis {marke} {automobilis['modelis']}, valstybinis numeris: {automobilis['valstybinis_numeris']}, pagamintas {automobilis['pagaminimo_metai']}\n")


print('==========================================================')
gamintoju_kiekis = {}

for gamintojas in automobilio_marke:
    if gamintojas in gamintoju_kiekis: #patikrint ar dabartinis gamintojas jau yra zodyne
        gamintoju_kiekis[gamintojas] += 1
    else:
        gamintoju_kiekis[gamintojas] = 1 #jei tokio dar nera tada =1 nes tai pirmasis jo kartas

for gamintojas, kiekis in gamintoju_kiekis.items():
    print(f'Gamintojas {gamintojas} sarase pasikartojo {kiekis} kartų')


print('==========================================================')
import datetime

siandien = datetime.date.today()
senienos = []
for automobilis in automobiliai:
    automobilis['automobilio amzius'] = siandien.year - int(automobilis['pagaminimo_metai'])
    if automobilis['automobilio amzius'] >10:
        senienos.append(automobilis)

if len(senienos) == 0:
    print('Senesniu nei 10 metu automobiliu sarase nera')
    failas3.write('Senesniu nei 10 metu automobiliu sarase nera')

else:
    for automobilis in senienos:
        csv_writer = DictWriter(failas3, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerow(automobilis)
        print(f'Senienu sarasas:\n {senienos}\n')



