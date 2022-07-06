import ctypes
Num = 1
Bg_Name=str(Num) + ".jpg"
ctypes.windll.user32.SystemParametersInfoW(20,0,Bg_Name,0)

