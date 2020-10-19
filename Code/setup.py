
import sys
from cx_Freeze import setup, Executable

includes = ["matplotlib","pandas","wx","datetime","hashlib","Crypto.PublicKey","Crypto.Cipher","pickle","webbrowser","wx.lib.scrolledpanel","matplotlib.pyplot","matplotlib.backends.backend_wxagg","matplotlib.backends.backend_wx","matplotlib.figure"]

icon = "icon.ico"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Stock Manager",
        # version = "",
        options = {"build_exe": {"includes": includes}},
        executables = [Executable("StockManager.py", base=base ,icon=icon)])
