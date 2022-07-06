import ctypes
Num = 1
Bg_Name=Num + ".jpg"
ctypes.windll.user32.SystemParameInfoW(20,0,Bg_Name,0)

