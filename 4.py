mport math
a=float(input('Введите число '))
"""Попросим ввести пользователя число"""

while a!=0:
        
        if a>0:
            b=math.sqrt(a)
            print('Корень числа =' ,b)
        else:
            print('Не вычислятся корень')
        a=float(input('Введите число '))
        

"""Создаём цикл, который выполняется, если а неравная нулю. При выполнении условия на экран выводится 
квадратный корень введённого числа, либо, если число отрицательное, выводится сообщение"""