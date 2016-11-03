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

        self.hbox = wx.BoxSizer()

        self.ibox = wx.BoxSizer()

        self.tbox = wx.BoxSizer()

        self.vbox = wx.BoxSizer()

    def LogMessage(self, msg):
        self.bar.AppendText(msg)

    def OnClose(self,evt):
        evt.Skip()




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
frame = log()
frame.Show()
app.MainLoop()
