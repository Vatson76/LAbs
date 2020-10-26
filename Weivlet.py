import random
import math
import time
import matplotlib.pyplot as plt
import numpy as np

Num = 2
f = 6

fig, ax = plt.subplots()
otr = np.linspace(0, 512, 512)

def lifting(signal, lvl):
    lvl -= 1

    x = [a for i, a in enumerate(signal) if  i % 2]  # нечетные по сути, четные по индексу
    y = [a for i, a in enumerate(signal) if not i % 2]  # четные по сути, нечетные по индексу

    p = [signal[i * 2 + 1] - signal[i * 2] for i, _ in enumerate(x)]  # предсказания
    u = [signal[i * 2] + zn / 2 for i, zn in enumerate(p)]  # обновления

    di = [x[i] - zn for i, zn in enumerate(p)]  # x-p
    si = [zn + y[i] for i, zn in enumerate(u)]  # y+u

    if lvl == 0:
        sm2 = []
        for i in range(len(di)):
            sm2.extend([di[i], si[i]])
        return sm2

    else:
        si = lifting(si, lvl)
        sm2 = []
        for i in range(len(di)):
            sm2.extend([di[i], si[i]])
        return sm2

if __name__ == '__main__':

	sm = [(4*math.cos(4*math.pi*i*Num) + random.normalvariate(0, 1) + f) if i == 299
		  else (4*math.cos(4*math.pi*i*Num) + random.normalvariate(0, 1)) for i in range(0, 512)] #исходный сигнал

	LiftedSignal = lifting(sm, 3)

	ax.plot(otr, sm)
	plt.show()

	ModuleMax52 = sorted([abs(zn) for zn in LiftedSignal], reverse=True)[:52] # 10% максимальных по модулю значений сигнала
	ClearedSignal = [zn if abs(zn) in ModuleMax52 else 0 for i, zn in enumerate(LiftedSignal) ] # сигнал только с макс. значениями

	counter = 1
	RecoveredSignal = ClearedSignal.copy()

	while counter != len(sm):  # Восстановление

		counter*=2
		#print('counter->', counter)

		mas1 = RecoveredSignal[-counter:]
		#print('mas1->', mas1)

		mas2 = mas1[:len(mas1)//2]
		#print('mas2->', mas2)
		mas3 = mas1[len(mas1)//2:]
		#print('mas3->', mas3)

		mas2 = [a*math.sqrt(2) for a in mas2]
		#print('mas2->*sqrt', mas2)
		mas3 = [a/math.sqrt(2) for a in mas3]
		#print('mas3->/sqrt', mas3)

		for i, zn in enumerate(mas3):
			mas1[2*i+1] = zn + 1/2*mas2[i]
			mas1[2*i] = zn - 1/2*mas2[i]
		#print('mas1fin', mas1)

		RecoveredSignal[-counter:] =  mas1

	fig, ax = plt.subplots()
	otr = np.linspace(0, 512, 512)
	ax.plot(otr, RecoveredSignal)
	plt.show()

	# print('ClearedSignal -> {}\nRecovered signal ->{}'.format(ClearedSignal, RecoveredSignal)


else:
	#---------Проверка-------------

	x = [a for i, a in enumerate(sm) if not i % 2]  # нечетные по сути, четные по индексу
	y = [a for i, a in enumerate(sm) if i % 2]  # четные по сути, нечетные по индексу

	p = [sm[i*2+1]-sm[i*2] for i, _ in enumerate(x)]  # предсказания
	u = [sm[i*2]+zn/2 for i, zn in enumerate(p)]  # обновления

	di = [x[i] - zn for i, zn in enumerate(p)]  # x-p
	si = [zn + y[i] for i, zn in enumerate(u)]  # y+u

	sm4 = []
	for i in range(len(di)):
	    sm4.extend([di[i], si[i]])
	print('1',sm4)

	x1 = [a for i, a in enumerate(si) if not i % 2]  # нечетные по сути, четные по индексу
	y1 = [a for i, a in enumerate(si) if i % 2]  # четные по сути, нечетные по индексу

	p1 = [si[i*2+1]-si[i*2] for i, _ in enumerate(x1)]  # предсказания
	u1 = [si[i*2]+zn/2 for i, zn in enumerate(p1)]  # обновления

	di1 = [x1[i] - zn for i, zn in enumerate(p1)]  # x1-p1
	si1 = [zn + y1[i] for i, zn in enumerate(u1)]  # y1+u1

	sm3 = []
	for i in range(len(di1)):
	    sm3.extend([di1[i], si1[i]])

	sm2 = []
	for i in range(len(di)):
	    sm2.extend([di[i], sm3[i]])
	print('2', sm2)

	print('проверка', sm2)
	print('функция', lifting(sm, 3))




