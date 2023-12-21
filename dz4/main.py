list = 'theword'
name = [i for i in list]
print(name)

list = ['a','b','c','e','f','g']
name= ['the '+i for i in list]
print(name)

list = [i for i in range(1,21)]
print(list)

list = [1,2,3,4,5,6,7,8,9,10]
num = [i for i in list if i%2 ==0]
print(num)

list = ['Pavel', 'Ivan', 'Timur', 'Oleg', 'Vanya', 'Olga']
name = [i for i in list if 'a' or 'o' in i]
print(name)

numbers = [i for i in range(1,21)]
num = [i*2 for i in numbers]
print(num)

names = ['Pavel', 'Roma', 'Ivan', 'Vasya', 'Elena', 'Timur']
word = [i[0] for i in names]
print(word)

