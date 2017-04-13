#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task4-15')
def task():
	pass
	#------- пишите код здесь -----
r.sleep = 0
for a in range(1,10):
        for b in range(1,10):
                r.pt()
                r.rt(2)
                r.pt()
        r.dn(2)
        for b in range(1,10):
                r.pt()
                r.lt(2)
                r.pt()
r.up()
r.rt()
for c in range(1,9):
        for d in range(1,9):
                r.pt()
                r.rt(2)
                r.pt()
        r.up(2)
        for d in range(1,9):
                r.pt()
                r.lt(2)
                r.pt()
r.up()
r.lt()
        #------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
