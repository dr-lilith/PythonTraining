# ПЕРВАЯ:
# рандомно присвоить порядковые номера для очередности выступлений участников фестиваля без функции рандом.
numbers = dict(
    zip({'иванов', "петров", "сидоров", "яковлева", "наумова", "гришин", "петренко", "бубнов", "дяченко", "рябин"},
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
print(numbers)

# ВТОРАЯ:
# Фирма хочет нанять команду для нового проекта. У идеально объективного HRа есть 4 списка работников по данным характеристикам:
#  - умные
#  - трудолюбивые
#  - с хорошим английским
#  - не требующие высокой зарплаты
# Фирма готова взять 1 идеального работника (соответствующего всем пунктам), 2х не очень умных стажеров (но соответствующих остальным пунктам),
# 1 разраба без инглиша (соответствующего остальным пунктам) и 1 охуевшего и ленивого тимлида, который будет следить за работой всей команды и общаться с кастомером.
# Помогите HRу сделать правильные офферы:D

clever = ['Смирнов', 'Рябов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов',
          'Петров', 'Волков', 'Соловьёв', 'Васильев']
hardworking = ['Лазарев', 'Медведев', 'Ершов', 'Никитин', 'Соболев', 'Рябов', 'Поляков', 'Цветков', 'Данилов', 'Жуков',
               'Фролов', 'Новиков', 'Журавлёв', 'Николаев', 'Крылов', 'Максимов', 'Сидоров', 'Осипов']
goodEnglish = ['Карпов', 'Афанасьев', 'Власов', 'Данилов', 'Маслов', 'Исаков', 'Тихонов', 'Соколов', 'Аксёнов',
               'Гаврилов', 'Родионов', 'Котов', 'Горбунов', 'Кудряшов', 'Быков', 'Новиков', 'Зуев', 'Ершов', 'Мухин']
cheap = ['Сафин', 'Данилов', 'Елисеев', 'Новиков', 'Орехов', 'Ершов', 'Исаев', 'Евдокимов', 'Кабанов', 'Рябов', 'Юдин',
         'Носков', 'Капустин', 'Кулагин', 'Лапин', 'Кошелев']
cleverSet = set(clever)
hardworkingSet = set(hardworking)
goodEnglishSet = set(goodEnglish)
cheapSet = set(cheap)
ideal = cleverSet & hardworkingSet & goodEnglishSet & cheapSet
trainee = hardworkingSet & goodEnglishSet & cheapSet - cleverSet
noEnglish = cleverSet & hardworkingSet & cheapSet - goodEnglishSet
teamLead = cleverSet & goodEnglishSet - hardworkingSet - cheapSet
print('ideal: ', ideal)
print('trainee: ', trainee)
print('noEnglish: ', noEnglish)
print('teamLead: ', teamLead)
