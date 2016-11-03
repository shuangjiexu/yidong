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
