import wx
import pandas as pd
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


class Developertool(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"開発者ツール")




        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()




        # パネル
        self.panel_developtool = wx.Panel(self)


        self.tmp1 = wx.StaticText(self.panel_developtool,wx.ID_ANY,"",size=(10,100))
        self.statictext_password = wx.StaticText(self.panel_developtool,wx.ID_ANY,"パスワードを入力して下さい。",style=wx.TE_CENTER)
        self.tmp2 = wx.StaticText(self.panel_developtool,wx.ID_ANY,"",size=(10,20))
        self.textctrl_password = wx.TextCtrl(self.panel_developtool,size=(100,20))
        self.label = wx.StaticText(self.panel_developtool,wx.ID_ANY,"",style=wx.TE_CENTER)
        self.label.SetForegroundColour((255, 0, 0))


        self.button_password = wx.Button(self.panel_developtool,-1,"設定",size=(100,20))
        self.button_password.SetForegroundColour((0,0,0))
        self.button_password.Bind(wx.EVT_BUTTON,self.clicked_button_password)

        self.layout_developtool = wx.BoxSizer(wx.VERTICAL)
        self.layout_developtool.Add(self.tmp1)
        self.layout_developtool.Add(self.statictext_password,flag=wx.GROW)
        self.layout_developtool.Add(self.tmp2)
        self.layout_developtool.Add(self.textctrl_password,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout_developtool.Add(self.label,flag=wx.GROW)
        self.layout_developtool.Add(self.button_password,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_developtool.SetSizer(self.layout_developtool)



        # 表示
        self.Show()


    def clicked_button_password(self,event):
        self.current_password = self.textctrl_password.GetValue()
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
            self.textctrl_password.Clear()
            self.label.SetLabel("パスワードが違います")
            self.layout_developtool.Layout()
