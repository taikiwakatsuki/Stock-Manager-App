# import wx
# import login

# class MyApp(wx.Frame):
#     def __init__(self,*args,**kw):
#         super(MyApp,self).__init__(*args,**kw)
#
#         self.sizer = wx.BoxSizer(wx.VERTICAL)
#         self.SetSizer(self.sizer)
#
#         self.SetTitle("Inventry Managment Softwere")
#         self.SetBackgroundColour((207, 207, 207))
#         self.SetSize((800,600))
#         self.Center()
#         # self.Show()
#
#         panel_top = wx.Panel(self,-1,pos=(0,0),size=(800,600))
#
#         self.notebook = wx.Notebook(panel_top,wx.ID_ANY)
#
#         # self.sizer = wx.BoxSizer(wx.VERTICAL)
#         self.sizer.Add(self.notebook,1,wx.EXPAND)
#         # panel_top.SetSizer(self.sizer)
#
#         self.panel_home = wx.Panel(self.notebook,wx.ID_ANY)
#         self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)
#         self.panel_kakonodata = wx.Panel(self.notebook,wx.ID_ANY)
#         self.panel_syouhidouko = wx.Panel(self.notebook,wx.ID_ANY)
#
#         self.panel_home.SetBackgroundColour("#550138")
#         self.panel_hacchu.SetBackgroundColour("#9f9247")
#         self.panel_kakonodata.SetBackgroundColour("#703dcf")
#         self.panel_syouhidouko.SetBackgroundColour("#0b551b")
#
#         self.notebook.InsertPage(0,self.panel_home, "ホーム")
#         self.notebook.InsertPage(1,self.panel_hacchu, "本日の発注")
#         self.notebook.InsertPage(2,self.panel_kakonodata, "過去のデータ")
#         self.notebook.InsertPage(3,self.panel_syouhidouko, "消費動向")
#
#         self.Show()
#
# app = wx.App()
# MyApp(None)
# app.MainLoop()










# import wx

# application = wx.App()
# frame = wx.Frame(None, wx.ID_ANY, 'テストフレーム', size=(300, 200))
#
# panel = wx.Panel(frame, wx.ID_ANY)
# panel.SetBackgroundColour('#AFAFAF')
#
# button_1 = wx.Button(panel, wx.ID_ANY, 'ボタン１')
# button_2 = wx.Button(panel, wx.ID_ANY, 'ボタン２')
# button_3 = wx.Button(panel, wx.ID_ANY, 'ボタン３')
# button_4 = wx.Button(panel, wx.ID_ANY, 'ボタン４')
#
# button_3.SetBackgroundColour('#0000FF')
#
# layout = wx.GridSizer(rows=2, cols=2, gap=(0, 0))
# layout.Add(button_1, 0, wx.GROW)
# layout.Add(button_2, 0, wx.GROW)
# layout.Add(button_3, 0, wx.GROW)
# layout.Add(button_4, 0, wx.GROW)
#
# panel.SetSizer(layout)
#
# frame.Show()
# application.MainLoop()










import wx
import wx.lib.scrolledpanel as scrolled

class Main(wx.Frame):

    def __init__(self, parent, id, title):
        """ レイアウトの作成 """

        wx.Frame.__init__(self, parent, id, title)
        notebook = wx.Notebook(self,wx.ID_ANY,style=wx.NB_TOP)
        panel = scrolled.ScrolledPanel(notebook, wx.ID_ANY)
        panel.SetupScrolling()

        # checkbox_1 = wx.CheckBox(panel,wx.ID_ANY,"フォーク")

        v_layout = wx.BoxSizer(wx.VERTICAL)

        # v_layout.Add(checkbox_1)
        v_layout.Add(wx.CheckBox(panel,wx.ID_ANY,"フォーク"))

        for i in range(30):
            text = wx.StaticText(panel, wx.ID_ANY, str(i))
            v_layout.Add(text)

        panel.SetSizer(v_layout)
        notebook.InsertPage(0,panel, "ホーム")
        self.Show(True)

def main():
    app = wx.App()
    Main(None, wx.ID_ANY, "タイトル")
    app.MainLoop()

if __name__ == "__main__":
    main()
