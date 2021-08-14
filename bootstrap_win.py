import ctypes

from dohna_sl_helper.ui import App

#HDPI START
try:  # >= win 8.1
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:  # win 8.0 or less
    ctypes.windll.user32.SetProcessDPIAware()

ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
# HDPI END

app = App(scaleFactor=ScaleFactor)

app.mainloop()
