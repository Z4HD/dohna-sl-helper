import logging
import re
import tkinter as tk
from tkinter import messagebox as msgbox
from tkinter import ttk

from pyautogui import FailSafeException, ImageNotFoundException, Point

from . import __version__
from .automatic import AutoActions, findGamePosition

logger = logging.getLogger('dsh.ui')


class App(ttk.Frame):
    def __init__(self, master=None, scaleFactor: int = 0):
        # init base window
        super().__init__(master)
        logger.info('start INIT')
        self.master.title(f'DSH {__version__}')
        self.master.resizable(False, False)
        if scaleFactor:
            self.master.tk.call('tk', 'scaling', scaleFactor / 72)
        # set up vars
        self.xInt = tk.IntVar(self, value=0)
        self.yInt = tk.IntVar(self, value=0)
        self.autoLoadBool = tk.BooleanVar(self, value=True)
        self.enterSellBool = tk.BooleanVar(self, value=False)
        # set up validation command
        self._vcmd = (self.register(intValidation), '%P')
        # set up widgets
        self.grid(padx=10, pady=10)
        self._widgets()

    def _widgets(self):
        "Put wedgets into main frame"
        # LF1: Game position
        self.fpLF1 = ttk.Labelframe(self, text="Game position")
        self.fpLF1.grid(row=0, column=0, ipadx=5, ipady=5, padx=5, pady=5)
        self.findGameBtn = ttk.Button(self.fpLF1,
                                      text="① Find game position",
                                      command=self.findGamePositionCommand)
        self.findGameBtn.grid(row=0, column=1, padx=5, pady=5)
        self.gPLx = ttk.Label(self.fpLF1, text="x:")
        self.gPLx.grid(row=1, column=0, sticky='E')
        self.gPLy = ttk.Label(self.fpLF1, text="y:")
        self.gPLy.grid(row=2, column=0, sticky='E')
        self.gPETx = ttk.Entry(self.fpLF1, textvariable=self.xInt)
        self.gPETx.config(validate='key', validatecommand=self._vcmd)
        self.gPETx.grid(row=1, column=1, padx=5, pady=5)
        self.gPETy = ttk.Entry(self.fpLF1, textvariable=self.yInt)
        self.gPETy.config(validate='key', validatecommand=self._vcmd)
        self.gPETy.grid(row=2, column=1, padx=5, pady=5)

        # FL2: Actions
        self.fpLF2 = ttk.Labelframe(self, text="Actions")
        self.fpLF2.grid(row=1, column=0, padx=5, pady=5)
        self.autoLoadChkB = ttk.Checkbutton(
            self.fpLF2,
            text="Auto load first slot savedata",
            command=self.autoLoadChkBCommand,
            variable=self.autoLoadBool)
        self.autoLoadChkB.grid(row=0, column=0, padx=5, pady=5, sticky='W')
        self.enterSaleChkB = ttk.Checkbutton(self.fpLF2,
                                             text="Auto enter sale action",
                                             variable=self.enterSellBool)
        self.enterSaleChkB.grid(row=1, column=0, padx=5, pady=5, sticky='W')

        # Final step: RUN
        self.runBtn = ttk.Button(self.fpLF2,
                                 text="② Run SL!",
                                 command=self.runBtnCommand)
        self.runBtn.grid(row=2, column=0, padx=5, pady=5)

    def _disableBtns(self):
        self.findGameBtn.config(state='disabled')
        self.runBtn.config(state='disabled')

    def _enableBtns(self):
        self.findGameBtn.config(state='normal')
        self.runBtn.config(state='normal')

    def findGamePositionCommand(self):
        self._disableBtns()
        try:
            point = findGamePosition()
        except ImageNotFoundException:
            msgbox.showerror(
                'Fuck!',
                'Could not find dohna:dohna game.\n Make sure you can see the game on your screen.'
            )
            self._enableBtns()
            return
        self.xInt.set(point.x)
        self.yInt.set(point.y)
        self._enableBtns()

    def runBtnCommand(self):
        self._disableBtns()
        try:
            if self.xInt.get() == 0 or self.yInt.get() == 0:
                i = msgbox.askyesno(
                    'Position warning',
                    'Game position is (0,0), may be you forget get game position.\nContinue anyway?'
                )
                if not i:
                    raise ValueError('Wrong game position')
            gP = Point(self.xInt.get(), self.yInt.get())
            ac = AutoActions(gP)
            ac.returnToTitle()
            ac.enterLoadSaveScreen()
            if self.autoLoadBool.get():
                ac.loadFirstSaveData()
                if self.enterSellBool.get():
                    ac.enterSaleAction()
        except FailSafeException:
            msgbox.showerror('PyAutoGUI',"PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen.\nAction stop.")
        finally:
            self._enableBtns()

    def autoLoadChkBCommand(self):
        if self.autoLoadBool.get():
            #self.enterSellBool.set(False)
            self.enterSaleChkB.config(state='normal')
        else:
            self.enterSellBool.set(False)
            self.enterSaleChkB.config(state='disabled')


def intValidation(vstr: str) -> bool:
    "match a str is contain int"
    if re.match("^\d*$", vstr):
        return True
    else:
        return False
