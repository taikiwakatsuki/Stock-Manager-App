import wx
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pickle



# バイナリーファイルから読み込む．
with open("secret.binaryfile","rb") as password:
  password_setting_hash_value = pickle.load(password)



# .pemファイルでパスワード復元
with open("private.pem","br") as f:
    private_pem = f.read()
    private_key = RSA.import_key(private_pem)

private_cipher = PKCS1_OAEP.new(private_key)
password_setting = private_cipher.decrypt(password_setting_hash_value).decode("utf-8")



class Password_setting(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"パスワードの変更")



        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()



        # パネル
        self.password_setting_panel = wx.Panel(self)



        # 警告表示
        self.label = wx.StaticText(self.password_setting_panel,-1,"",pos=(135,180),size=(125,20))
        self.label.SetForegroundColour((255, 0, 0))



        # 現在のパスワード入力フォーム
        self.statictext_password_setting = wx.StaticText(self.password_setting_panel,wx.ID_ANY,"現在のパスワード",pos=(150,80),size=(100,20))
        self.textctrl_password_setting = wx.TextCtrl(self.password_setting_panel,pos=(150,100),size=(100,20))



        # 新しいパスワード入力フォーム
        self.statictext_newpassword_setting = wx.StaticText(self.password_setting_panel,wx.ID_ANY,"新しいパスワード",pos=(150,130),size=(100,20))
        self.textctrl_newpassword_setting = wx.TextCtrl(self.password_setting_panel,pos=(150,150),size=(100,20))


        # ボタン
        self.button_password_setting = wx.Button(self.password_setting_panel,-1,"設定",pos=(150,200),size=(100,20))
        self.button_password_setting.SetForegroundColour((0,0,0))
        self.button_password_setting.Bind(wx.EVT_BUTTON,self.clicked_button_password_setting)



        # 表示
        self.Show()



    # ボタンをクリックした時
    def clicked_button_password_setting(self,event):
        self.current_password = self.textctrl_password_setting.GetValue()
        self.new_password = self.textctrl_newpassword_setting.GetValue()
        if password_setting == self.current_password:
            with open("public.pem","br") as f:
                public_pem = f.read()
                public_key = RSA.import_key(public_pem)
            public_cipher = PKCS1_OAEP.new(public_key)
            ciphertext = public_cipher.encrypt(self.new_password.encode())
            with open("secret.binaryfile","wb") as password:
                pickle.dump(ciphertext,password)
            self.Destroy()
        else:
            self.textctrl_password_setting.Clear()
            self.textctrl_newpassword_setting.Clear()
            self.label.SetLabel("現在のパスワードが違います")
