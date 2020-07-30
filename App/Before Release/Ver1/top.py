import wx
import wx.lib.scrolledpanel as scrolled

class panel_top(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent,wx.ID_ANY)
        self.parent = parent

        # panel_top = wx.Panel(self,-1,pos=(0,0),size=(1200,600))

        self.notebook = wx.Notebook(panel_top,wx.ID_ANY,style=wx.NB_TOP)

        self.panel_home = wx.Panel(self.notebook,wx.ID_ANY)
        # self.panel_home = wx.Panel(self.notebook,-1,pos=(0,0),size=(1200,800))
        self.panel_home_right = scrolled.ScrolledPanel(self.panel_home,wx.ID_ANY)
        self.panel_home_right.SetupScrolling()
        y_layout = wx.BoxSizer(wx.VERTICAL)
        y_layout.Add(wx.CheckBox(self.panel_home_right,wx.ID_ANY,"フォーク"))
        y_layout.Add(wx.CheckBox(self.panel_home_right,wx.ID_ANY,"スプーン"))
        y_layout.Add(wx.CheckBox(self.panel_home_right,wx.ID_ANY,"スプーン"))
        y_layout.Add(wx.CheckBox(self.panel_home_right,wx.ID_ANY,"スプーン"))
        y_layout.Add(wx.CheckBox(self.panel_home_right,wx.ID_ANY,"スプーン"))
        y_layout.Add(wx.CheckBox(self.panel_home_right,wx.ID_ANY,"スプーン"))
        self.panel_home_right.SetSizer(y_layout)
        # self.panel_home_left = scrolled.ScrolledPanel(self.panel_home,-1,pos=(150,0),size=(650,600))
        # self.panel_home_left.SetupScrolling()

        # self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)
        # self.panel_kakonodata = wx.Panel(self.notebook,wx.ID_ANY)
        # self.panel_syouhidouko = wx.Panel(self.notebook,wx.ID_ANY)

        self.notebook.InsertPage(0,self.panel_home,"ホーム")
        # self.notebook.InsertPage(1,self.panel_hacchu,"本日の発注")
        # self.notebook.InsertPage(2,self.panel_kakonodata,"過去のデータ")
        # self.notebook.InsertPage(3,self.panel_syouhidouko,"消費動向")

        # self.parent.sizer = wx.BoxSizer(wx.VERTICAL)
        # self.parent.sizer.Add(self.notebook,1,wx.EXPAND)
        # panel_top.SetSizer(self.parent.sizer)

        # self.Show()
