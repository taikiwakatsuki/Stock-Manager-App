import wx
import login

class MyApp(wx.Frame):
    def __init__(self,*args,**kw):
        super(MyApp,self).__init__(*args,**kw)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        self.SetTitle("Inventry Managment Softwere")
        self.SetBackgroundColour((207, 207, 207))
        self.SetSize((1200,600))
        self.Center()

        self.set_screen(login.panel_login)

        self.Show()

    def set_screen(self,panel):
        self.sizer.Clear(False)
        self.DestroyChildren()

        self.now_panel = panel(self)
        self.sizer.Add(self.now_panel,1,wx.EXPAND)
        self.sizer.Layout()

app = wx.App()
MyApp(None)
app.MainLoop()
