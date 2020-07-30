import wx
import top

class panel_login(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent,wx.ID_ANY)
        self.parent = parent
        panel_login = wx.Panel(self,-1,pos=(0,0),size=(1200,600))

        # self.image = wx.Image("login_image.png")
        # self.image.Rescale(800,550)
        # self.bitmap = self.image.ConvertToBitmap()
        # self.image_login = wx.StaticBitmap(panel_login,-1,self.bitmap,pos=(0,0))

        self.label = wx.StaticText(panel_login,-1,"",pos=(335,280),size=(150,20))
        # self.label = wx.StaticText(panel_login,-1,"")
        self.label.SetForegroundColour((255, 0, 0))

        self.textctrl_password = wx.TextCtrl(panel_login,style=wx.TE_PASSWORD,pos=(350,310),size=(100,20))
        # self.textctrl_password = wx.TextCtrl(panel_login,style=wx.TE_PASSWORD)
        # self.textctrl_password.SetBackgroundColour((131, 185, 255))

        self.button_login = wx.Button(panel_login,-1,"Log In",pos=(350,350),size=(100,20))
        # self.button_login = wx.Button(panel_login,-1,"Log In")
        # self.button_login.SetBackgroundColour((0, 110, 255))
        self.button_login.SetForegroundColour((0, 0, 0))
        self.button_login.Bind(wx.EVT_BUTTON,self.clicked_login)

        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.layout.Add(self.label)
        self.layout.Add(self.textctrl_password)
        self.layout.Add(self.button_login)
        panel_login.SetSizer(self.layout)

    def clicked_login(self,event):
        self.password = self.textctrl_password.GetValue()
        if self.password == "1234":
            self.parent.set_screen(top.panel_top)
        else:
            self.textctrl_password.Clear()
            self.label.SetLabel("※パスワードが違います")
