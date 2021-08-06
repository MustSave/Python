import find_image as fi
import GetMousePoint as fp
import pyautogui as pa
import time
import random
from init_config import *

def findImgAndPressKey(imgName, key, startPos, cnt=60, confidence=.8, wait=0.1):
    posBtn = fi.findImageUntil(imgName, startPos=startPos, cnt=cnt, confidence=confidence, wait=wait)
    if posBtn == None:
        return False
    else:
        pa.press(key)
        return True

def fishingLostArk(wait, setPos=1, fishingKey='w'):
    fishingFailCnt = 0
    posList = []

    if setPos == 0:
        posList = fp.getMousePointWithKey(3)
    else:
        posList = fp.getFishingPointList()
        print('point of init : ', str(posList))
    
    width = FISHING_WIDTH
    height = FISHING_HEIGHT

    while True:
        if fishingFailCnt > 20:
            print("Fishing Too Mush Fail")
            return
            
        if len(posList) > 0:
            idx = random.randrange(0, len(posList))
            pa.moveTo(posList[idx][0], posList[idx][1], 1)
        else:
            print("Can't get fishing point")
            return
        
        pa.press(fishingKey)
        time.sleep(1)

        region = fi.makeRegion(fi.getCenterOfScreen(), width, height)

        res = findImgAndPressKey(FISHING_EXCLAMATION_MARK_IMG_NAME, fishingKey, startPos=region, cnt=FISHING_EXCLAMATION_MARK_DETECT_CNT, confidence=0.8, wait=0.1)
        if res == True:
            print('Fishing Success')
            #time.sleep(wait)
            time.sleep(random.randrange(2,5))
            if fishingFailCnt > 0:
                fishingFailCnt -= 1
        else:
            print('fishing Fail')
            fishingFailCnt += 1
            time.sleep(2)
        
if __name__ == "__main__":
    fishingLostArk(FISHING_WAIT_TIME, setPos=1, fishingKey='w')