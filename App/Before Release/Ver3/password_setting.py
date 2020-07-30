import wx


class Password_setting(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"パスワードの変更")



        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()



        # パネル
        password_setting_panel = wx.Panel(self)



        # 現在のパスワード入力フォーム
        self.textctrl_password_setting = wx.TextCtrl(password_setting_panel,style=wx.TE_PASSWORD,pos=(150,100),size=(100,20))



        # 新しいパスワード入力フォーム
        self.textctrl_newpassword_setting = wx.TextCtrl(password_setting_panel,style=wx.TE_PASSWORD,pos=(150,150),size=(100,20))



        # ボタン
        self.button_password_setting = wx.Button(password_setting_panel,-1,"設定",pos=(150,200),size=(100,20))
        self.button_password_setting.SetForegroundColour((0,0,0))
        self.button_password_setting.Bind(wx.EVT_BUTTON,self.clicked_button_password_setting)



        # 表示
        self.Show()



    # ボタンをクリックした時
