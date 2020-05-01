from PIL import Image
import math
import cv2
import time
def get_Image():
    while True:
        try:
            inputFile = input("Enter image name to shade: ")
            File = open(inputFile)
        except IOError:
            print('Could not find file')
            print('-------------------')
            continue
        else:
            break
    return inputFile
def usePIL():
    img = Image.open(get_Image())
    pix = img.load()
    totx, toty = img.size
    
    for x in range(totx):
        for y in range(toty):
            pix[x,y]=calculate_closest_color(pix[x,y])
    img.save('completed.png')
def usecv2():
    img = cv2.imread(get_Image())
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    totx = img.shape[0]
    toty = img.shape[1]
    for x in range(totx):
        for y in range(toty):
            img[x,y]=calculate_closest_color(img[x,y])
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)    
    cv2.imwrite('completed.png', img) 
def create_color_pallet_from_image():
    while True:
        try:
            inputFile = input("Enter color pallet file: ")
            File = open(inputFile)
        except IOError:
            print('Could not find file')
            print('-------------------')
            continue
        else:
            break
    return inputFile
def create_color_pallet():
    img = Image.open(create_color_pallet_from_image())
    pix = img.load()
    totx, toty = img.size

    inputFile = open('color_pallet.txt','w')
    arr = []
    for x in range(totx):
        for y in range(toty):
            if pix[x,y] not in arr:
                inputFile.write(str(pix[x,y])[1:-1]+'\n')
                arr.append(pix[x,y])
def get_color_pallet():
    while True:
        try:
            inputFile = open('color_pallet.txt')
        except IOError:
            print('Could not find file')
            print('-------------------')
            continue
        else:
            break
    return [(int(line.split(',')[0]),int(line.split(',')[1]),int(line.split(',')[2])) for line in inputFile]
def calculate_closest_color(pixel):
    minMagnitude = 10000
    closestColor = pallet[0]
    for color in pallet:
        magnitude = math.sqrt(pow(abs(color[0]-pixel[0]),2)+pow(abs(color[1]-pixel[1]),2)+pow(abs(color[2]-pixel[2]),2))
        if  magnitude < minMagnitude:
            minMagnitude = magnitude
            closestColor = color
    return closestColor
create_color_pallet()
pallet = get_color_pallet()


#last_time = time.time()
#usecv2()
#print('cv2 took {} seconds'.format(time.time()-last_time))
last_time = time.time()
usePIL()
print('PIL took {} seconds'.format(time.time()-last_time))
