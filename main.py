#Задача 1
movie, cinema, time = input(), input(), input()
print('Билет на"', movie, '" в "', cinema, '" на ', time, 'забронирован')

#Задача 2
print('Зарплата за месяц')
z= int(input('»>'))
print('кол-во отработанных часов в выходные дни')
a = int(input('»>'))
print('Размер премии',(z*0.01)*a)

#Задача 3
price = input('Введите сумму:')
price = int(price)
price1 = price%1000
price2 = price%100
price3 = price%10
price4 = price3//1
price5 = price2//10
price6 = price1//100
price7 = price//1000
print(price4, '-по 1р')
print(price5, '- по 10р')
print(price6, '-по 100р')
print(price7, '-по 1000р')

#Задача 4
feedback = input('Оцените развлекательный комплекс:')
searching1 = feedback.find('весело')
searching2 = feedback.find('увлекательно')
searching3 = feedback.find('развлечения')
print('Результат анализа:', searching1, searching2, searching3)

#Задача 5
z = input()
print(z[(len(z)-1)//2])

#Задача 6
feedback = 'Алиса и Вася, большое спасибо за теплый приём'
name1 = feedback[0:5]
name2 = feedback[8:12]
print('Назначить премию', name1 + '/' + name2)

#Задача 7
while True:
    n = int( input('n = ') )
    s = ''
    for i in range(n-1, n+3):
        s += chr( ord('A') + i % 26 )
    print(s)

#Задача 8
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list.insert(1,'привет')
print(my_list)
removed = my_list.pop(3)
print(my_list)
print(removed)
print(my_list[1:5])
my_list.reverse()
print(my_list)
my_list_rev = list(reversed(my_list))

#Задача №9
tuple1 = ()
tuple2 = (1, 2, 3, 4, 5)

#Задача №10
s1 = {}
s2 = {1, 2, 3, 4}
s1 = {5, 6, 7, 'a', 8}
s2.remove(5)
s1.discard('a')

#Задача №11
dict1 = {} #Пустой словарь
dict2 = {1: 'mango', 2: 'paw paw'} #Словарь с элементамии

#Добавление элементов
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
dict_sample["Capacity"] = "1800CC"
print(dict_sample)

#Удаление элементов
dict_sample = {
  "Company": "Toyota",
  "model": "Premio",
  "year": 2012
}
del dict_sample["year"]
print(dict_sample)