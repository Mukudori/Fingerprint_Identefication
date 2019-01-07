
def tmpDelete(img):  #вызов процедуры скелетизации, на входе список списков(после бинаризации)
    h=len(img)
    w=len(img[0])
    count=1
    print('Скелетизация ...')
    while count!=0: #повторять пок удалялся хотя бы один пиксель
        count=delete(img,w,h)
        if count:
            delete2(img,w,h)


def delete(img,w,h): #удаление пикселя по основному набору, возврат кол-ва удаленных
    count=0
    for i in range(1,h-1):
        for j in range(1,w-1):
            if img[i,j]==0:
                if deletable(img,i,j):
                    img[i,j]=1
                    count+=1
    return count


def delete2(img, w, h):  # удаление пикселя по шумовому набору
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            if img[i,j] == 0:
                if deletable2(img, i, j):
                    img[i,j] = 1


def fringe(a):  # определение принадлежности 3*3 к шумам
    t = [[1, 1, 1, 1, 0, 1, 1, 1, 1],

         [1, 1, 1, 1, 0, 1, 1, 0, 0],
         [1, 1, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 1, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 1],

         [1, 1, 1, 1, 0, 1, 0, 0, 1],
         [0, 1, 1, 0, 0, 1, 1, 1, 1],
         [1, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 0],

         [1, 1, 1, 1, 0, 1, 0, 0, 0],
         [0, 1, 1, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 0, 1, 0, 0, 1, 1, 0]]
    for i in t:
        if a == i:
            return True


def check(a):  # определение принадлежности 3*3 к основным шаблонам
    t123457 = [1, 1, 0, 0, 1, 0]
    t013457 = [1, 1, 1, 0, 0, 0]
    t134567 = [0, 1, 0, 0, 1, 1]
    t134578 = [0, 0, 0, 1, 1, 1]
    t0123457 = [1, 1, 1, 0, 0, 0, 0]
    t0134567 = [1, 0, 1, 0, 0, 1, 0]
    t1345678 = [0, 0, 0, 0, 1, 1, 1]
    t1234578 = [0, 1, 0, 0, 1, 0, 1]

    t = [a[1], a[2], a[3], a[4], a[5], a[7]]
    if t == t123457:
        return True
    t = [a[0], a[1], a[3], a[4], a[5], a[7]]
    if t == t013457:
        return True
    t = [a[1], a[3], a[4], a[5], a[6], a[7]]
    if t == t134567:
        return True
    t = [a[1], a[3], a[4], a[5], a[7], a[8]]
    if t == t134578:
        return True
    t = [a[0], a[1], a[2], a[3], a[4], a[5], a[7]]
    if t == t0123457:
        return True
    t = [a[1], a[3], a[4], a[5], a[6], a[7], a[8]]
    if t == t1345678:
        return True
    t = [a[0], a[1], a[3], a[4], a[5], a[6], a[7]]
    if t == t0134567:
        return True
    t = [a[1], a[2], a[3], a[4], a[5], a[7], a[8]]
    if t == t1234578:
        return True


def deletable(img, y, x):  # получение 3*3, передача на проверку для осн.
    a = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            a.append(img[i,j])
    return check(a)


def deletable2(img, y, x):  # получение 3*3, передача на проверку для шумов
    a = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            a.append(img[i,j])
    return fringe(a)