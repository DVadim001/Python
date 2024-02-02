spis = ['Pavel', 'Sasha', 'Ivan', 'Petya']

print(spis)

# Как вставлять новое имя на место того, которое удалили (на тот же индекс)?
edited_name = input('Введите имя для редактирования: ')

spis.remove(edited_name)

new_name = input('Введите новое имя: ')

new_name = spis.append(new_name)
print(spis)
