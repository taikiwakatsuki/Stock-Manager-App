import wx
import wx.lib.scrolledpanel as scrolled
import pandas as pd



data = pd.read_csv("物資名.csv")
names = data["名前"]
checkbox = []
panel = []



class Top(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム")



        # フレーム
        self.SetSize((1000,700))
        self.SetBackgroundColour((207,207,207))
        self.Center()



        # Notebook設定
        self.notebook = wx.Notebook(self,wx.ID_ANY,style=wx.NB_TOP)



        # 現在の在庫状況
        self.panel_home = wx.Panel(self.notebook,wx.ID_ANY)
        self.panel_home_left = scrolled.ScrolledPanel(self.panel_home,-1,pos=(0,0),size=(300,600))
        self.panel_home_right = scrolled.ScrolledPanel(self.panel_home,-1,pos=(300,0),size=(700,600))
        self.panel_home_left.SetupScrolling()
        self.panel_home_right.SetupScrolling()
        self.layout_left = wx.BoxSizer(wx.VERTICAL)
        self.layout_right = wx.BoxSizer(wx.VERTICAL)

        for name in names:
            checkbox_tmp = wx.CheckBox(self.panel_home_left,wx.ID_ANY,str(name))
            checkbox.append(checkbox_tmp)
            self.layout_left.Add(checkbox_tmp)

        self.Bind(wx.EVT_CHECKBOX,self.checked)

        self.panel_home_left.SetSizer(self.layout_left)
        self.panel_home_right.SetSizer(self.layout_right)

        self.notebook.InsertPage(0,self.panel_home, "現在の在庫状況")



        # 発注
        self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)
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
                self.panel_tmp = wx.Panel(self.panel_home_right,wx.ID_ANY,size=(700,100))
                self.label_tmp = wx.StaticText(self.panel_tmp,wx.ID_ANY,str(names[counts]))
                self.layout_right.Add(self.panel_tmp)
                self.layout_right.Layout()
            counts += 1
