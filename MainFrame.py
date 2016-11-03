# coding:UTF-8
import sys
import wx
import time
import os
import CaseOne
import CaseTwo
import CaseThree
import BigDataAnalysis
########################################################################
# set the file filter
wildcard1 = "Txt source (*.txt)|*.txt|"\
            "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Txt source (*.txt)|*.txt|"\
    "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"
########################################################################
class Demo(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title="Demo platform",
                          size=(1200, 1000),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Cflag = 0

        self.Panel1 = wx.Panel(self)
        self.Panel1.SetBackgroundColour('Red')

        self.Panel2 = wx.Panel(self)
        self.Panel2.SetBackgroundColour('Green')

        self.Panel3 = wx.Panel(self)
        self.Panel3.SetBackgroundColour('Blue')

        self.Panel4 = wx.Panel(self)
        self.Panel4.SetBackgroundColour('Yellow')

        #***************panel 1**********************************************
        IndexSystemButton = wx.Button(self.Panel1, label=u'指标体系')
        IndexSystemButton.Bind(wx.EVT_BUTTON, self.IndexSystem)

        BigDataAnalysisButton = wx.Button(self.Panel1, label=u'大数据分析')
        BigDataAnalysisButton.Bind(wx.EVT_BUTTON, self.BigDataAnalysis)

        CaseShowButton = wx.Button(self.Panel1, label=u'案例展示')
        CaseShowButton.Bind(wx.EVT_BUTTON, self.CaseShow)

        CaseOneButton = wx.Button(self.Panel1, label=u'案例1:盲点检测展示')
        CaseOneButton.Bind(wx.EVT_BUTTON, self.CaseOne)
        CaseTwoButton = wx.Button(self.Panel1, label=u'案例2:用户密度预测')
        CaseTwoButton.Bind(wx.EVT_BUTTON, self.CaseTwo)
        CaseThreeButton = wx.Button(self.Panel1, label=u'案例3:异常信令事件分析')
        CaseThreeButton.Bind(wx.EVT_BUTTON, self.CaseThree)
        # ***************panel 1**********************************************

        # ***************panel 2**********************************************
        self.sampleList1 = {
            u"接入类指标":0,
            u"保持类指标":1,
            u"信道类指标":2,
            u"用户分布类指标":3,
            u"用户感知类指标":4,
            u"其他类指标":5
        }
        self.sampleList2 = [
            [u"业务请求时延", u"加密时延", u"身份识别时延",u"TMSI重分配时延",u"语音寻呼时延"],
            [u"剔除UI的无线掉线率"],
            [u"阴影效应", u"多普勒效应", u"远近效应"],
            [u"用户密度", u"用户密度对通信质量影响"],
            [u"低接通用户数劣化指标", u"高掉线用户数劣化指标", u"高流量用户时延劣化指标",u"高流量用户接通劣化指标",
             u"高时延用户数劣化指标"],
            [u"上行业务质量", u"上行噪声影响", u"上行干扰对弱覆盖的影响",u"下行业务弱覆盖影响"]
        ]
        self.sample = wx.StaticText(self.Panel2, -1, u"指标类型:", style=wx.ALIGN_CENTER)
        self.choices1 = wx.Choice(self.Panel2, -1,choices=self.sampleList1.keys(),style=wx.ALIGN_CENTER)

        self.indexname = wx.StaticText(self.Panel2, -1, u"指标名称:", style=wx.ALIGN_CENTER)
        self.choices2 = wx.Choice(self.Panel2, -1, choices=self.sampleList2[0], style=wx.ALIGN_CENTER)

        self.choices1.Bind(wx.EVT_CHOICE, self.UpdateC2)
        # ***************panel 2**********************************************

        # ***************panel 3**********************************************
        # ***************panel 3**********************************************

        # ***************panel 4**********************************************
        #状态栏
        self.bar = wx.TextCtrl(self.Panel4, style=wx.TE_MULTILINE | wx.TE_RICH2)
        # ***************panel 4**********************************************

        # ***************panel 1 box set**********************************************
        self.CSTbox = wx.BoxSizer(wx.VERTICAL)
        self.CSTbox.Add(CaseOneButton, proportion=0, flag=wx.LEFT, border=0)
        self.CSTbox.Add(CaseTwoButton, proportion=0, flag=wx.LEFT, border=0)
        self.CSTbox.Add(CaseThreeButton, proportion=0, flag=wx.LEFT, border=0)

        self.ISBbox = wx.BoxSizer(wx.VERTICAL)
        self.ISBbox.Add(IndexSystemButton, proportion=0, flag=wx.LEFT, border=0)

        self.BDAbox = wx.BoxSizer(wx.VERTICAL)
        self.BDAbox.Add(BigDataAnalysisButton, proportion=0, flag=wx.LEFT, border=0)

        self.CSbox = wx.BoxSizer(wx.VERTICAL)
        self.CSbox.Add(CaseShowButton, proportion=0, flag=wx.LEFT, border=0)
        self.CSbox.Add(self.CSTbox, proportion=0, flag=wx.LEFT, border=0)
        self.CSbox.Hide(self.CSTbox)

        self.hbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox.Add(self.ISBbox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.hbox.Add(self.BDAbox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.hbox.Add(self.CSbox, proportion=0, flag=wx.LEFT | wx.TOP, border=20)

        self.vbox = wx.BoxSizer()
        self.vbox.Add(self.hbox, proportion=0, flag=wx.ALL, border=10)

        self.Panel1.SetSizer(self.vbox)
        # ***************panel 1 box set**********************************************

        # ***************panel 2 box set**********************************************
        self.P2abox = wx.BoxSizer()
        self.P2abox.Add(self.sample, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.P2abox.Add(self.choices1, proportion=0, flag=wx.LEFT | wx.TOP, border=20)

        self.P2abox.Add(self.indexname, proportion=0, flag=wx.LEFT | wx.TOP, border=20)
        self.P2abox.Add(self.choices2, proportion=0, flag=wx.LEFT | wx.TOP, border=20)

        self.Panel2.SetSizer(self.P2abox)
        # ***************panel 2 box set**********************************************

        # ***************panel 3 box set**********************************************
        # ***************panel 3 box set**********************************************

        # ***************panel 4 box set**********************************************
        self.P4abox = wx.BoxSizer()
        self.P4abox.Add(self.bar, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        self.Panel4.SetSizer(self.P4abox)
        # ***************panel 4 box set**********************************************

        # ***************window box set**********************************************
        self.mbox = wx.BoxSizer(wx.VERTICAL)
        self.mbox.Add(self.Panel2, proportion=2, flag=wx.ALL | wx.EXPAND, border=10)
        self.mbox.Add(self.Panel3, proportion=20, flag=wx.ALL | wx.EXPAND, border=10)

        self.tbox = wx.BoxSizer()
        self.tbox.Add(self.Panel1, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.tbox.Add(self.mbox, proportion=5, flag=wx.ALL | wx.EXPAND, border=10)

        self.wbox = wx.BoxSizer(wx.VERTICAL)
        self.wbox.Add(self.tbox, proportion=10, flag=wx.ALL | wx.EXPAND, border=10)
        self.wbox.Add(self.Panel4, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)

        self.SetSizer(self.wbox)
        # ***************window box set**********************************************


    def IndexSystem(self, evt):
        pass

    def BigDataAnalysis(self,evt):
        BDA = BigDataAnalysis.BigDataAnalysis()
        BDA.Show()

    def CaseShow(self, evt):
        if(self.Cflag == 0):
            self.CSbox.Show(self.CSTbox)
            self.vbox.Layout()
            self.Cflag = 1
        else:
            self.CSbox.Hide(self.CSTbox)
            self.vbox.Layout()
            self.Cflag = 0


    def CaseOne(self, evt):
        case = CaseOne.CaseOne()
        case.Show()

    def CaseTwo(self, evt):
        case = CaseTwo.CaseTwo()
        case.Show()

    def CaseThree(self, evt):
        case = CaseThree.CaseThree()
        case.Show()

    def OnClose(self,evt):
        evt.Skip()

    def UpdateC2(self, evt):
        self.choices2.Set(self.sampleList2[self.sampleList1[self.choices1.GetStringSelection()]])
        self.P2abox.Layout()

    def Show_Content(self, con):
        self.bar.SetValue(con)
        self.bar.SetInsertionPoint(0)
        f = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.bar.SetStyle(0, self.bar.GetLastPosition(), wx.TextAttr("black", "white", f))




class log(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title=u"登陆",
                          size=(555, 200),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        account = wx.StaticText(self, -1, "Account:")
        password = wx.StaticText(self, -1, "Password:")

        self.Act = wx.TextCtrl(self, -1, "admin")
        self.paw = wx.TextCtrl(self, -1, "12345", style=wx.TE_PASSWORD)

        log_inbutton = wx.Button(self, label=u'登陆')
        log_inbutton.Bind(wx.EVT_BUTTON, self.log_in)

        exitbutton = wx.Button(self, label=u'退出')
        exitbutton.Bind(wx.EVT_BUTTON, self.exit_out)

        hbox = wx.BoxSizer(wx.VERTICAL)
        hbox.Add(account, proportion=0, flag=wx.EXPAND, border=10)
# coding:UTF-8
import sys
import wx
import time
import os
########################################################################
# set the file filter
wildcard1 = "Txt source (*.txt)|*.txt|"\
            "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Txt source (*.txt)|*.txt|"\
    "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"
########################################################################
class Demo(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title="Demo platform",
                          size=(1200, 1000),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Cflag = 0

        self.Panel1 = wx.Panel(self)
        self.Panel1.SetBackgroundColour('Red')

        self.Panel2 = wx.Panel(self)
        self.Panel2.SetBackgroundColour('Green')

        self.Panel3 = wx.Panel(self)
        self.Panel3.SetBackgroundColour('Blue')

        self.Panel4 = wx.Panel(self)
        self.Panel4.SetBackgroundColour('Yellow')

        #***************panel 1**********************************************
        IndexSystemButton = wx.Button(self.Panel1, label=u'指标体系')
        IndexSystemButton.Bind(wx.EVT_BUTTON, self.IndexSystem)

        BigDataAnalysisButton = wx.Button(self.Panel1, label=u'大数据分析')
        BigDataAnalysisButton.Bind(wx.EVT_BUTTON, self.BigDataAnalysis)

        CaseShowButton = wx.Button(self.Panel1, label=u'应用展示')
        CaseShowButton.Bind(wx.EVT_BUTTON, self.CaseShow)

        CaseOneButton = wx.Button(self.Panel1, label=u'应用1:盲点检测展示')
        CaseOneButton.Bind(wx.EVT_BUTTON, self.CaseOne)
        CaseTwoButton = wx.Button(self.Panel1, label=u'应用2:用户密度预测')
        CaseTwoButton.Bind(wx.EVT_BUTTON, self.CaseTwo)
        CaseThreeButton = wx.Button(self.Panel1, label=u'应用3:异常信令事件分析')
        CaseThreeButton.Bind(wx.EVT_BUTTON, self.CaseThree)
        # ***************panel 1**********************************************
        # ***************panel 2  part 1**********************************************
        self.sampleList1 = {
            u"接入类指标": 0,
            u"保持类指标": 1,
            u"信道类指标": 2,
            u"用户分布类指标": 3,
            u"用户感知类指标": 4,
            u"其他类指标": 5
        }
        self.sampleList2 = [
            [u"业务请求时延", u"加密时延", u"身份识别时延", u"TMSI重分配时延", u"语音寻呼时延"],
            [u"剔除UI的无线掉线率"],
            [u"阴影效应", u"多普勒效应", u"远近效应"],
            [u"用户密度", u"用户密度对通信质量影响"],
            [u"低接通用户数劣化指标", u"高掉线用户数劣化指标", u"高流量用户时延劣化指标", u"高流量用户接通劣化指标",
             u"高时延用户数劣化指标"],
            [u"上行业务质量", u"上行噪声影响", u"上行干扰对弱覆盖的影响", u"下行业务弱覆盖影响"]
        ]
        self.sample = wx.StaticText(self.Panel2, -1, u"指标类型:", style=wx.ALIGN_CENTER)
        self.choices1 = wx.Choice(self.Panel2, -1, choices=self.sampleList1.keys(), style=wx.ALIGN_CENTER)

        self.indexname = wx.StaticText(self.Panel2, -1, u"指标名称:", style=wx.ALIGN_CENTER)
        self.choices2 = wx.Choice(self.Panel2, -1, choices=self.sampleList2[0], style=wx.ALIGN_CENTER)

        self.choices1.Bind(wx.EVT_CHOICE, self.UpdateC2)
        # ***************panel 2  part 1**********************************************
        # ***************panel 2  part 2**********************************************
        self.methods = wx.StaticText(self.Panel2, -1, u"计算方法:", style=wx.ALIGN_CENTER)
        self.sampleList3 = [u"常规方法", u"物化视图"]
        self.choices3 = wx.Choice(self.Panel2, -1, choices=self.sampleList3, style=wx.ALIGN_CENTER)

        self.InputBigDataButton = wx.Button(self.Panel2, label=u'导入数据')
        self.InputBigDataButton.Bind(wx.EVT_BUTTON, self.InputBigData)

        self.ShowDataButton = wx.Button(self.Panel2, label=u'显示数据')
        self.ShowDataButton.Bind(wx.EVT_BUTTON, self.ShowData)

        self.DataProcessButton = wx.Button(self.Panel2, label=u'数据操作')
        self.DataProcessButton.Bind(wx.EVT_BUTTON, self.DataProcess)

        self.ComputingButton = wx.Button(self.Panel2, label=u'开始计算并统计')
        self.ComputingButton.Bind(wx.EVT_BUTTON, self.Computing)
        # ***************panel 2  part 2**********************************************
        # ***************panel 2  part 3 --case 1**********************************************
        self.InputDataButton = wx.Button(self.Panel2, label=u'导入数据')
        self.InputDataButton.Bind(wx.EVT_BUTTON, self.InputData)

        self.ScreenDataButton = wx.Button(self.Panel2, label=u'筛选异常用户数据')
        self.ScreenDataButton.Bind(wx.EVT_BUTTON, self.ScreenData)

        self.BlindspotMonitorButton = wx.Button(self.Panel2, label=u'盲点检测')
        self.BlindspotMonitorButton.Bind(wx.EVT_BUTTON, self.BlindspotMonitor)

        self.ResultOutputButton = wx.Button(self.Panel2, label=u'结果输出')
        self.ResultOutputButton.Bind(wx.EVT_BUTTON, self.ResultOutput)
        # ***************panel 2  part 3 --case 1**********************************************
        # ***************panel 2  part 4 --case 2**********************************************
        self.InputUserDataButton = wx.Button(self.Panel2, label=u'导入用户数据')
        self.InputUserDataButton.Bind(wx.EVT_BUTTON, self.InputUserData)

        self.ScreenUserDataButton = wx.Button(self.Panel2, label=u'筛选异常用户数据')
        self.ScreenUserDataButton.Bind(wx.EVT_BUTTON, self.ScreenUserData)

        self.regions = wx.StaticText(self.Panel2, -1, u"用户区域选择:", style=wx.ALIGN_CENTER)
        self.sampleList4 = [u"区域1", u"区域2", u"区域3"]
        self.choices4 = wx.Choice(self.Panel2, -1, choices=self.sampleList4, style=wx.ALIGN_CENTER)

        self.UserPredictButton = wx.Button(self.Panel2, label=u'用户密度预测')
        self.UserPredictButton.Bind(wx.EVT_BUTTON, self.UserPredict)
        # ***************panel 2  part 4 --case 2**********************************************

        # ***************panel 3**********************************************
        # ***************panel 3**********************************************

        # ***************panel 4**********************************************
        #状态栏
        self.bar = wx.TextCtrl(self.Panel4, style=wx.TE_MULTILINE | wx.TE_RICH2)
        # ***************panel 4**********************************************

        # ***************panel 1 box set**********************************************
        self.CSTbox = wx.BoxSizer(wx.VERTICAL)
        self.CSTbox.Add(CaseOneButton, proportion=0, flag=wx.ALL, border=0)
        self.CSTbox.Add(CaseTwoButton, proportion=0, flag=wx.ALL, border=0)
        self.CSTbox.Add(CaseThreeButton, proportion=0, flag=wx.ALL, border=0)

        self.ISBbox = wx.BoxSizer(wx.VERTICAL)
        self.ISBbox.Add(IndexSystemButton, proportion=0, flag=wx.ALL, border=0)

        self.BDAbox = wx.BoxSizer(wx.VERTICAL)
        self.BDAbox.Add(BigDataAnalysisButton, proportion=0, flag=wx.ALL, border=0)

        self.CSbox = wx.BoxSizer(wx.VERTICAL)
        self.CSbox.Add(CaseShowButton, proportion=0, flag=wx.ALL, border=0)
        self.CSbox.Add(self.CSTbox, proportion=0, flag=wx.ALL, border=0)
        self.CSbox.Hide(self.CSTbox)

        self.hbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox.Add(self.ISBbox, proportion=0, flag=wx.ALL, border=10)
        self.hbox.Add(self.BDAbox, proportion=0, flag=wx.ALL, border=10)
        self.hbox.Add(self.CSbox, proportion=0, flag=wx.ALL, border=10)

        self.vbox = wx.BoxSizer()
        self.vbox.Add(self.hbox, proportion=0, flag=wx.ALL, border=10)

        self.Panel1.SetSizer(self.vbox)
        # ***************panel 1 box set**********************************************


        # ***************panel 2  part 1 box set**********************************************
        self.Labox = wx.BoxSizer()
        self.Labox.Add(self.sample, proportion=0, flag=wx.ALL, border=10)
        self.Labox.Add(self.choices1, proportion=0, flag=wx.ALL, border=10)

        self.Labox.Add(self.indexname, proportion=0, flag=wx.ALL, border=10)
        self.Labox.Add(self.choices2, proportion=0, flag=wx.ALL, border=10)
        # ***************panel 2 part 1 box set**********************************************
        # ***************panel 2 part 2 box set**********************************************
        self.DPbox = wx.BoxSizer()
        self.DPbox.Add(self.methods, proportion=0, flag=wx.ALL, border=10)
        self.DPbox.Add(self.choices3, proportion=0, flag=wx.ALL, border=10)

        self.DPAbox = wx.BoxSizer()
        self.DPAbox.Add(self.InputBigDataButton, proportion=0, flag=wx.LEFT, border=10)
        self.DPAbox.Add(self.ShowDataButton, proportion=0, flag=wx.LEFT, border=10)
        self.DPAbox.Add(self.DataProcessButton, proportion=0, flag=wx.LEFT, border=10)
        self.DPAbox.Add(self.ComputingButton, proportion=0, flag=wx.LEFT, border=10)

        self.DPbox.Add(self.DPAbox, proportion=0, flag=wx.ALL, border=10)
        # ***************panel 2 part 2 box set**********************************************
        # ***************panel 2 part 3 box set**********************************************
        self.IDbox = wx.BoxSizer(wx.VERTICAL)
        self.IDbox.Add(self.InputDataButton, proportion=0, flag=wx.LEFT, border=0)

        self.SDbox = wx.BoxSizer(wx.VERTICAL)
        self.SDbox.Add(self.ScreenDataButton, proportion=0, flag=wx.LEFT, border=0)

        self.BMbox = wx.BoxSizer(wx.VERTICAL)
        self.BMbox.Add(self.BlindspotMonitorButton, proportion=0, flag=wx.LEFT, border=0)

        self.RObox = wx.BoxSizer(wx.VERTICAL)
        self.RObox.Add(self.ResultOutputButton, proportion=0, flag=wx.LEFT, border=0)

        self.Bhbox = wx.BoxSizer()
        self.Bhbox.Add(self.IDbox, proportion=0, flag=wx.ALL, border=10)
        self.Bhbox.Add(self.SDbox, proportion=0, flag=wx.ALL, border=10)
        self.Bhbox.Add(self.BMbox, proportion=0, flag=wx.ALL, border=10)
        self.Bhbox.Add(self.RObox, proportion=0, flag=wx.ALL, border=10)

        self.Bvbox = wx.BoxSizer()
        self.Bvbox.Add(self.Bhbox, proportion=0, flag=wx.ALL, border=0)
        # ***************panel 2 part 3 box set**********************************************
        # ***************panel 2 part 4 box set**********************************************
        self.UPbox = wx.BoxSizer()
        self.UPbox.Add(self.InputUserDataButton, proportion=0, flag=wx.ALL, border=10)
        self.UPbox.Add(self.ScreenUserDataButton, proportion=0, flag=wx.ALL, border=10)
        self.UPbox.Add(self.regions, proportion=0, flag=wx.ALL, border=10)
        self.UPbox.Add(self.choices4, proportion=0, flag=wx.ALL, border=10)
        self.UPbox.Add(self.UserPredictButton, proportion=0, flag=wx.ALL, border=10)

        # ***************panel 2 part 4 box set**********************************************
        # ***************panel 2 box set**********************************************
        self.P2box = wx.BoxSizer(wx.VERTICAL)
        self.P2box.Add(self.Labox, proportion=0, flag=wx.ALL, border=0)
        self.P2box.Add(self.DPbox, proportion=0, flag=wx.ALL, border=0)
        self.P2box.Add(self.Bvbox, proportion=0, flag=wx.ALL, border=0)
        self.P2box.Add(self.UPbox, proportion=0, flag=wx.ALL, border=0)

        self.P2box.Hide(self.Labox)
        self.P2box.Hide(self.DPbox)
        self.P2box.Hide(self.Bvbox)
        self.P2box.Hide(self.UPbox)

        self.Panel2.SetSizer(self.P2box)
        # ***************panel 2 box set**********************************************
        # ***************panel 3 box set**********************************************
        # ***************panel 3 box set**********************************************

        # ***************panel 4 box set**********************************************
        self.P4abox = wx.BoxSizer()
        self.P4abox.Add(self.bar, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        self.Panel4.SetSizer(self.P4abox)
        # ***************panel 4 box set**********************************************

        # ***************window box set**********************************************
        self.mbox = wx.BoxSizer(wx.VERTICAL)
        self.mbox.Add(self.Panel2, proportion=2, flag=wx.ALL | wx.EXPAND, border=10)
        self.mbox.Add(self.Panel3, proportion=20, flag=wx.ALL | wx.EXPAND, border=10)

        self.tbox = wx.BoxSizer()
        self.tbox.Add(self.Panel1, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.tbox.Add(self.mbox, proportion=5, flag=wx.ALL | wx.EXPAND, border=10)

        self.wbox = wx.BoxSizer(wx.VERTICAL)
        self.wbox.Add(self.tbox, proportion=10, flag=wx.ALL | wx.EXPAND, border=10)
        self.wbox.Add(self.Panel4, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)

        self.SetSizer(self.wbox)
        # ***************window box set**********************************************


    def IndexSystem(self, evt):
        self.P2box.Hide(self.Bvbox)
        self.P2box.Hide(self.DPbox)
        self.P2box.Hide(self.UPbox)
        self.P2box.Show(self.Labox)
        self.wbox.Layout()

    def BigDataAnalysis(self,evt):
        self.P2box.Hide(self.Labox)
        self.P2box.Hide(self.Bvbox)
        self.P2box.Hide(self.UPbox)
        self.P2box.Show(self.DPbox)
        self.wbox.Layout()

    def CaseShow(self, evt):
        if(self.Cflag == 0):
            self.CSbox.Show(self.CSTbox)
            self.vbox.Layout()
            self.Cflag = 1
        else:
            self.CSbox.Hide(self.CSTbox)
            self.vbox.Layout()
            self.Cflag = 0

    def CaseOne(self, evt):
        self.P2box.Hide(self.Labox)
        self.P2box.Hide(self.DPbox)
        self.P2box.Hide(self.UPbox)
        self.P2box.Show(self.Bvbox)
        self.wbox.Layout()

    def CaseTwo(self, evt):
        self.P2box.Hide(self.Labox)
        self.P2box.Hide(self.DPbox)
        self.P2box.Hide(self.Bvbox)
        self.P2box.Show(self.UPbox)
        self.wbox.Layout()

    def CaseThree(self, evt):
        pass

    def InputBigData(self, evt):
        path111 = cur_file_dir()
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile=path111,
            wildcard=wildcard1,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            # paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            temp = paths[0]
            if (len(paths) > 1):
                self.Show_Content("Only open one file each time!")
                return False
            tem = temp.split('.')
            print tem
            if (tem[-1] != 'txt'):
                self.Show_Content("Only open .txt file!")
                return False
            # print "You chose the following file(s):"
            # set the value of TextCtrl[filename]
            # self.filename.SetValue(temp)
            # set the value to the TextCtrl[contents]
            file = open(temp)
            self.Show_Content(file.read().decode('utf-8'))
            file.close()
        dlg.Destroy()

    def InputData(self, evt):
        path111 = cur_file_dir()
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile=path111,
            wildcard=wildcard1,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            # paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            temp = paths[0]
            if (len(paths) > 1):
                self.Show_Content("Only open one file each time!")
                return False
            tem = temp.split('.')
            print tem
            if (tem[-1] != 'txt'):
                self.Show_Content("Only open .txt file!")
                return False
            # print "You chose the following file(s):"
            # set the value of TextCtrl[filename]
            # self.filename.SetValue(temp)
            # set the value to the TextCtrl[contents]
            file = open(temp)
            self.Show_Content(file.read().decode('utf-8'))
            file.close()
        dlg.Destroy()

    def InputUserData(self, evt):
        path111 = cur_file_dir()
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile=path111,
            wildcard=wildcard1,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            # paths = dlg.GetPaths()
            paths = dlg.GetPaths()
            temp = paths[0]
            if (len(paths) > 1):
                self.Show_Content("Only open one file each time!")
                return False
            tem = temp.split('.')
            print tem
            if (tem[-1] != 'txt'):
                self.Show_Content("Only open .txt file!")
                return False
            # print "You chose the following file(s):"
            # set the value of TextCtrl[filename]
            # self.filename.SetValue(temp)
            # set the value to the TextCtrl[contents]
            file = open(temp)
            self.Show_Content(file.read().decode('utf-8'))
            file.close()
        dlg.Destroy()

    def DataProcess(self, evt):
        pass

    def ShowData(self, evt):
        pass

    def Computing(self, evt):
        pass

    def ScreenData(self, evt):
        pass

    def BlindspotMonitor(self, evt):
        pass

    def ResultOutput(self, evt):
        pass

    def ScreenUserData(self, evt):
        pass

    def UserPredict(self, evt):
        pass

    def OnClose(self,evt):
        evt.Skip()

    def UpdateC2(self, evt):
        self.choices2.Set(self.sampleList2[self.sampleList1[self.choices1.GetStringSelection()]])
        self.P2abox.Layout()

    def Show_Content(self, con):
        self.bar.SetValue(con)
        self.bar.SetInsertionPoint(0)
        f = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.bar.SetStyle(0, self.bar.GetLastPosition(), wx.TextAttr("black", "white", f))




class log(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title=u"登陆",
                          size=(555, 200),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        account = wx.StaticText(self, -1, "Account:")
        password = wx.StaticText(self, -1, "Password:")

        self.Act = wx.TextCtrl(self, -1, "admin")
        self.paw = wx.TextCtrl(self, -1, "12345", style=wx.TE_PASSWORD)

        log_inbutton = wx.Button(self, label=u'登陆')
        log_inbutton.Bind(wx.EVT_BUTTON, self.log_in)

        exitbutton = wx.Button(self, label=u'退出')
        exitbutton.Bind(wx.EVT_BUTTON, self.exit_out)

        hbox = wx.BoxSizer(wx.VERTICAL)
        hbox.Add(account, proportion=0, flag=wx.EXPAND, border=10)
        hbox.Add(self.Act, proportion=0, flag=wx.EXPAND)
        hbox.Add(password, proportion=0, flag=wx.EXPAND, border=10)
        hbox.Add(self.paw, proportion=0, flag=wx.EXPAND)
        hbox.Add(log_inbutton, proportion=0, flag=wx.EXPAND, border=10)
        hbox.Add(exitbutton, proportion=0, flag=wx.EXPAND, border=10)
        #vbox = wx.BoxSizer(wx.VERTICAL)
        #vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL, border=10)
        #vbox.Add(contents, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=10)
        self.SetSizer(hbox)

    def log_in(self, event):
        if self.Act.GetValue() == 'admin' and self.paw.GetValue() == "12345":
            self.Show(False)
            spider_now = Demo()
            spider_now.Show()
        else:
            error_now = error()
            error_now.Show()

    def exit_out(self, event):
        self.Show(False)

    def OnClose(self, evt):
        evt.Skip()

class error(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title="error",
                          size=(300, 200),
                          style=wx.DEFAULT_FRAME_STYLE)
        b = wx.Button(self, -1, u"登陆信息有误！\n请重新输出！", (50, 50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)
    def OnButton(self, event):
        self.Show(False)


def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

# 打印时间
def show_time():
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    print time.strftime(ISOTIMEFORMAT, time.localtime())
app = wx.App()
#frame = log() #调试用，跳过登陆界面
frame = Demo()
frame.Show()
app.MainLoop()
