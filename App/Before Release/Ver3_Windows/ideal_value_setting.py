import wx
import pandas as pd


data = pd.read_csv("Data.csv")
names = data["物資名"]
ideal_value = data["理想量"]
element_array = []


class Ideal_value_setting(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"理想量の変更")



        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()




        # パネル
        self.ideal_value_setting_panel = wx.Panel(self)



        for name in names:
            element_array.append(str(name))
        self.combobox = wx.ComboBox(self.ideal_value_setting_panel,wx.ID_ANY,choices=element_array,style=wx.CB_READONLY,pos=(100,50),size=(200,50))



        # ボタン
        self.button_ideal_value_setting = wx.Button(self.ideal_value_setting_panel,-1,"設定",pos=(150,100),size=(100,20))
        self.button_ideal_value_setting.SetForegroundColour((0,0,0))
        self.button_ideal_value_setting.Bind(wx.EVT_BUTTON,self.clicked_button_ideal_value_setting)



        # 表示
        self.Show()



    # ボタンをクリックした時
    def clicked_button_ideal_value_setting(self,event):
        counter = 0
        for name in names:
            if name == self.combobox.GetValue():
                self.counts = counter
            counter += 1
        self.statictext_ideal_value_setting = wx.StaticText(self.ideal_value_setting_panel,wx.ID_ANY,"現在の理想量は「" + str(ideal_value[self.counts]) + "」です。新しい理想量を入力してください。",pos=(60,200),size=(400,50))
        self.textctrl_ideal_value_setting = wx.TextCtrl(self.ideal_value_setting_panel,pos=(120,250),size=(50,20))
        self.button_newideal_value_setting = wx.Button(self.ideal_value_setting_panel,-1,"変更",pos=(180,250),size=(100,20))
        self.button_newideal_value_setting.SetForegroundColour((0,0,0))
        self.button_newideal_value_setting.Bind(wx.EVT_BUTTON,self.clicked_button_newideal_value_setting)



    # ボタンをクリックした時
    def clicked_button_newideal_value_setting(self,event):
        ideal_value[self.counts] = self.textctrl_ideal_value_setting.GetValue()
        data.to_csv("Data.csv")
        self.Destroy()
