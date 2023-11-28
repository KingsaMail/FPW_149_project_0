from random import randint #модуль для выбора первого игрока (случайно)

from object import Plaer, FieldOfGame

def custom_plaer():
    """Генерация данных игроков."""
    print()
    p_1 = input("Введите имя первого игрока: ")
    p_2 = input("Введите имя второго игрока: ")
    
    if randint(0,1):
        p_11, p_22 = 'X', 'O'
    else:
        p_11, p_22 = 'O', 'X'
    if randint(0,1):
        p_111, p_222 = 1, 2
    else:
        p_111, p_222 = 2, 1
    
    return (p_1, p_11, p_111), (p_2, p_22, p_222)

p_tuple = custom_plaer()        
p_1 = Plaer(*p_tuple[0]) # Создание игроков
p_2 = Plaer(*p_tuple[1])

if p_1.position == 1:  #Вывод подсказки кто чем играет и когда ходит
    print(f'Игрок {p_1.name} играет "{p_1.chip}" и ходит {p_1.position}-ым')
    print(f'Игрок {p_2.name} играет "{p_2.chip}" и ходит {p_2.position}-ым')
else:
    print(f'Игрок {p_2.name} играет "{p_2.chip}" и ходит {p_2.position}-ым')
    print(f'Игрок {p_1.name} играет "{p_1.chip}" и ходит {p_1.position}-ым')
    
# список игроков
plaer_list = []    
if p_1.position == 1:
    plaer_list.append(p_1)
    plaer_list.append(p_2)
else:
    plaer_list.append(p_2)
    plaer_list.append(p_1)
 
while True:  # цикл игры
    print()    
    field = FieldOfGame()  # создаем поле      
    print('ходит ', plaer_list[0].name, '\n') 
    
    while True: #цикл раунда
        
        field.drow() #рисуем поле
        # выбор возможных вариантов хода
        tern_field = list(filter(lambda x: type(x)==int, field.field)) 
        
        while True: # цикл корректности хода
            print('\n', plaer_list[0].name, '(', plaer_list[0].chip, ')', end='')
            tern = input(" введите номер позиции (Q - выход из игры): ")
            if tern in ['q', 'Q']:
                exit()
            print()
            if int(tern) not in tern_field:
                print('попробуйте ещё раз')
                continue
            tern = int(tern)            
            break
        
        field.field_set(tern, plaer_list[0].chip) #ход игрока, ставим фишку
        if field.chek(plaer_list[0].chip): #проверка на выигрыш
            plaer_list[0].score = 1
            print(plaer_list[0].name, 'выиграл', '\nобщий счёт:')
            print(plaer_list[0].name, '-',plaer_list[0].score)
            print(plaer_list[1].name, '-',plaer_list[1].score)
            break
        else:
            plaer_list.append(plaer_list.pop(0)) #смена игрока
        
    if input("ещё играем? (Y/N)") in ['N', 'n']:
        exit()
        
    
    
