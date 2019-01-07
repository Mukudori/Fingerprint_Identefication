
from PIL import Image
from FingerRecognitionLib import BinaringImageModule as BIM, Skeletization as SK, MaitchingPoints as MP, \
    SinglingPoints as SP, ImageProcessing as IP
import  os
from math import sqrt, pow


def writeMat(mat, h, w):
    '''Запись массива в текстовый файл'''
    f = open('out.txt', 'w')
    sum=0
    for i in range(w):
        outS = str()
        for j in range(h):
            outS+= ' '+str(mat[i, j])
            if mat[i,j]!=1:
                sum+=1
        f.write(outS + '\n')
    f.close();
    print(sum)

def recognition(url,num=0):
    '''Выделение особых точек на изображении'''
    name = url.split('/')[-1].split('.')[0]
    folderBin = './images/%s_bin.png'
    folderSkelet = './images/%s_skelletization.png'
    folderCheck  = './images/%s_checkPoint'
    folderDelNoices = './images/%s_delNoices'
    img = Image.open(url)

    #Бинаризация
    bin = BIM.Bradley_Rot(img)
    bin = IP.cutFingerFill(bin)
    height,width = bin.shape
    IP.saveBinImageFromArray(bin, folderBin %name)

    #Скелетизация
    SK.tmpDelete(bin)
    IP.saveBinImageFromArray(bin, folderSkelet%name)

    #Поиск точек
    cp = SP.findCheckPoint(bin, num)
    IP.saveImageFromCP(cp, (folderCheck % name) + '_%i.png', _shape=(height, width))

  #  cp = SP.delNoisePoint(cp)
    #IP.saveImageFromCP(cp, (folderDelNoices % name) + '_%i.png', _shape=(height, width))
    return cp

def binnaringImages():
    for filename in os.listdir('./data/db/3/'):
        img = Image.open('./data/db/3/'+filename)
        bin = BIM.Bradley_Rot(img)
        saveName = './images/bins/%s.png' % filename.split('.')[0]
        IP.saveBinImageFromArray(bin, saveName)
        print('Сохранено : saveName')

def evklid():
    etalon = {'131_1' : ((77, 124),
                         (123,102),
                         (138,29),
                         (92,182),
                         (121,189),
                         (133,109),
                         (241,132)),
              '132_5' : ((173,269),
                         (200,268),
                         (158,239),
                         (213,215),
                         (142,204),
                         (84,175),
                         (203,163),
                         (161,95),
                         (178,74),
                         (101,56),
                         (261,158),
                         (125,36),
                         (65,54),
                         (222,59),
                         (104,56),
                         (48,82),
                         (84,235),
                         (118,277)
                         )
              }
    name = '132_5'
    cp1 = recognition('./data/db/3/%s.tif'%name)[0]
    all=0
    check_15 =0
    check_30 = 0
    check_ = 0
    for p1 in cp1:
        k_ = 0
        for p2 in etalon[name]:
            d = sqrt(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2))

            if d<=15:
                check_15+=1
                k_=0
                break
            elif d<= 30:
                check_30+=1
                k_=0
                break
            else:
                k_+=1

        if k_:
            check_+=1

    print('15 - %f%%' % (check_15/len(cp1)))
    print('30 - %f%%' % (check_30 / len(cp1)))
    print('Больше - %f%%' % (check_/len(cp1)))
    print('len - %i' % (len(cp1)))

def testCut(url):
    """Проверка метода, отсекающего лишний шум"""
    img = Image.open(url)
    bin = BIM.Bradley_Rot(img)
    newBin = IP.cutFingerFill(bin)
    IP.saveBinImageFromArray(newBin, 'testCut.png')

def compareRecognition(url_1, url_2):
    folder = './images'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)

    cp1 = recognition(url_1, 1)
    cp2 = recognition(url_2, 2)
    res, p1, p2 = MP.matchingPoint(cp1, cp2)
    print('\nВерификация завершена.')
    print('Совпадений = %i' % res[0])
    print('Всего итераций = %i' % res[1])
    if len(cp1[0]):
        print('1 len = %i : %% %f' % (len(cp1[0]), p1))
        if len(cp2[0]):
            print('2 len = %i : %% %f' % (len(cp2[0]), p2))
            print('Усредненное совпадение : %% %f' % ((p1 + p2) / 2))
        else:
            print('У второго отпечатка точки не найдены')
    else:
        print('У первого отпечатка точки не найдены')


if __name__ == '__main__':
    compareRecognition('./data/db/1/101_2.tif', './data/db/1/101_4.tif')




