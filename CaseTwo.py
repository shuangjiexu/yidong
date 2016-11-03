# coding:UTF-8
import wx

class CaseTwo(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title=u"案例2：用户密度预测",
                          size=(1200, 1000),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.Panel1 = wx.Panel(self)
        self.Panel1.SetBackgroundColour('Red')

        self.Panel2 = wx.Panel(self)
        self.Panel2.SetBackgroundColour('Green')

        self.Panel3 = wx.Panel(self)
        self.Panel3.SetBackgroundColour('Blue')

        # ***************panel 1**********************************************
        self.InputDataButton = wx.Button(self.Panel1, label=u'导入数据')
        self.InputDataButton.Bind(wx.EVT_BUTTON, self.InputData)

        self.ScreenDataButton = wx.Button(self.Panel1, label=u'筛选异常用户数据')
        self.ScreenDataButton.Bind(wx.EVT_BUTTON, self.ScreenData)

        self.BlindspotMonitorButton = wx.Button(self.Panel1, label=u'盲点检测')
        self.BlindspotMonitorButton.Bind(wx.EVT_BUTTON, self.BlindspotMonitor)

        self.ResultOutputButton = wx.Button(self.Panel1, label=u'结果输出')
        self.ResultOutputButton.Bind(wx.EVT_BUTTON, self.ResultOutput)
        # ***************panel 1**********************************************

        # ***************panel 2**********************************************

        # ***************panel 2**********************************************

        # ***************panel 1 box set**********************************************
        self.IDbox = wx.BoxSizer(wx.VERTICAL)
        self.IDbox.Add(self.InputDataButton, proportion=0, flag=wx.LEFT, border=0)

        self.SDbox = wx.BoxSizer(wx.VERTICAL)
        self.SDbox.Add(self.ScreenDataButton, proportion=0, flag=wx.LEFT, border=0)

        self.BMbox = wx.BoxSizer(wx.VERTICAL)
        self.BMbox.Add(self.BlindspotMonitorButton, proportion=0, flag=wx.LEFT, border=0)

        self.RObox = wx.BoxSizer(wx.VERTICAL)
        self.RObox.Add(self.ResultOutputButton, proportion=0, flag=wx.LEFT, border=0)

        self.hbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox.Add(self.IDbox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.hbox.Add(self.SDbox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.hbox.Add(self.BMbox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.hbox.Add(self.RObox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)

        self.vbox = wx.BoxSizer()
        self.vbox.Add(self.hbox, proportion=0, flag=wx.ALL, border=10)

        self.Panel1.SetSizer(self.vbox)
        # ***************panel 1 box set**********************************************

        # ***************panel 2 box set**********************************************

        # ***************panel 2 box set**********************************************

        # ***************panel 3 box set**********************************************
        # ***************panel 3 box set**********************************************

        # ***************window box set**********************************************
        self.mbox = wx.BoxSizer(wx.VERTICAL)
        self.mbox.Add(self.Panel2, proportion=2, flag=wx.ALL | wx.EXPAND, border=10)
        self.mbox.Add(self.Panel3, proportion=20, flag=wx.ALL | wx.EXPAND, border=10)

        self.tbox = wx.BoxSizer()
        self.tbox.Add(self.Panel1, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.tbox.Add(self.mbox, proportion=5, flag=wx.ALL | wx.EXPAND, border=10)

        self.SetSizer(self.tbox)
        # ***************window box set**********************************************

    def InputData(self, evt):
        pass

    def ScreenData(self, evt):
        pass

    def BlindspotMonitor(self, evt):
        pass

    def ResultOutput(self, evt):
        pass

    def OnClose(self, evt):
        evt.Skip()
