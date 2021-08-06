import os
import time
import sys
import pyautogui as pa
import configparser

# -모니터 화면의 중앙 좌표 리턴
def getCenterOfScreen():
    tup = pa.size()
    tup = (int(tup[0]/2), int(tup[1]/2))
    return tup

# -검출 영역 지정
def makeRegion(center, width, height):
    x = center[0]
    y = center[1]

    startPos = (x - width, y - height)
    region = (startPos[0], startPos[1], 2*width, 2*height)
    return region

def findLocationWithImage(fileName, startPos, confidence=.7):
    file_path = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'img' + '\\' + fileName
    result = pa.locateOnScreen(file_path, confidence=confidence, region=startPos)

    sys.stdout.write('. ')
    sys.stdout.flush()
    if result != None:
        print('Find Image ' + str(result))
    return result

def findImageUntil(fileName, startPos, cnt=60, confidence=0.8, wait=0.1):
    for i in range(cnt):
        imgpos = findLocationWithImage(fileName, startPos, confidence=confidence)
        if imgpos != None:
            break
        else:
            time.sleep(wait)
    
    if imgpos == None:
        return None
    else:
        return imgpos

if __name__ == "__main__":
    configFile = os.path.dirname(os.path.realpath(__file__)) + '\\' + 'init.txt'
    config = configparser.ConfigParser()
    config.read(configFile)

    width = int(config['lostark_fishing']['width'])
    height = int(config['lostark_fishing']['height'])

    region = makeRegion(getCenterOfScreen(), width, height)
    
    #Filename = "LA_exclamation_mark.png"
    Filename = "Folder.png"
    findImageUntil(Filename, region, cnt=60, confidence=0.8)
