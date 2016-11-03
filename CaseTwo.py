# coding:UTF-8
import wx
import os,sys

########################################################################
# set the file filter
wildcard1 = "Txt source (*.txt)|*.txt|"\
            "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Txt source (*.txt)|*.txt|"\
    "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"
########################################################################
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

        self.Panel4 = wx.Panel(self)
        self.Panel4.SetBackgroundColour('Yellow')
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
        # ***************panel 4**********************************************
        # 状态栏
        self.bar = wx.TextCtrl(self.Panel4, style=wx.TE_MULTILINE | wx.TE_RICH2)
        # ***************panel 4**********************************************
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
            #self.filename.SetValue(temp)
            # set the value to the TextCtrl[contents]
            file = open(temp)
            self.Show_Content(file.read().decode('utf-8'))
            file.close()
        dlg.Destroy()

    def ScreenData(self, evt):
        pass

    def BlindspotMonitor(self, evt):
        pass

    def ResultOutput(self, evt):
        pass

    def Show_Content(self, con):
        self.bar.SetValue(con)
        self.bar.SetInsertionPoint(0)
        f = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.bar.SetStyle(0, self.bar.GetLastPosition(), wx.TextAttr("black", "white", f))

    def OnClose(self, evt):
        evt.Skip()

def cur_file_dir():
    # 获取脚本路径
    path = sys.path[0]
    # 判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)
