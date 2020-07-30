import wx
import pandas as pd


class Info(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"情報")




        # フレーム
        self.SetSize((400,220))
        self.SetBackgroundColour((207,207,207))
        self.Center()




        # パネル
        self.panel_info = wx.Panel(self)




        # 情報
        self.statictext_info_tmp1 = wx.StaticText(self.panel_info,-1,"")
        self.statictext_info_version = wx.StaticText(self.panel_info,-1,"Version1.0",style=wx.TE_CENTER)
        self.statictext_info_tmp2 = wx.StaticText(self.panel_info,-1,"")
        self.statictext_info_release_date = wx.StaticText(self.panel_info,-1,"Release 2020/00/00",style=wx.TE_CENTER)
        self.statictext_info_update_date = wx.StaticText(self.panel_info,-1,"Update 2020/00/00",style=wx.TE_CENTER)
        self.statictext_info_tmp3 = wx.StaticText(self.panel_info,-1,"")
        self.statictext_info_enviroment = wx.StaticText(self.panel_info,-1,"Windows10")
        self.statictext_info_language = wx.StaticText(self.panel_info,-1,"Python3.7.4")
        self.statictext_info_library = wx.StaticText(self.panel_info,-1,"（matplotlib,pandas,wxPython）")
        self.font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.statictext_info_version.SetFont(self.font)


        self.layout_info = wx.BoxSizer(wx.VERTICAL)
        self.layout_info.Add(self.statictext_info_tmp1,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_version,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_tmp2,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_release_date,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_update_date,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_tmp3,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_enviroment,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_language,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_library,flag=wx.GROW)
        self.panel_info.SetSizer(self.layout_info)



        # 表示
        self.Show()
