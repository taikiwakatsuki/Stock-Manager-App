import wx
import wx.lib.scrolledpanel as scrolled
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import datetime
import password_setting


date = datetime.date.today()
data = pd.read_csv("Data.csv")
names = data["物資名"]
TorF = data["TorF"]
checkbox = []
ideal_value = data["理想量"]
value = data["現在の量"]



class Top(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム")



        # フレーム
        self.SetSize((1000,700))
        self.SetBackgroundColour((207,207,207))
        self.Center()



        # メニューバー
        self.menu_bar = wx.MenuBar()
        self.setting = wx.Menu()
        self.setting.Append(1,"物資の追加・削除")
        self.setting.Append(2,"理想量の変更")
        self.setting.Append(3,"パスワードの変更")

        self.developertool = wx.Menu()
        self.developertool.Append(4,"1")

        self.menu_bar.Append(self.setting,"設定")
        self.menu_bar.Append(self.developertool,"デベロッパーツール")

        self.SetMenuBar(self.menu_bar)

        # self.Bind(wx.EVT_MENU, self.clicked)



        # Notebook設定
        self.notebook = wx.Notebook(self,wx.ID_ANY,style=wx.NB_TOP)



        # 現在の在庫状況
        self.panel_home = wx.Panel(self.notebook,wx.ID_ANY)
        self.panel_home_left = scrolled.ScrolledPanel(self.panel_home,-1,pos=(0,0),size=(300,600))
        self.panel_home_right = scrolled.ScrolledPanel(self.panel_home,-1,pos=(300,0),size=(680,600))
        self.panel_home_left.SetupScrolling()
        self.panel_home_right.SetupScrolling()
        self.layout_left = wx.BoxSizer(wx.VERTICAL)
        self.layout_right = wx.BoxSizer(wx.VERTICAL)

        counts = 0
        for name in names:
            checkbox_tmp = wx.CheckBox(self.panel_home_left,wx.ID_ANY,str(name))
            if TorF[counts] == True:
                checkbox_tmp.SetValue(True)
            else:
                checkbox_tmp.SetValue(False)
            checkbox.append(checkbox_tmp)
            self.layout_left.Add(checkbox_tmp)
            counts += 1

        counts = 0
        for checked in checkbox:
            self.torf = checked.GetValue()
            if self.torf == True:
                plt.rcParams["ytick.direction"] = "in"
                self.fig = Figure(figsize=(6,1),facecolor=(0.81,0.81,0.81))
                self.fig.suptitle(str(names[counts]),fontname="Hiragino sans",fontsize=8)
                self.ax = self.fig.add_subplot(111)
                self.fig.subplots_adjust(bottom=0.7,top=0.8)
                self.ax.set_xlim(0,1.0)
                self.ax.set_xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
                self.ax.set_xticklabels(["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
                self.ax.set_ylim(0,1)
                self.ax.set_yticks([0.5])
                self.ax.set_yticklabels([""])
                x = [0.5]
                y = value[counts] / ideal_value[counts]
                self.ax.barh(x,y,align="center")
                self.canvas = FigureCanvas(self.panel_home_right,-1,self.fig)
                self.layout_right.Add(self.canvas)
                self.layout_right.Layout()
            counts += 1

        self.Bind(wx.EVT_CHECKBOX,self.checked)

        self.panel_home_left.SetSizer(self.layout_left)
        self.panel_home_right.SetSizer(self.layout_right)

        self.notebook.InsertPage(0,self.panel_home, "現在の在庫状況")



        # 発注
        self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)
        self.panel_hacchu_center = scrolled.ScrolledPanel(self.panel_hacchu,-1,pos=(300,0),size=(680,600))
        self.panel_hacchu_center.SetupScrolling()
        self.layout_hacchu = wx.BoxSizer(wx.VERTICAL)

        self.notebook.InsertPage(1,self.panel_hacchu, "本日の発注")



        # 過去のデータ
        self.panel_kakonodata = wx.Panel(self.notebook,wx.ID_ANY)
        self.notebook.InsertPage(2,self.panel_kakonodata, "過去のデータ")



        # 今後の発注数
        self.panel_syouhidouko = wx.Panel(self.notebook,wx.ID_ANY)
        self.notebook.InsertPage(3,self.panel_syouhidouko, "今後の発注数")



        # 表示
        self.Show()



    # チェックボックスにチェックをした時の画面変化
    def checked(self,event):
        self.layout_right.Clear(True)
        counts = 0
        for checked in checkbox:
            self.torf = checked.GetValue()
            if self.torf == True:
                plt.rcParams["ytick.direction"] = "in"
                self.fig = Figure(figsize=(6,1),facecolor=(0.81,0.81,0.81))
                self.fig.suptitle(str(names[counts]),fontname="Hiragino sans",fontsize=8)
                self.ax = self.fig.add_subplot(111)
                self.fig.subplots_adjust(bottom=0.7,top=0.8)
                self.ax.set_xlim(0,1.0)
                self.ax.set_xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
                self.ax.set_xticklabels(["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
                self.ax.set_ylim(0,1)
                self.ax.set_yticks([0.5])
                self.ax.set_yticklabels([""])
                x = [0.5]
                y = value[counts] / ideal_value[counts]
                self.ax.barh(x,y,align="center")
                self.canvas = FigureCanvas(self.panel_home_right,-1,self.fig)
                self.layout_right.Add(self.canvas)
                self.layout_right.Layout()
            counts += 1
            self.panel_home_right.SetupScrolling()



    # メニューバーがクリックされた時
    # def clicked(self,event):
    #     event_id = event.GetID()
    #     if event_id == 1:
    #         password_setting.Password_setting()
