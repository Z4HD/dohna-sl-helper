import logging
import os.path
import sys
import time

import pyautogui as pa

logger = logging.getLogger('dsh.AutoAction')

pa.PAUSE = 0.5
pa.FAILSAFE = True

if getattr(sys, 'frozen', False):  # In PyInstaller binary
    basedir = sys._MEIPASS # pylint: disable=no-member
else: # normal
    basedir = os.path.abspath('.')

def sleep(secs:float):
    logger.debug(f"Wait {secs} seconds...")
    time.sleep(secs)

def findGamePosition() -> pa.Point:
    """
    Get Game left-right position by pre-define image.

    Returns:
        pyautogui.Point: (x,y)
    """
    p_path = os.path.abspath(os.path.join(basedir, 'pic/game-icon.jpg'))
    r = pa.locateCenterOnScreen(p_path, confidence=0.9, grayscale=True)
    if not r:
        raise pa.ImageNotFoundException()
    pa.moveTo(r.x, r.y)
    logger.info('Successful get game position.')
    return r


class AutoActions():
    def __init__(self, gamePosition: pa.Point):
        self.gamePosition = gamePosition

    def initMousePosition(self):
        pa.moveTo(*self.gamePosition)

    def _clickRel(self, x: int, y: int):
        """
        Click the point relative to base position.

        Args:
            x (int): x offset
            y (int): y offset
        """
        self.initMousePosition()
        pa.moveRel(x, y)
        pa.click()

    def returnToTitle(self):
        #系统：10,35
        #标题画面：60,93
        logger.info('Start action: returnToTitle')
        # click 系统
        self._clickRel(10, 35)
        # click 标题画面
        self._clickRel(60, 93)
        pa.press('enter')
        sleep(5)
        logger.info('END action: returnToTitle')

    def enterLoadSaveScreen(self):
        #5,195
        logger.info('Start action: enterLoadSaveScreen')
        self._clickRel(5, 195)
        sleep(1)
        logger.info('END action: enterLoadSaveScreen')

    def loadFirstSaveData(self):
        logger.info('Start action: loadFirstSaveData')
        self._clickRel(25, 175)
        sleep(7)
        logger.info('END action: loadFirstSaveData')


    def enterSaleAction(self):
        "从游戏据点界面进入春销界面"
        logger.info('Start action: loadFirstSaveData')
        #1165,720
        self._clickRel(1165, 720)
        #sleep(1)
        #440,470
        self._clickRel(440, 470)
        logger.info('END action: loadFirstSaveData')
