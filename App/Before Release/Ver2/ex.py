import wx
import wx.lib.scrolledpanel as scrolled
import pandas as pd

data = pd.read_csv("物資名.csv")
names = data["名前"]
checkbox = []

class Top(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム")

# class MyFrame(wx.Frame):
#     def __init__(self):
#        wx.Frame.__init__(self, None, -1, "Title")

        # フレーム
        self.SetSize((1000,700))
        self.SetBackgroundColour((207,207,207))
        self.Center()


        # Notebook設定
        # self.notebook = wx.Notebook(self,wx.ID_ANY,style=wx.NB_TOP)


        # 現在の在庫状況
        self.panel_home = wx.Panel(self,wx.ID_ANY)
        self.panel_home_left = wx.Panel(self.panel_home,-1,pos=(0,0),size=(300,600))
        self.panel_home_right = wx.Panel(self.panel_home,-1,pos=(300,0),size=(700,600))
        # self.panel_home_left.SetupScrolling()
        # self.panel_home_right.SetupScrolling()
        self.layout_left = wx.BoxSizer(wx.VERTICAL)
        self.layout_right = wx.BoxSizer(wx.VERTICAL)

        for name in names:
            tmp = wx.CheckBox(self.panel_home_left,wx.ID_ANY,str(name))
            checkbox.append(tmp)
            self.layout_left.Add(tmp)

        self.panel_home_right.SetSizer(self.layout_right)
        self.panel_home_left.SetSizer(self.layout_left)

        self.Bind(wx.EVT_CHECKBOX,self.checked)

        # self.notebook.InsertPage(0,self.panel_home, "現在の在庫状況")


        # 発注
        # self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)
        # self.notebook.InsertPage(1,self.panel_hacchu, "本日の発注")


        # 過去のデータ
        # self.panel_kakonodata = wx.Panel(self.notebook,wx.ID_ANY)
        # self.notebook.InsertPage(2,self.panel_kakonodata, "過去のデータ")
        #

        # 今後の発注数
        # self.panel_syouhidouko = wx.Panel(self.notebook,wx.ID_ANY)
        # self.notebook.InsertPage(3,self.panel_syouhidouko, "今後の発注数")


        # 表示
        self.Show()


    def checked(self,event):
        self.layout_right.Clear(False)
        counts = 0
        for checked in checkbox:
            torf = checked.GetValue()
            if torf == True:
                tmp2 = wx.StaticText(self.panel_home_right,wx.ID_ANY,str(names[counts]),size=(100,20))
                self.layout_right.Add(tmp2)
            counts += 1

app = wx.App()
Top()
app.MainLoop()










# import wx
#
# application = wx.App()
# frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 200))
#
# panel = wx.Panel(frame, wx.ID_ANY)
# panel.SetBackgroundColour('#AFAFAF')
#
# s_text_1 = wx.StaticText(panel, wx.ID_ANY, 'テキスト１')
# s_text_2 = wx.StaticText(panel, wx.ID_ANY, 'テキスト２')
# s_text_3 = wx.StaticText(panel, wx.ID_ANY, 'テキスト３')
# s_text_4 = wx.StaticText(panel, wx.ID_ANY, 'テキスト４')
# s_text_5 = wx.StaticText(panel, wx.ID_ANY, 'テキスト５')
#
# layout = wx.BoxSizer(wx.VERTICAL)
# layout.Add(s_text_1)
# layout.Add(s_text_2)
# layout.Add(s_text_3)
# layout.Add(s_text_4)
# layout.Add(s_text_5)
#
# panel.SetSizer(layout)
#
# frame.Show()
# application.MainLoop()
