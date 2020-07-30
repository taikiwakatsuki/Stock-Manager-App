import wx
import top


password_setting = "1234"

class Login(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム",size=(400,400),style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)



        # フレーム
        self.SetBackgroundColour((207, 207, 207))
        self.Center()



        # パネル
        panel_login = wx.Panel(self)



        # 背景画像
        self.image = wx.Image("login_image.png")
        self.image.Rescale(400,260)
        self.bitmap = self.image.ConvertToBitmap()
        self.image_login = wx.StaticBitmap(panel_login,-1,self.bitmap,pos=(0,0))



        # 警告表示
        self.label = wx.StaticText(panel_login,-1,"",pos=(137.5,270),size=(125,20))
        self.label.SetForegroundColour((255, 0, 0))



        # パスワード入力フォーム
        self.textctrl_password = wx.TextCtrl(panel_login,style=wx.TE_PASSWORD,pos=(150,300),size=(100,20))



        # ボタン
        self.button_login = wx.Button(panel_login,-1,"ログイン",pos=(150,340),size=(100,20))
        self.button_login.SetForegroundColour((0,0,0))
        self.button_login.Bind(wx.EVT_BUTTON,self.clicked_login)



        # 表示
        self.Show()



    # ボタンをクリックした時
    def clicked_login(self,event):
        self.password = self.textctrl_password.GetValue()
        if self.password == password_setting:
            top.Top()
            self.Destroy()
        else:
            self.textctrl_password.Clear()
            self.label.SetLabel("パスワードが違います")



# App表示
app = wx.App()
Login()
app.MainLoop()
