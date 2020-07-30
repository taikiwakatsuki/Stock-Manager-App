import wx
import pandas as pd


class Add_and_delete(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"物資の追加・削除")




        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()




        # パネル
        self.panel_add_and_delete = wx.Panel(self)
