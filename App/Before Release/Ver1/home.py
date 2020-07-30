import wx
import wx.lib.scrolledpanel as scrolled
import top

class home(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent,wx.ID_ANY)
        self.parent = parent

        panel = scrolled.ScrolledPanel(top.top.self.notebook, wx.ID_ANY)
        panel.SetupScrolling()

        v_layout = wx.BoxSizer(wx.VERTICAL)

        for i in range(30):
            text = wx.StaticText(panel, wx.ID_ANY, str(i))
            v_layout.Add(text)

        panel.SetSizer(v_layout)
        self.Show(True)
