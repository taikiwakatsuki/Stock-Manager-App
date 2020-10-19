# ライブラリのインポート
import wx
import wx.lib.scrolledpanel as scrolled
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import datetime
import pandas as pd
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import pickle
import webbrowser


# バイナリーファイルからハッシュ値を読み込む．
with open("secret.binaryfile","rb") as password:
  password_setting_hash_value = pickle.load(password)


# .pemファイルでパスワード復元
with open("private.pem","br") as f:
    private_pem = f.read()
    private_key = RSA.import_key(private_pem)

private_cipher = PKCS1_OAEP.new(private_key)
password_setting = private_cipher.decrypt(password_setting_hash_value).decode("utf-8")


# グローバル関数の定義
date = datetime.date.today()

data = pd.read_csv("Data.csv")
names = data["物資名"]
TorF = data["TorF"]
ideal_value = data["理想量"]
value = data["現在の量"]
criterion_number_of_customers = data["1在庫を消費する客数"]
all_number_of_customers = data["前回発注日からの客数"]
last_time_hacchu_quantity = data["前回発注数"]
last_time_hacchu_day = data["前回発注日"]
hacchu = data["更新日"]

log = pd.read_csv("Log.csv",index_col=0)
log_date = log["日付"]
log_name = log["物資名"]
log_quantity = log["発注数"]

checkbox = []
hacchu_counter = []
comboboxs = []
hacchu_date = []
element_array = []


