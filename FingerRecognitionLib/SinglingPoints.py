import numpy as np

def checkThisPoint(img, y, x):  # подсчет количества черных в окрестности
    c = 0
    for i in range(y - 1, y + 1):
        for j in range(x - 1, x + 1):
            try:
                if img[i,j] == 0:
                    c += 1
            except:
                print('Выход за пределы матрицы на (%i , %i)' % (i,j))
                pass

    return c - 1


def findCheckPoint(img, num =0):  # формирование списков точек ветвления и конечных
    y = len(img)
    x = len(img[0])

    N = x * y
    persent = N / 100
    it = 0

    branchPoint = []
    endPoint = []
    for i in range(y):
        for j in range(x):
            if img[i,j] == 0:
                t = checkThisPoint(img, i, j)
                if t == 1:

                    endPoint.append((i,j))

                if t == 3:

                    branchPoint.append((i,j))
            it+=1
        print("Выделение точек %i: %f %%" % (num, it / persent))

    return (np.array(branchPoint), np.array(endPoint))

def __removeDouble(x, y):  # возвращает список элементов, у которых нет одинакового в другом  списке
        z = []
        N = len(x) * len(y) * 2
        persent = N / 100
        it =0

        for i in x:
            c = True
            for j in y:
                if (i == j).all():
                    c = False
                it+=1
            if c:
                z.append(i)
            print("Удаление дубликатов : %f %%" % (it / persent))
        print('remove 1')
        for i in y:
            c = True
            for j in x:
                if (i == j).all():
                    c = False
                it+=1
            if c:
                z.append(i)
            print("Удаление дубликатов : %f %%" % (it / persent))

        return z

def delNoisePoint(r):  # на входе кортеж (ветвление, конечные)
    tmp = []
    tmp2 =[]
    N = len(r[0])*len(r[1])
    persent = N/100

    print('Количество итераций = %i' % N)
    n =0
    it=0
    for i in r[1]:
        x = (i[0] - 5, i[0] + 5)
        y = (i[1] - 5, i[1] + 5)
       # print('(x,y) = (%i,%i)' % (x,y))
        for j in r[0]:
            if j[0] >= x[0] and j[0]<=x[1] \
                    and j[1] >= y[0] and j[1]<=y[1]:
                tmp.append(i)
                tmp2.append(j)
            it+=1
                #print('(i1,j1) = (%i,%i), i2,j2) = (%i,%i)'%(i[0],i[1],j[0],j[1]))

        print('Определение шума завершено: %f %%' % (it/persent))

    tmp = np.array(tmp)
    tmp2 = np.array(tmp2)
    return (r[0], __removeDouble(r[1], tmp))