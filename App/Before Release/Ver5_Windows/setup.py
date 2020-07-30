# from distutils.core import setup
# import py2exe
#
# option = {
#     'bundle_files':1,
#     'compressed': True
#     # 'compressed': False
# }
# setup(
#     options = {'py2exe': option},
#     console=['main.py'],
#     zipfile = 'main.zip',
#     )


# ---------------------------------------


# import sys, os
# from cx_Freeze import setup, Executable
#
# #個人的な設定（コマンドライン上でファイルをぶっこみたい）
# file_path = input("main.py")
#
# #TCL, TKライブラリのエラーが発生する場合に備え、以下を設定
# #参考サイト：http://oregengo.hatenablog.com/entry/2016/12/23/205550
# if sys.platform == "win32":
#     base = None # "Win32GUI" ←GUI有効
#     #Windowsの場合の記載　それぞれの環境によってフォルダの数値等は異なる
#     os.environ["TCL_LIBRARY"] = "C:\\ユーザー\\perio\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tcl8.6"
#     os.environ["TK_LIBRARY"] = "C:\\ユーザー\\perio\\AppData\\Local\\Programs\\Python\\Python36\\tcl\\tk8.6"
# else:
#     base = None # "Win32GUI"
#
# #importして使っているライブラリを記載
# # packages = []
#
# #importして使っているライブラリを記載（こちらの方が軽くなるという噂）
# includes = ["matplotlib","pandas","wx","datetime","hashlib","Crypto.PublicKey","Crypto.Cipher","pickle","webbrowser","wx.lib.scrolledpanel","matplotlib.pyplot","matplotlib.backends.backend_wxagg","matplotlib.backends.backend_wx","matplotlib.figure"]
#
# #excludesでは、パッケージ化しないライブラリやモジュールを指定する。
# # """
# # numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
# # 他にも、PIL(5MB)など。
# # """
# excludes = []
#
# ##### 細かい設定はここまで #####
#
# #アプリ化したい pythonファイルの指定触る必要はない
# exe = Executable(
#     script = file_path,
#     base = base
# )
#
# # セットアップ
# setup(name = "main",
#       options = {
#           "build_exe": {
#               # "packages": packages,
#               "includes": includes,
#               "excludes": excludes
#           }
#       },
#       version = "0.1",
#       description = "converter",
#       executables = [exe]
#       )


# ----------------------------------------


import sys
from cx_Freeze import setup, Executable

includes = ["matplotlib","pandas","wx","datetime","hashlib","Crypto.PublicKey","Crypto.Cipher","pickle","webbrowser","wx.lib.scrolledpanel","matplotlib.pyplot","matplotlib.backends.backend_wxagg","matplotlib.backends.backend_wx","matplotlib.figure"]

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "main",
        # version = "",
        options = {"build_exe": {"includes": includes}},
        executables = [Executable("main.py", base=base)])
