
#Фунцияның ішінде функция шақыру
def Square(X):
    return (X * X)

def SumofSquares(Array, n):
    Sum = 0
    for i in range(n):
        SquaredValue = Square(Array[i])
        Sum += SquaredValue
    return Sum

Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(Array)
Total = SumofSquares(Array, n)
print("Листтағы сандардың квадраттарының суммасы : ", Total)

#Map - мысал
def starts_with_A(s):
    return s[0] == "А"
fruit = ["Алма", "Банан", "Алмұрт", "Шабдалы", "Апельсин"]
map_object = map(starts_with_A, fruit)
print(list(map_object))

#Map
def myMapFunc(s):
    return s.upper()
my_str = "nabi aiman"
updated_list = map(myMapFunc, my_str)
print(updated_list)
for i in updated_list:
    print(i, end="")

#Map
org_list = [1, 2, 3, 4, 5]
def cube(num):
    return num ** 3
fin_list = list(map(cube, org_list))
print(fin_list)

#Filter - мысал
numbers = [1, 2, 3, 4, 5, 6, 7]
even_numbers_iterator = filter(lambda x: (x%2 == 0), numbers)
even_numbers = list(even_numbers_iterator)#Листқа айналдырады
print(even_numbers)

#Reduce - мысал
from functools import reduce
numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, numbers)) #10


