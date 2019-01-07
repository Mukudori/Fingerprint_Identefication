import numpy as np

def matchingPoint(r, v):  # вход: кортеж точек эталона и кортеж проверяемого; выход (совпало, всего)
    all = 0
    match = 0
    checkLen = 30

    checkR = np.zeros(shape=(len(r[0])))
    checkV = np.zeros(shape=(len(v[0])))
    iv=0
    for i in v[0]:
        x = (i[0] - checkLen, i[0] + checkLen)
        y = (i[1] - checkLen, i[1] + checkLen)
        ir=0
        for j in r[0]:
            if j[0] >= x[0] and j[0]<=x[1] \
                    and j[1] >= y[0] and j[1]<=y[1]:
                match += 1
                checkR[ir]=1
                checkV[iv]=1
            ir+=1
            all += 1
        iv+=1

    try:
        persentR = np.compress(checkR==1, checkR).size / checkR.size * 100
    except:
        persentR = 0

    try:
        persentV = np.compress(checkV==1, checkV).size / checkV.size * 100
    except:
        persentV = 0



    '''for i in v[1]:
        x = (i[0] - checkLen, i[0] + checkLen)
        y = (i[1] - checkLen, i[1] + checkLen)
        all += 1
        for j in r[1]:
            try:
                if j[0] >= x[0] and j[0] <= x[1] \
                        and j[1] >= y[0] and j[1] <= y[1]:
                    match += 1
            except:
                pass

            all += 1'''

    return (match, all) , persentR, persentV