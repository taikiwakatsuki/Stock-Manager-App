import wx
import pandas as pd
import wx.lib.scrolledpanel as scrolled


class Help(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"ヘルプ")




        # フレーム
        self.SetSize((500,600))
        self.SetBackgroundColour((207,207,207))
        self.Center()




        # パネル
        self.panel_help = wx.Panel(self)
        self.panel_help_scroll = scrolled.ScrolledPanel(self.panel_help,-1,pos=(0,0),size=(500,600))
        self.panel_help_scroll.SetupScrolling()



        # 説明
        self.help_text = "ヘルプ"
        self.statictext_help = wx.StaticText(self.panel_help_scroll,-1,self.help_text,pos=(0,0),size=(500,1000))



        # 表示
        self.Show()
