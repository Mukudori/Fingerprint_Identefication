from PIL import Image
import numpy as np
import matplotlib as plt

def resizeImage(img, toWidth = 100):
    wpercent = (toWidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((toWidth, hsize), Image.ANTIALIAS)
    return img

def saveBinImageFromArray(ar, name, _shape=0):
    if _shape:
        newar = np.ones(shape=_shape)
        for p in ar[0]:
            newar[p[0], p[1]] = 0
    else:
        newar = ar


    imS = getImageFromArray(newar)
    imS.save(name)

def getImageFromArray(ar):
    im = Image.fromarray(np.uint8(plt.cm.gist_earth(ar) * 255))
    return im

def saveImageFromCP(cp, name, _shape):
    num = 0
    for ar in cp:
        newar = np.ones(shape= _shape)
        for p in ar:
            newar[p[0],p[1]] = 0
        imS = getImageFromArray(newar)
        imS.save(name%num)
        num+=1

def cutFingerFill(ar):
    left = 0
    right = 0
    up = 0
    down = 0
    border = 15
    n, m = ar.shape


    f= False
    for j in range(border,m-border):
        for i in range(border,n-border):
            if not ar[i,j] and not ar[i,j+1] and not ar[i,j+2]:
                left = j
                f = True
                break
        if f:
            break

    f = False
    for j in reversed(range(border,m-border)):
        for i in range(n)[border:n-border]:
            if not ar[i,j] and not ar[i,j-1] and not ar[i,j-2]:
                right = j
                f = True
                break
        if f:
            break
    f=False
    for i in range(border,n-border):
        for j in reversed(range(border,m-border)):
            if not ar[i,j] and not ar[i+1,j] and not ar[i+2,j]:
                up=i
                f = True
                break
        if f:
            break

    f = False
    for i in reversed(range(border,n - border)):
        for j in reversed(range(border,m - border)):
            if not ar[i,j] and not ar[i-1,j] and not ar[i-2,j]:
                down = i
                f = True
                break
        if f:
            break
    nn = down-up
    nm = right-left
    newAr = np.empty(shape=(nn,nm))
    ni=0
    for i in range(up,down):
        nj=0
        for j in range(left,right):
            newAr[ni,nj] = ar[i,j]
            nj+=1
        ni+=1

    return newAr










