#Exercise 1: Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
print(list1)
list1.reverse()
print(list1)
print('===========================')
#Exercise 2: Concatenate two lists index-wise
list1 = ['M', 'na', 'i', 'Ke']
list2 = ['y', 'me', 's', 'lly']
print(list1)
print(list2)
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)

list1 = ['Ma', 'var', 'y', 'Aure']
list2 = ['no', 'das', 'ra', 'lija']
list3 = [a+b for a,b in zip(list1, list2)]
print(list3)


print('===========================')
#Exercise 3: Turn every item of a list into its square
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers2 = [x ** 2 for x in numbers]
print(numbers)
print(numbers2)


print('===========================')
#Exercise 4: Concatenate two lists in the following order
list1 = ['Hello', 'take']
list2 = ['Dear', 'Sir']
list3 = [i + j for i in list1 for j in list2]
print(list3)


row = 5
for sk in range(1,row+1,1):
    for eil in range(1, sk+1):
        print(eil, end=' ')
    print("")


# skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
# suma = 0
# for sk in range(1, skaicius+1):
#     suma += sk
# print('Suma yra: ', suma)


skaicius = int(input('Iveskite norima sveikaji skaiciu: '))
daugyba = 1
for sk in range(1, 11):
    daugyba = skaicius * sk
    print(sk, '==', daugyba)