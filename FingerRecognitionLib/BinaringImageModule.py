import numpy as np


def binary(img):
    #Топорный алгоритм, но более быстрый
    #Не подходит для изображений с большим количеством шума
    N = img.size[1]*img.size[0]
    per = N/100
    it = 0
    bImg=np.empty(shape=(img.size[1],img.size[0]))
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            t=img.getpixel((j,i))
            #p=t[0]*0.3+t[1]*0.59+t[2]*0.11
            p=t
            if p>128:
                p=1
            else:
                p=0
            bImg[i,j]=p
            it+=1
        print("Бинаризация : %f %%" % (it/per))

    return bImg


def Bradley_Rot(img):
    #Более тонкий алгоритм, но более затратный по ресурсам
    #Справляется со всеми примерами БД
    width = img.size[0]
    height = img.size[1]
    integral_image = np.empty(shape=(height,width))
    S = height//8
    s2 = S//2
    t_const = 0.15


    # рассчитываем интегральное изображение
    for i in range(height):
        sum=0.
        for j in range(width):
            t = img.getpixel((j, i))
            if type(t) == type(int()):
                sum +=t
            else:
                sum += t[0] * 0.3 + t[1] * 0.59 + t[2] * 0.11
            if i==0:
                integral_image[i,j] = sum
            else:
                integral_image[i,j] = integral_image[i-1,j] + sum

    res = np.empty(shape=(height,width))
    # находим границы для локальные областей
    for i in range(height):
        for j in range(width):
            x1 = i - s2
            x2 = i + s2
            y1 = j - s2
            y2 = j + s2

            if (x1 < 0):
                x1=0
            if (x2>=height):
                x2 = height-1
            if (y1<0):
                y1 = 0
            if (y2>=width):
                y2 = width-1

            count = (x2-x1)*(y2-y1)
            try:
                sum = integral_image[x2, y2] - integral_image[x2,y1] \
                      - integral_image[x1,y2] + integral_image[x1,y1]
            except:
                print(((x1,y1), (x2,y2)))
                continue

            t = img.getpixel((j, i))
            if type(t) == type(int()):
                scr = t
            else:
                scr = t[0] * 0.3 + t[1] * 0.59 + t[2] * 0.11
            if (scr * count < sum * (1.0-t_const)):
                res[i,j] = 0
            else:
                res[i,j] = 1

    return res


