
pupils = {'Ученики': {}}
open_classrooms = [i for i in range(1,21)]
closed_classrooms = []

def register(name,classroom):
    if not pupils[name] in pupils['Ученики']: #test
        pupils['Ученики'][name] = classroom # test 2
        open_classrooms.remove(name)
        closed_classrooms.append(name)
        print(f'Ученик добавлен в {pupils['Ученики']}\n')
    else:
        print(f'Такой ученик уже существует. Он учится в {pupils['Ученики'][name]} классе.')

def delete(name):
    closed_classrooms.remove(pupils[name])
    open_classrooms.append(pupils[name])


def closed_rooms():
    return closed_classrooms


action = input('Выберите действие: ')

if action.lower() == 'добавить':
    pupils_name = input('Введите имя: ')
    print(open_classrooms)
    pupils_room = input('Выберите класс: ')
    register(pupils_name, pupils_room)
    # if pupils_room in open_classrooms:
    #     register(pupils_name, pupils_room)
    # else:
    #     print('Класс занят.')

elif action.lower() == 'убрать':
    pupils_name = input('Введите имя: ')
    if pupils_name in pupils:
        delete(pupils_name)
    else:
        print('Нет такого ученика.')

elif action.lower == 'занятые':
    print(closed_rooms())
else:
    print('Неизвестная операция.')





# sum = lambda chislo1,chislo2: chislo1+chislo2
# chislo1 = int(input('Введите первое число: '))
# chislo2 = int(input('Введите второе число: '))
#
# print(sum(chislo1,chislo2))