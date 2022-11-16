
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



#Zhanna (Нефункциональный функция)
movie = 'The good,the bad,and the ugly'
rating = 7

result = f'Movie:"{movie}",rating:{rating}'
print(result)
print()
movie = 'Titanic'
rating=9
result = f'Movie:"{movie}",rating:{rating}'
print(result)

#Zhanna 2 
def name_function(a,b,c):
    print(a+b)
    print(b+c)
    k = a-c
    print(c)
    print(k)
name_function(10,5,7)

#Кортеж
#список общего количества рабочих часов за каждую неделю.
#словарь

def people_age(): 
    d = dict(); 
    d['Jack'] = 30
    d['Kim'] = 28
    d['Bob'] = 27
    return d
d = people_age() 
print(d)

#Список
def natural_numbers(numbers = []):
   
   for i in range(1, 16):
       numbers.append(i)
   return numbers
 
print(natural_numbers())
#Кортеж
def fun(): 
    str1 = "Happy"
    str2 = "Coding"
    return str1, str2; 
str1, str2= fun() 
print(str1) 
print(str2)