# login画面
class Login(wx.Frame):


    # init
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム",size=(400,400),style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)


        # フレーム
        self.SetBackgroundColour((207, 207, 207))
        self.Center()


        # パネル
        self.panel_login = wx.Panel(self)


        # 背景画像
        self.image = wx.Image("login_image.png")
        self.image.Rescale(380,260)
        self.bitmap = self.image.ConvertToBitmap()
        self.image_login = wx.StaticBitmap(self.panel_login,-1,self.bitmap,pos=(0,0))
        self.layout_tmp = wx.BoxSizer(wx.VERTICAL)
        self.layout_tmp.Add(self.image_login)


        # 警告表示
        self.label = wx.StaticText(self.panel_login,-1,"",size=(125,20))
        self.label.SetForegroundColour((255, 0, 0))


        # パスワード入力フォーム
        self.textctrl_password = wx.TextCtrl(self.panel_login,style=wx.TE_PASSWORD,size=(100,20))


        # 空白
        self.tmp1 = wx.StaticText(self.panel_login,-1,"",size=(10,5))


        # ボタン
        self.button_login = wx.Button(self.panel_login,-1,"ログイン",size=(100,20))
        self.button_login.SetForegroundColour((0,0,0))
        self.button_login.Bind(wx.EVT_BUTTON,self.clicked_login)


        # Sizer
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.layout.Add(self.layout_tmp,flag=wx.CENTER)
        self.layout.Add(self.label,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.textctrl_password,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.tmp1)
        self.layout.Add(self.button_login,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_login.SetSizer(self.layout)
        # self.Layout()


        # 表示
        self.Show()


    # ボタンをクリックした時
    def clicked_login(self,event):
        self.password = self.textctrl_password.GetValue()
        if self.password == password_setting:
            Top()
            self.Destroy()
        else:
            self.textctrl_password.Clear()
            self.label.SetLabel("パスワードが違います")


# top画面
class Top(wx.Frame):


    # init
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム",style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)


        # フレーム
        self.SetSize((1000,700))
        self.SetBackgroundColour((207,207,207))
        self.Center()


        # メニューバー
        self.menu_bar = wx.MenuBar()
        self.menu_setting = wx.Menu()
        self.menu_setting.Append(1,"物資の追加・削除")
        self.menu_setting.Append(2,"理想量の変更")
        self.menu_setting.Append(3,"パスワードの変更")

        self.menu_help = wx.Menu()
        self.menu_help.Append(4,"ヘルプ")

        self.menu_info = wx.Menu()
        self.menu_info.Append(5,"情報")

        self.menu_developertool = wx.Menu()
        self.menu_developertool.Append(6,"開発者ツール")

        self.menu_bar.Append(self.menu_setting,"設定")
        self.menu_bar.Append(self.menu_help,"ヘルプ")
        self.menu_bar.Append(self.menu_info,"情報")
        self.menu_bar.Append(self.menu_developertool,"開発者ツール")

        self.SetMenuBar(self.menu_bar)

        self.Bind(wx.EVT_MENU, self.clicked)


        # Notebook設定
        self.notebook = wx.Notebook(self,wx.ID_ANY,style=wx.NB_TOP)


        # 現在の在庫状況
        self.panel_home = wx.Panel(self.notebook,wx.ID_ANY)
        self.panel_home_left = scrolled.ScrolledPanel(self.panel_home,-1,pos=(0,0),size=(300,615))
        self.panel_home_right = scrolled.ScrolledPanel(self.panel_home,-1,pos=(300,0),size=(680,615))
        self.panel_home_left.SetupScrolling()
        self.panel_home_right.SetupScrolling()
        self.layout_left = wx.BoxSizer(wx.VERTICAL)
        self.layout_right = wx.BoxSizer(wx.VERTICAL)

        counts1 = 0
        for name in names:
            checkbox_tmp = wx.CheckBox(self.panel_home_left,wx.ID_ANY,str(name))
            if TorF[counts1] == True:
                checkbox_tmp.SetValue(True)
            else:
                checkbox_tmp.SetValue(False)
            checkbox.append(checkbox_tmp)
            self.layout_left.Add(checkbox_tmp)
            counts1 += 1

        counts1 = 0
        for checked in checkbox:
            self.torf = checked.GetValue()
            if self.torf == True:
                plt.rcParams["ytick.direction"] = "in"
                self.fig = Figure(figsize=(6,1),facecolor=(0.81,0.81,0.81))
                self.fig.suptitle(str(names[counts1]),fontname="MS Gothic",fontsize=8)
                self.ax = self.fig.add_subplot(111)
                self.fig.subplots_adjust(bottom=0.7,top=0.8)
                self.ax.set_xlim(0,1.0)
                self.ax.set_xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
                self.ax.set_xticklabels(["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
                self.ax.set_ylim(0,1)
                self.ax.set_yticks([0.5])
                self.ax.set_yticklabels([""])
                x = [0.5]
                y = value[counts1] / ideal_value[counts1]
                self.ax.barh(x,y,align="center")
                self.canvas = FigureCanvas(self.panel_home_right,-1,self.fig)
                self.layout_right.Add(self.canvas)
                self.layout_right.Layout()
            counts1 += 1

        self.Bind(wx.EVT_CHECKBOX,self.checked)

        self.panel_home_left.SetSizer(self.layout_left)
        self.panel_home_right.SetSizer(self.layout_right)

        self.notebook.InsertPage(0,self.panel_home, "現在の在庫状況")


        # 発注
        self.panel_hacchu = wx.Panel(self.notebook,wx.ID_ANY)

        self.panel_hacchu_center = scrolled.ScrolledPanel(self.panel_hacchu,-1,size=(1000,565))
        self.panel_hacchu_center.SetupScrolling()

        self.layout_hacchu = wx.BoxSizer(wx.VERTICAL)

        self.panel_hacchu_message = wx.Panel(self.panel_hacchu_center,-1,size=(1000,100))
        self.statictext_hacchu_message = wx.StaticText(self.panel_hacchu_message,-1,"本日の発注をして下さい。",pos=(400,20),size=(200,20))
        self.font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.statictext_hacchu_message.SetFont(self.font)
        self.statictext_hacchu_message.SetForegroundColour((255, 0, 0))
        self.layout_hacchu.Add(self.panel_hacchu_message)
        self.layout_hacchu.Layout()

        counts2 = 0
        for name in names:
            if criterion_number_of_customers[counts2] == all_number_of_customers[counts2]:
                self.panel_hacchu_tmp = wx.Panel(self.panel_hacchu_center,-1,size=(1000,30))
                self.text = wx.StaticText(self.panel_hacchu_tmp,wx.ID_ANY,str(name),pos=(325,0),size=(300,20))
                self.font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
                self.text.SetFont(self.font)
                self.element_array = ("1","2","3","4","5")
                self.combobox = wx.ComboBox(self.panel_hacchu_tmp,wx.ID_ANY,choices=self.element_array,style=wx.CB_READONLY,pos=(625,0),size=(50,20))
                comboboxs.append(self.combobox)
                self.layout_hacchu.Add(self.panel_hacchu_tmp)
                self.layout_hacchu.Layout()
                hacchu_counter.append(counts2)
            counts2 += 1

        self.panel_hacchu_button = wx.Panel(self.panel_hacchu_center,-1,size=(1000,30))
        self.button_hacchu = wx.Button(self.panel_hacchu_button,-1,"発注",pos=(450,0),size=(100,20))
        self.button_hacchu.SetForegroundColour((0,0,0))
        self.button_hacchu.Bind(wx.EVT_BUTTON,self.clicked_button_hacchu)
        self.layout_hacchu.Add(self.panel_hacchu_button)
        self.layout_hacchu.Layout()

        self.panel_hacchu_center.SetSizer(self.layout_hacchu)

        self.notebook.InsertPage(1,self.panel_hacchu, "本日の発注")


        # 過去の発注データ
        self.panel_kakonodata = wx.Panel(self.notebook,wx.ID_ANY)
        self.layout_kakonodata_first = wx.BoxSizer(wx.VERTICAL)

        self.panel_kakonodata_center = scrolled.ScrolledPanel(self.panel_kakonodata,-1,size=(1000,565))
        self.panel_kakonodata_center.SetupScrolling()

        self.layout_kakonodata = wx.BoxSizer(wx.VERTICAL)

        self.panel_kakonodata_message = wx.Panel(self.panel_kakonodata_center,-1,size=(1000,30))
        self.statictext_kakonodata_message_day = wx.StaticText(self.panel_kakonodata_message,-1,"日付",pos=(295,5),size=(100,20))
        self.statictext_kakonodata_message_name = wx.StaticText(self.panel_kakonodata_message,-1,"物資名",pos=(470,5),size=(300,20))
        self.statictext_kakonodata_message_quantity = wx.StaticText(self.panel_kakonodata_message,-1,"個数",pos=(660,5),size=(50,20))
        self.font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.statictext_kakonodata_message_day.SetFont(self.font)
        self.statictext_kakonodata_message_name.SetFont(self.font)
        self.statictext_kakonodata_message_quantity.SetFont(self.font)
        self.statictext_kakonodata_message_day.SetForegroundColour((0, 56, 152))
        self.statictext_kakonodata_message_name.SetForegroundColour((0, 56, 152))
        self.statictext_kakonodata_message_quantity.SetForegroundColour((0, 56, 152))
        self.layout_kakonodata.Add(self.panel_kakonodata_message)
        self.layout_kakonodata.Layout()

        self.layout_kakonodata.Add(wx.StaticLine(self.panel_kakonodata_center),flag=wx.GROW)
        self.layout_kakonodata.Layout()

        counts3 = 1
        counts3_counts = len(log_name)
        for ln in reversed(log_name):
            self.panel_tmp = wx.Panel(self.panel_kakonodata_center,-1,size=(1000,30))
            self.font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            self.statictext_log_date = wx.StaticText(self.panel_tmp,-1,str(log_date[counts3_counts-counts3]),pos=(275,10),size=(100,20))
            self.statictext_log_name = wx.StaticText(self.panel_tmp,-1,str(log_name[counts3_counts-counts3]),pos=(375,10),size=(300,20))
            self.statictext_log_quantity = wx.StaticText(self.panel_tmp,-1,str(log_quantity[counts3_counts-counts3]),pos=(675,10),size=(50,20))
            self.statictext_log_date.SetFont(self.font)
            self.statictext_log_name.SetFont(self.font)
            self.statictext_log_quantity.SetFont(self.font)
            self.layout_kakonodata.Add(self.panel_tmp)
            self.layout_kakonodata.Layout()
            counts3 += 1

        self.panel_kakonodata_center.SetSizer(self.layout_kakonodata)

        self.notebook.InsertPage(2,self.panel_kakonodata, "過去のデータ")


        # # 今後の発注数
        # self.panel_syouhidouko = wx.Panel(self.notebook,wx.ID_ANY)
        # self.notebook.InsertPage(3,self.panel_syouhidouko, "今後の発注数")


        # 表示
        self.Show()


    # チェックボックスにチェックをした時の画面変化
    def checked(self,event):
        self.layout_right.Clear(True)
        counts = 0
        for checked in checkbox:
            self.torf = checked.GetValue()
            if self.torf == True:
                TorF[counts] = True
                plt.rcParams["ytick.direction"] = "in"
                self.fig = Figure(figsize=(6,1),facecolor=(0.81,0.81,0.81))
                self.fig.suptitle(str(names[counts]),fontname="MS Gothic",fontsize=8)
                self.ax = self.fig.add_subplot(111)
                self.fig.subplots_adjust(bottom=0.7,top=0.8)
                self.ax.set_xlim(0,1.0)
                self.ax.set_xticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
                self.ax.set_xticklabels(["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
                self.ax.set_ylim(0,1)
                self.ax.set_yticks([0.5])
                self.ax.set_yticklabels([""])
                x = [0.5]
                y = value[counts] / ideal_value[counts]
                self.ax.barh(x,y,align="center")
                self.canvas = FigureCanvas(self.panel_home_right,-1,self.fig)
                self.layout_right.Add(self.canvas)
                self.layout_right.Layout()
            else:
                TorF[counts] = False
            data.to_csv("Data.csv")
            counts += 1
            self.panel_home_right.SetupScrolling()


    # メニューバーがクリックされた時
    def clicked(self,event):
        event_id = event.GetId()
        if event_id == 1:
            Add_and_delete()

        elif event_id == 2:
            Ideal_value_setting()

        elif event_id == 3:
            Password_setting()

        elif event_id == 4:
            Help()

        elif event_id == 5:
            Info()

        elif event_id == 6:
            Developertool()


    # 発注ボタンがクリックされた時
    def clicked_button_hacchu(self,event):
        if str(hacchu[0]) == str(date):
            self.statictext_hacchu_message.SetLabel("本日は発注完了しています。")
            self.statictext_hacchu_message.SetForegroundColour((0, 56, 152))
        else:
            counts4 = 0
            for hacchu_counter_tmp in hacchu_counter:
                last_time_hacchu_day[hacchu_counter_tmp] = str(date)
                last_time_hacchu_quantity[hacchu_counter_tmp] = comboboxs[counts4].GetStringSelection()
                log_order = [last_time_hacchu_day[hacchu_counter_tmp],names[hacchu_counter_tmp],last_time_hacchu_quantity[hacchu_counter_tmp]]
                log.loc[len(log)] = log_order
                counts4 += 1
            hacchu[0] = str(date)
            webbrowser.open("https://www.google.com")
            data.to_csv("Data.csv")
            log.to_csv("Log.csv")


# 物資の追加・削除
class Add_and_delete(wx.Frame):


    # init
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"物資の追加・削除")


        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()


        # パネル
        self.panel_add_and_delete = wx.Panel(self)


# 理想量の変更
class Ideal_value_setting(wx.Frame):


    # init
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"理想量の変更")


        # フレーム
        self.SetSize((400,400))
        self.SetBackgroundColour((207,207,207))
        self.Center()


        # パネル
        self.ideal_value_setting_panel = wx.Panel(self)


        # コンボボックス
        for name in names:
            element_array.append(str(name))
        self.combobox = wx.ComboBox(self.ideal_value_setting_panel,wx.ID_ANY,choices=element_array,style=wx.CB_READONLY,pos=(100,50),size=(200,50))


        # ボタン
        self.button_ideal_value_setting = wx.Button(self.ideal_value_setting_panel,-1,"設定",pos=(150,100),size=(100,20))
        self.button_ideal_value_setting.SetForegroundColour((0,0,0))
        self.button_ideal_value_setting.Bind(wx.EVT_BUTTON,self.clicked_button_ideal_value_setting)


        # 表示
        self.Show()


    # ボタンをクリックした時
    def clicked_button_ideal_value_setting(self,event):
        counter = 0
        for name in names:
            if name == self.combobox.GetValue():
                self.counts = counter
            counter += 1
        self.statictext_ideal_value_setting = wx.StaticText(self.ideal_value_setting_panel,wx.ID_ANY,"現在の理想量は「" + str(ideal_value[self.counts]) + "」です。新しい理想量を入力してください。",pos=(60,200),size=(400,50))
        self.textctrl_ideal_value_setting = wx.TextCtrl(self.ideal_value_setting_panel,pos=(120,250),size=(50,20))
        self.button_newideal_value_setting = wx.Button(self.ideal_value_setting_panel,-1,"変更",pos=(180,250),size=(100,20))
        self.button_newideal_value_setting.SetForegroundColour((0,0,0))
        self.button_newideal_value_setting.Bind(wx.EVT_BUTTON,self.clicked_button_newideal_value_setting)


    # ボタンをクリックした時
    def clicked_button_newideal_value_setting(self,event):
        ideal_value[self.counts] = self.textctrl_ideal_value_setting.GetValue()
        data.to_csv("Data.csv")
        self.Destroy()


# パスワードの変更
class Password_setting(wx.Frame):


    # init
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


# ヘルプ
class Help(wx.Frame):


    # init
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"ヘルプ",style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)


        # フレーム
        self.SetSize((500,600))
        self.SetBackgroundColour((207,207,207))
        self.Center()


        # パネル
        self.panel_help = wx.Panel(self)
        self.panel_help_scroll = scrolled.ScrolledPanel(self.panel_help,-1,pos=(0,0),size=(500,600))
        self.panel_help_scroll.SetupScrolling()


        # 説明
        self.tmp1 = wx.StaticText(self.panel_help_scroll,-1,size=(10,20))
        self.statictext_help_title = wx.StaticText(self.panel_help_scroll,-1,"ヘルプ",style=wx.TE_CENTER)
        self.tmp2 = wx.StaticText(self.panel_help_scroll,-1,size=(10,30))
        self.font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.statictext_help_title.SetFont(self.font)
        self.statictext_help_para1 = wx.StaticText(self.panel_help_scroll,-1,"＜現在の在庫状況＞")
        self.statictext_help_para2 = wx.StaticText(self.panel_help_scroll,-1,"あらかじめ設定した理想量を100%として、現在ある在庫の割合を表示している。左のチェックボックスにチェックを入れることで、確認したい物資を表示させることができる。また、理想量の変更や物資の追加および削除はメニューバーから行うことができる。",size=(400,60))
        self.tmp3 = wx.StaticText(self.panel_help_scroll,-1,size=(10,10))
        self.statictext_help_para3 = wx.StaticText(self.panel_help_scroll,-1,"＜本日の発注＞")
        self.statictext_help_para4 = wx.StaticText(self.panel_help_scroll,-1,"本日発注しなければならない物資を表示している。こ",size=(400,50))
        self.tmp4 = wx.StaticText(self.panel_help_scroll,-1,size=(10,10))
        self.statictext_help_para5 = wx.StaticText(self.panel_help_scroll,-1,"＜過去のデータ＞")
        self.statictext_help_para6 = wx.StaticText(self.panel_help_scroll,-1,"過去に発注した日付と物資名、物資の数を表示している。",size=(400,40))
        self.tmp5 = wx.StaticText(self.panel_help_scroll,-1,size=(10,10))
        self.statictext_help_para7 = wx.StaticText(self.panel_help_scroll,-1,"＜メニューバー＞")
        self.statictext_help_para8 = wx.StaticText(self.panel_help_scroll,-1,"メニューバーにある「設定」では、物資の追加および削除、理想量の変更、ログインパスワードの変更ができる。「ヘルプ」では、このアプリケーションの使い方を確認できる。「情報」では、システムのバージョンおよび動作環境を確認できる。",size=(400,60))
        self.layout = wx.BoxSizer(wx.VERTICAL)
        self.layout.Add(self.tmp1)
        self.layout.Add(self.statictext_help_title,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.tmp2)
        self.layout.Add(self.statictext_help_para1,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.statictext_help_para2,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.tmp3)
        self.layout.Add(self.statictext_help_para3,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.statictext_help_para4,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.tmp4)
        self.layout.Add(self.statictext_help_para5,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.statictext_help_para6,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.tmp5)
        self.layout.Add(self.statictext_help_para7,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.layout.Add(self.statictext_help_para8,flag=wx.SHAPED | wx.ALIGN_CENTER)
        self.panel_help_scroll.SetSizer(self.layout)



        # 表示
        self.Show()


# 情報
class Info(wx.Frame):


    # init
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"情報",style=wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)


        # フレーム
        self.SetSize((400,280))
        self.SetBackgroundColour((32, 32, 32))
        self.Center()


        # パネル
        self.panel_info = wx.Panel(self)


        # 情報
        self.statictext_info_tmp1 = wx.StaticText(self.panel_info,-1,"")
        self.statictext_info_version = wx.StaticText(self.panel_info,-1,"Version1.0",style=wx.TE_CENTER)
        self.statictext_info_version.SetForegroundColour((231, 231, 231))
        self.statictext_info_tmp2 = wx.StaticText(self.panel_info,-1,"")
        self.statictext_info_release_date = wx.StaticText(self.panel_info,-1,"Release 2020/00/00",style=wx.TE_CENTER)
        self.statictext_info_release_date.SetForegroundColour((99, 99, 99))
        self.statictext_info_update_date = wx.StaticText(self.panel_info,-1,"Update 2020/00/00",style=wx.TE_CENTER)
        self.statictext_info_update_date.SetForegroundColour((99, 99, 99))
        self.statictext_info_tmp3 = wx.StaticText(self.panel_info,-1,"")
        self.statictext_info_enviroment = wx.StaticText(self.panel_info,-1,"Windows10",style=wx.TE_CENTER)
        self.statictext_info_enviroment.SetForegroundColour((99, 99, 99))
        self.statictext_info_language = wx.StaticText(self.panel_info,-1,"Python3.6.5",style=wx.TE_CENTER)
        self.statictext_info_language.SetForegroundColour((99, 99, 99))
        self.statictext_info_library = wx.StaticText(self.panel_info,-1,"\n -Library- \n matplotlib,pandas,wxPython \n datetime,hashlib,pickle \n webbrowser,pycryptodome",style=wx.TE_CENTER)
        self.statictext_info_library.SetForegroundColour((99, 99, 99))
        self.font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.statictext_info_version.SetFont(self.font)

        self.layout_info = wx.BoxSizer(wx.VERTICAL)
        self.layout_info.Add(self.statictext_info_tmp1,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_version,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_tmp2,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_release_date,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_update_date,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_tmp3,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_enviroment,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_language,flag=wx.GROW)
        self.layout_info.Add(self.statictext_info_library,flag=wx.GROW)
        self.panel_info.SetSizer(self.layout_info)


        # 表示
        self.Show()


# 開発者ツール
class Developertool(wx.Frame):


    # init
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
        self.textctrl_password = wx.TextCtrl(self.panel_developtool,style=wx.TE_PASSWORD,size=(100,20))
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


    # ボタンをクリックした時
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


# App表示
app = wx.App()
Login()
app.MainLoop()
