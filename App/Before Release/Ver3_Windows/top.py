import wx
import wx.lib.scrolledpanel as scrolled
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import datetime
import password_setting
import ideal_value_setting
import add_and_delete
import help
import info
import developertool
import webbrowser




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





class Top(wx.Frame):
    def __init__(self):
        super().__init__(None,wx.ID_ANY,"在庫管理システム")





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
            add_and_delete.Add_and_delete()

        elif event_id == 2:
            ideal_value_setting.Ideal_value_setting()

        elif event_id == 3:
            password_setting.Password_setting()

        elif event_id == 4:
            help.Help()

        elif event_id == 5:
            info.Info()

        elif event_id == 6:
            developertool.Developertool()





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
