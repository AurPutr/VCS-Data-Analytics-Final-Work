# 1. Raskite visus sekos range(-101,101,3) skaitmenis, kurie:
# • Dalinasi iš 7 ir yra teigiami. Raskite tokių skaičių kiekį.
# • Dalinasi iš 5 ir yra neigiami. Raskite tokių skaičių kiekį.
# • Lyginiai ir dalinasi iš 3 be liekanos (Turi nerasti).
# • Nelyginiai ir dalinasi iš 7 be liekanos. Raskite tokių skaičių kiekį.
# 2. Pakeiskite pirmos užduoties range parametrų nurodymą per kintamuosius, ir kad
# jie būtų suvedami iš klaviatūros.


print('=====================1=============================')
skaiciai = []

for sk in range(-101,101,3):
    if sk %7 == 0 and sk > 0:
        skaiciai.append(sk)
print(skaiciai)
print('Visko skaiciu kurie dalinasi is 7 ir yra teigiami yra', len(skaiciai))

skaiciai2 = []
for sk in range(-101, 100, 3):
    if sk %5 == 0 and sk < 0:
        skaiciai2.append(sk)
print(skaiciai2)
print('Visko skaiciu kurie dalinasi is 5 ir yra neigiami yra', len(skaiciai2))

skaiciai3 = []
for sk in range(-101, 101, 3):
    if sk %2 == 0 and sk %3 == 0:
        skaiciai3.append(sk)

print(skaiciai3)
print('Visko skaiciu kurie yra lyginiai ir dalinasi is 3 yra', len(skaiciai3))


skaiciai4 = []
for sk in range(-101, 101, 3):
    if sk %2 != 0 and sk %7 == 0:
        skaiciai4.append(sk)

print(skaiciai4)
print('Visko skaiciu kurie yra nelyginiai ir dalinasi is 7 yra', len(skaiciai4))


print('=====================2=============================')
# skaiciai = []
# pradzia = int(input('Iveskite norimo intervalo pradzia: '))
# pabaiga = int(input('Iveskite norimo intervalo pabaiga: '))
# for sk in range(pradzia, pabaiga +1):
#     if sk %7 == 0 and sk > 0:
#         skaiciai.append(sk)
# print(skaiciai)
# print('Visko skaiciu kurie dalinasi is 7 ir yra teigiami yra', len(skaiciai))
#
# skaiciai2 = []
# for sk in range(pradzia, pabaiga +1):
#     if sk %5 == 0 and sk < 0:
#         skaiciai2.append(sk)
# print(skaiciai2)
# print('Visko skaiciu kurie dalinasi is 5 ir yra neigiami yra', len(skaiciai2))
#
# skaiciai3 = []
# for sk in range(pradzia, pabaiga +1):
#     if sk %2 == 0 and sk %3 == 0:
#         skaiciai3.append(sk)
#
# print(skaiciai3)
# print('Visko skaiciu kurie yra lyginiai ir dalinasi is 3 yra', len(skaiciai3))
#
#
# skaiciai4 = []
# for sk in range(pradzia, pabaiga +1):
#     if sk %2 != 0 and sk %7 == 0:
#         skaiciai4.append(sk)
#
# print(skaiciai4)
# print('Visko skaiciu kurie yra nelyginiai ir dalinasi is 7 yra', len(skaiciai4))

print('============Antra=dalis==================')
failas = open('parduotuve1.txt',encoding='utf8')
failas2 = open('parduotuve2.txt', encoding='utf8')

prekes = []

for eilute in failas:
    eilute = eilute.rstrip('\n')
    isskaidyta = eilute.split(',')
    preke = dict(
            preke = isskaidyta[0],
            kategorija = isskaidyta[1],
            esamas_kiekis = int(isskaidyta[2]),
            reikiamas_kiekis = int(isskaidyta[3])
        )
    prekes.append(preke)

print(prekes)

prekes2 = []

for eil in failas2:
    eil = eil.rstrip('\n')
    isskaidyta2 = eil.split(',')
    preke2 = dict(
            preke = isskaidyta2[0],
            kategorija = isskaidyta2[1],
            esamas_kiekis = int(isskaidyta2[2]),
            reikiamas_kiekis = int(isskaidyta2[3])
        )
    prekes2.append(preke2)

print(prekes2)

print('=================1================')

nepakankamas_prekiu_kiekis_pard1 = []
for preke in prekes:
    if preke['esamas_kiekis'] < 50:
        nepakankamas_prekiu_kiekis_pard1.append(preke)

nepakankamas_prekiu_kiekis_pard2 = []
for preke2 in prekes2:
    if preke2['esamas_kiekis'] < 50:
        nepakankamas_prekiu_kiekis_pard2.append(preke2)

print(nepakankamas_prekiu_kiekis_pard1)
print(nepakankamas_prekiu_kiekis_pard2)

print('=================2================')
print(f'Pirmojoje parduotuveje viso yra {len(nepakankamas_prekiu_kiekis_pard1)} prekiu, kuriu kiekis yra maziau nei 50 vnt')
print(f'Antrojoje parduotuveje viso yra {len(nepakankamas_prekiu_kiekis_pard2)} prekiu, kuriu kiekis yra maziau nei 50 vnt')

print('=================3================')
if len(nepakankamas_prekiu_kiekis_pard1) > len(nepakankamas_prekiu_kiekis_pard2):
    print('Pirmojoje parduotuveje yra didesnis skaicius prekiu, kuriu kiekis yra maziau nei 50')
elif len(nepakankamas_prekiu_kiekis_pard1) < len(nepakankamas_prekiu_kiekis_pard2):
    print('Antrojoje parduotuveje yra didesnis skaicius prekiu, kuriu kiekis yra maziau nei 50')
elif len(nepakankamas_prekiu_kiekis_pard1) == len(nepakankamas_prekiu_kiekis_pard2):
    print('Abiejose parduotuvėse tokių prekių, kurių esamas kiekis parduotuvėje yra mažiau nei 50 vienetų, yra po lygiai')

print('=================4================')

maziausias = prekes[0]['reikiamas_kiekis']
for preke in prekes:
    if preke['reikiamas_kiekis'] < maziausias:
        maziausias = preke['reikiamas_kiekis']
        print(f'Pirmojoje parduotuveje prekei {preke['preke']} reikiamas tureti kiekis yra {preke['reikiamas_kiekis']} ir tai yra maziausias reikiamas tureti kiekis visoje parduotuveje')


maziausias2 = prekes2[0]['reikiamas_kiekis']
for preke2 in prekes2:
    if preke2['reikiamas_kiekis'] < maziausias2:
        maziausias2 = preke2['reikiamas_kiekis']
        print(f'Antrojoje parduotuveje prekei {preke2['preke']} reikiamas tureti kiekis yra {preke2['reikiamas_kiekis']} ir tai yra maziausias reikiamas tureti kiekis visoje parduotuveje')
#kaip padaryti kad mestu tik viena pacia maziausia?





