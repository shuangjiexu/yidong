# coding:UTF-8
import sys
import wx
import time
import os
import threading
import random
########################################################################
# set the file filter
wildcard1 = "Txt source (*.txt)|*.txt|"\
            "All files (*.*)|*.*|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
wildcard2 = "Txt source (*.txt)|*.txt|"\
    "Python source (*.py; *.pyc)|*.py;*.pyc|" \
            "All files (*.*)|*.*"
########################################################################
class Computing(threading.Thread):
    """
    This computing bigdata thread.
    """
    def __init__(self, filePath, colNum,flag, window):
        threading.Thread.__init__(self)
        self.filePath = filePath
        self.window = window
        self.colNum = colNum
        self.flag = flag
        self.messageDelay = 0.1 + 2.0 * random.random()
        #初始化实例时即可开始run
        self.start()

    def run(self):
        try:
            if(self.flag == 0):
                msg = u"开始常规数据计算!"
                wx.CallAfter(self.window.LogMessage, msg)
                print self.filePath
                print self.colNum
                fout = open(self.filePath)
                contents = fout.readlines()[:self.colNum]
                temp = 0
                #progressMax = 1000#设置进度条长度
                #创建进度条
                #dialog = wx.ProgressDialog(u"大数据计算", u"正在计算", progressMax,
                 #                          style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME)
                keepGoing = True
                i = 0
                for content in contents:
                    if (i%1000 == 0):
                        msg = u"正在计算第" + str(i/1000 + 1) + u"000行数据！"
                        wx.CallAfter(self.window.LogMessage, msg)
                    data = content.rsplit(" ")
                    diaoxian = (float(data[1]) - float(data[2])) / (float(data[3]) - float(data[4].rstrip("\n")))
                    temp += diaoxian
                    i+=1
                    #count = count + 1
                    #keepGoing = dialog.Update(count)
                temp /= self.colNum
                print temp
                fout = open("view.txt", 'w+')
                fout.write(str(self.colNum) +" "+ str(temp))
                fout.close()
                #dialog.Destroy()#结束进度条
                msg = u"数据计算结束!"
                wx.CallAfter(self.window.LogMessage, msg)
            elif(self.flag == 1):
                msg = u"开始使用物化视图方法进行数据计算!"
                wx.CallAfter(self.window.LogMessage, msg)
                ffout = open("view.txt", 'r+')
                view = ffout.readline().split(' ')
                if(self.colNum >= int(view[0])):
                    msg = u"找到可用视图!"
                    wx.CallAfter(self.window.LogMessage, msg)
                    fout = open(self.filePath)
                    contents = fout.readlines()[:self.colNum]
                    temp = 0
                    #progressMax = 1000  # 设置进度条长度
                    # 创建进度条
                    #dialog = wx.ProgressDialog(u"大数据计算", u"正在计算", progressMax,
                     #                          style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME)
                    #keepGoing = True
                    count = 1
                    #已经计算好的掉线率
                    otemp = float(view[1])
                    onum = int(view[0])
                    i = onum
                    for content in contents[onum:]:
                        #print content
                        if (i % 1000 == 0):
                            msg = u"正在计算第" + str(i/1000 + 1) + u"000行数据！"
                            wx.CallAfter(self.window.LogMessage, msg)
                        data = content.rsplit(" ")
                        diaoxian = (float(data[1]) - float(data[2])) / (float(data[3]) - float(data[4].rstrip("\n")))
                        temp += diaoxian
                        i+=1
                        #keepGoing = dialog.Update(count)
                    temp += onum * otemp
                    temp /= self.colNum
                    print temp
                    fout = open("view.txt", 'w+')
                    fout.write(str(self.colNum) + " " + str(temp))
                    fout.close()
                    #dialog.Destroy()  # 结束进度条
                    msg = u"数据计算结束!使用物化视图计算方法！"
                    wx.CallAfter(self.window.LogMessage, msg)
                else:
                    msg = u"未找到可用视图!"
                    wx.CallAfter(self.window.LogMessage, msg)
                    fout = open(self.filePath)
                    contents = fout.readlines()[:self.colNum]
                    temp = 0
                    i = 0
                    #progressMax = 1000  # 设置进度条长度
                    # 创建进度条
                    #dialog = wx.ProgressDialog(u"大数据计算", u"正在计算", progressMax,
                     #                          style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME)
                    for content in contents:
                        if(i%1000 == 0):
                            msg = u"正在计算第" + str(i/1000 + 1) + u"000行数据！"
                            wx.CallAfter(self.window.LogMessage, msg)
                        data = content.rsplit(" ")
                        diaoxian = (float(data[1]) - float(data[2])) / (float(data[3]) - float(data[4].rstrip("\n")))
                        temp += diaoxian
                        i+=1
                    temp /= self.colNum
                    print temp
                    fout = open("view.txt", 'w+')
                    fout.write(str(self.colNum) + " " + str(temp))
                    fout.close()
                    #dialog.Destroy()  # 结束进度条
                    msg = u"数据计算结束!未查找到视图，使用常规计算方法！"
                    wx.CallAfter(self.window.LogMessage, msg)
        except:
            msg = u"未进行显示数据操作！"
            wx.CallAfter(self.window.LogMessage, msg)

class OpenFile(threading.Thread):
    """
    This open bigdata file thread.
    """
    def __init__(self, filePath, colNum,window):
        threading.Thread.__init__(self)
        self.filePath = filePath
        self.window = window
        self.colNum = colNum
        self.messageDelay = 0.1 + 2.0 * random.random()
        #初始化实例时即可开始run
        self.start()

    def run(self):
        try:
            msg = u"数据读取开始!"
            wx.CallAfter(self.window.LogMessage, msg)
            file = open(self.filePath)
            contentList = file.readlines()
            self.contentSelected = []
            content = ''
            if self.colNum > len(contentList):
                self.colNum = len(contentList)
            #progressMax = 1000 # 设置进度条长度
            # 创建进度条
            #dialog = wx.ProgressDialog(u"大数据导入", u"正在导入", progressMax,
            #                          style=wx.PD_CAN_ABORT | wx.PD_ELAPSED_TIME)
            #keepGoing = True
            #count = 0
            for i in range(self.colNum):
                #count = count + 1
                #keepGoing = dialog.Update(count)
                if(i%1000 == 0):
                    msg = u"正在读取前" + str(i/1000 + 1) +u"000行数据！"
                    wx.CallAfter(self.window.LogMessage, msg)
                content = content + contentList[i]
                self.contentSelected.append(contentList[i])
            wx.CallAfter(self.window.Set_grids, content.decode('utf-8'))
            #self.window.Set_Grids(content.decode('utf-8'))
            #dialog.Destroy()  # 结束进度条
            file.close()

            msg = u"数据读取结束!"
            wx.CallAfter(self.window.LogMessage, msg)
            msg = u"当前处理文件：" + self.filePath + "\t" + u"显示行数：" + str(self.colNum)
            wx.CallAfter(self.window.LogMessage, msg)
        except:
            msg = u"未进行显示数据操作！"
            wx.CallAfter(self.window.LogMessage, msg)

class Demo(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,
                          title="Demo platform",
                          size=(1200, 1000),
                          style=wx.DEFAULT_FRAME_STYLE)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Cflag = 0

        #self.SetBackgroundColour("White")
        self.Panel1 = wx.Panel(self)
        #self.Panel1.SetBackgroundColour('Red')

        self.Panel2 = wx.Panel(self)
        #self.Panel2.SetBackgroundColour('Green')

        self.Panel3 = wx.Panel(self)
        #self.Panel3.SetBackgroundColour('Blue')

        self.Panel4 = wx.Panel(self)
        #self.Panel4.SetBackgroundColour('Yellow')

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

        self.InputBigDataButton = wx.Button(self.Panel2, label=u'添加数据源')
        self.InputBigDataButton.Bind(wx.EVT_BUTTON, self.InputBigData)
        # init opend file list of BigDataAnalysis
        self.BigDataAnalysisFileList = []

        self.ShowDataButton = wx.Button(self.Panel2, label=u'导入并显示数据')
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

        self.times1 = wx.StaticText(self.Panel2, -1, u"时段选择:", style=wx.ALIGN_CENTER)
        self.sampleList6 = [u"时段1", u"时段2", u"时段3"]
        self.choices6 = wx.Choice(self.Panel2, -1, choices=self.sampleList6, style=wx.ALIGN_CENTER)

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

        self.times2 = wx.StaticText(self.Panel2, -1, u"时段选择:", style=wx.ALIGN_CENTER)
        self.sampleList5 = [u"时段1", u"时段2", u"时段3"]
        self.choices5 = wx.Choice(self.Panel2, -1, choices=self.sampleList5, style=wx.ALIGN_CENTER)

        self.UserPredictButton = wx.Button(self.Panel2, label=u'用户密度预测')
        self.UserPredictButton.Bind(wx.EVT_BUTTON, self.UserPredict)
        # ***************panel 2  part 4 --case 2**********************************************

        # ***************panel 3**********************************************
        self.grids = wx.TextCtrl(self.Panel3, -1, style=wx.TE_MULTILINE | wx.TE_RICH2)
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
        self.Bhbox.Add(self.times1, proportion=0, flag=wx.ALL, border=10)
        self.Bhbox.Add(self.choices6, proportion=0, flag=wx.ALL, border=10)
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
        self.UPbox.Add(self.times2, proportion=0, flag=wx.ALL, border=10)
        self.UPbox.Add(self.choices5, proportion=0, flag=wx.ALL, border=10)
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
        self.P3abox = wx.BoxSizer()
        self.P3abox.Add(self.grids, proportion=1, flag=wx.EXPAND | wx.ALL, border=20)

        self.Panel3.SetSizer(self.P3abox)
        # ***************panel 3 box set**********************************************

        # ***************panel 4 box set**********************************************
        self.P4abox = wx.BoxSizer()
        self.P4abox.Add(self.bar, proportion=1, flag=wx.EXPAND | wx.ALL, border=0)

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
            if (tem[-1] != 'txt'):
                self.Show_Content("Only open .txt file!")
                return False
            # print "You chose the following file(s):"
            # set the value of TextCtrl[filename]
            # self.filename.SetValue(temp)
            # set the value to the TextCtrl[contents]
            file = open(temp)
            #self.Show_Content(file.read().decode('utf-8'))
            file.close()
            self.BigDataAnalysisFileList.append(temp)
            print self.BigDataAnalysisFileList
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
            if (tem[-1] != 'txt'):
                self.Show_Content("Only open .txt file!")
                return False
            # print "You chose the following file(s):"
            # set the value of TextCtrl[filename]
            # self.filename.SetValue(temp)
            # set the value to the TextCtrl[contents]
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
        ds = DataProcessDialog(self)
        ds.Show()

    def ComputingSetting(self, operationNum):
        self.ComputingNum = operationNum

    def ShowData(self, evt):
        ds = DataShowDialog(self)
        ds.Show()

    def ShowGrid(self,filePath, colNum):
        '''
        show content according to DataShowDialog
        filePath: file path to read
        colNum: lines to show
        '''

        self.filePath = filePath
        self.colNum = colNum
        #实例化导入数据对象
        OpenFile(self.filePath,self.colNum,self)

    def Computing(self, evt):
        try:
            self.selected = self.choices3.GetSelection()
            print type(self.selected)
            print self.selected
            if(self.selected== 0):
                Computing(self.filePath, self.colNum ,0, self)
            elif(self.selected == 1):
                Computing(self.filePath, self.colNum, 1, self)
            else:
                self.Show_Content("Error!", 1)
        except:
            self.Show_Content("Error!", 1)

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
        self.P2box.Layout()

    def Set_grids(self, con):
        self.grids.SetValue(con)
        self.grids.SetInsertionPoint(0)
        f = wx.Font(18, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.grids.SetStyle(0, self.grids.GetLastPosition(), wx.TextAttr("black", "white", f))

    def Show_Content(self, con, flag = 0):
        if(flag == 0):
            self.bar.AppendText(con)
            ISOTIMEFORMAT = '%Y-%m-%d %X'
            cc = time.strftime(ISOTIMEFORMAT, time.localtime())
            self.bar.AppendText("   "+cc + "\n")
            self.bar.SetInsertionPoint(0)
            f = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
            self.bar.SetStyle(0, self.bar.GetLastPosition(), wx.TextAttr("black", "white", f))
        else:
            self.bar.SetValue(con)
            self.bar.SetInsertionPoint(0)
            f = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
            self.bar.SetStyle(0, self.bar.GetLastPosition(), wx.TextAttr("black", "white", f))

    def show_time():
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        print time.strftime(ISOTIMEFORMAT, time.localtime())
        return time.strftime(ISOTIMEFORMAT, time.localtime())

    def LogMessage(self, msg):
        self.bar.AppendText(msg)
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        cc = time.strftime(ISOTIMEFORMAT, time.localtime())
        self.bar.AppendText("   " + cc + "\n")
        #self.bar.SetInsertionPoint(0)
        f = wx.Font(15, wx.ROMAN, wx.NORMAL, wx.NORMAL, False)
        self.bar.SetStyle(0, self.bar.GetLastPosition(), wx.TextAttr("black", "white", f))

class DataShowDialog(wx.Dialog):
    def __init__(self, parent):
        super(DataShowDialog, self).__init__(parent, title = u"大数据分析-数据显示", size = (700,300))
        self.parent = parent

        # get file list from parent
        self.fileList = parent.BigDataAnalysisFileList

        self.Panel_ds = wx.Panel(self)
        #self.Panel_ds.SetBackgroundColour('Red')

        self.Panel_ds1 = wx.Panel(self)
        #self.Panel_ds1.SetBackgroundColour('Green')

        self.Panel_ds2 = wx.Panel(self)
        #self.Panel_ds2.SetBackgroundColour('Blue')


        self.title = wx.StaticText(self.Panel_ds1, -1, u"大数据平台数据显示设置:", style=wx.ALIGN_CENTER)

        self.DataSource = wx.StaticText(self.Panel_ds, -1, u"数据源选择:", style=wx.ALIGN_CENTER)
        self.choices = wx.Choice(self.Panel_ds, -1, choices=self.fileList, style=wx.ALIGN_CENTER)

        self.datacols = wx.StaticText(self.Panel_ds, -1, u"数据行数:", style=wx.ALIGN_CENTER)
        self.DataCols = wx.TextCtrl(self.Panel_ds, -1, r'500000')

        self.SetButton = wx.Button(self.Panel_ds2, label=u'设置')
        self.SetButton.Bind(wx.EVT_BUTTON, self.Set)
        self.exitbutton = wx.Button(self.Panel_ds2, label=u'退出')
        self.exitbutton.Bind(wx.EVT_BUTTON, self.exit_out)
        #boxSizer set*********************************

        self.P1box = wx.BoxSizer()
        self.P1box.Add(self.title, proportion=0, flag=wx.ALL, border=10)
        self.Panel_ds1.SetSizer(self.P1box)

        self.P2box = wx.BoxSizer(wx.VERTICAL)
        self.P2box.Add(self.SetButton, proportion=0, flag=wx.ALL, border=10)
        self.P2box.Add(self.exitbutton, proportion=0, flag=wx.ALL, border=10)
        self.Panel_ds2.SetSizer(self.P2box)

        self.P221box = wx.BoxSizer()
        self.P221box.Add(self.DataSource, proportion=0, flag=wx.ALL, border=10)
        self.P221box.Add(self.choices, proportion=0, flag=wx.ALL, border=10)
        self.P222box = wx.BoxSizer()
        self.P222box.Add(self.datacols, proportion=0, flag=wx.ALL, border=10)
        self.P222box.Add(self.DataCols, proportion=0, flag=wx.ALL, border=10)

        self.P22box = wx.BoxSizer(wx.VERTICAL)
        self.P22box.Add(self.P221box, proportion=0, flag=wx.ALL, border=10)
        self.P22box.Add(self.P222box, proportion=0, flag=wx.ALL, border=10)
        self.Panel_ds.SetSizer(self.P22box)

        self.P3box = wx.BoxSizer()
        self.P3box.Add(self.Panel_ds, proportion=0, flag=wx.ALL, border=10)
        self.P3box.Add(self.Panel_ds2, proportion=0, flag=wx.ALL, border=10)

        self.Pbox = wx.BoxSizer(wx.VERTICAL)
        self.Pbox.Add(self.Panel_ds1, proportion=0, flag=wx.ALL, border=10)
        self.Pbox.Add(self.P3box, proportion=0, flag=wx.ALL, border=10)

        self.SetSizer(self.Pbox)

    def Set(self, evt):
        self.selected = self.choices.GetSelection()
        filePath = self.fileList[self.selected]
        self.Show(False)
        self.parent.ShowGrid(filePath, int(self.DataCols.GetValue()))


    def exit_out(self, event):
        self.Show(False)

    def OnClose(self, evt):
        evt.Skip()

class DataProcessDialog(wx.Dialog):
    def __init__(self, parent):
        super(DataProcessDialog, self).__init__(parent, title = u"大数据分析-数据显示", size = (500,300))
        self.parent = parent

        self.Panel_ds = wx.Panel(self)
        #self.Panel_ds.SetBackgroundColour('Red')

        self.Panel_ds1 = wx.Panel(self)
        #self.Panel_ds1.SetBackgroundColour('Green')

        self.Panel_ds2 = wx.Panel(self)
        #self.Panel_ds2.SetBackgroundColour('Blue')

        self.typeList = [u'求和', u'累乘', u'掉线率计算']

        self.title = wx.StaticText(self.Panel_ds1, -1, u"大数据平台数据操作设置:", style=wx.ALIGN_CENTER)

        self.DataSource = wx.StaticText(self.Panel_ds, -1, u"数据操作类型选择:", style=wx.ALIGN_CENTER)
        self.choices = wx.Choice(self.Panel_ds, -1, choices=self.typeList, style=wx.ALIGN_CENTER)

        self.SetButton = wx.Button(self.Panel_ds2, label=u'设置')
        self.SetButton.Bind(wx.EVT_BUTTON, self.Set)
        self.exitbutton = wx.Button(self.Panel_ds2, label=u'退出')
        self.exitbutton.Bind(wx.EVT_BUTTON, self.exit_out)
        #boxSizer set*********************************

        self.P1box = wx.BoxSizer()
        self.P1box.Add(self.title, proportion=0, flag=wx.ALL, border=10)
        self.Panel_ds1.SetSizer(self.P1box)

        self.P2box = wx.BoxSizer(wx.VERTICAL)
        self.P2box.Add(self.SetButton, proportion=0, flag=wx.ALL, border=10)
        self.P2box.Add(self.exitbutton, proportion=0, flag=wx.ALL, border=10)
        self.Panel_ds2.SetSizer(self.P2box)

        self.P221box = wx.BoxSizer()
        self.P221box.Add(self.DataSource, proportion=0, flag=wx.ALL, border=10)
        self.P221box.Add(self.choices, proportion=0, flag=wx.ALL, border=10)
        self.P222box = wx.BoxSizer()

        self.P22box = wx.BoxSizer(wx.VERTICAL)
        self.P22box.Add(self.P221box, proportion=0, flag=wx.ALL, border=10)
        self.P22box.Add(self.P222box, proportion=0, flag=wx.ALL, border=10)
        self.Panel_ds.SetSizer(self.P22box)

        self.P3box = wx.BoxSizer()
        self.P3box.Add(self.Panel_ds, proportion=0, flag=wx.ALL, border=10)
        self.P3box.Add(self.Panel_ds2, proportion=0, flag=wx.ALL, border=10)

        self.Pbox = wx.BoxSizer(wx.VERTICAL)
        self.Pbox.Add(self.Panel_ds1, proportion=0, flag=wx.ALL, border=10)
        self.Pbox.Add(self.P3box, proportion=0, flag=wx.ALL, border=10)

        self.SetSizer(self.Pbox)

    def Set(self, evt):
        self.selected = self.choices.GetSelection()
        self.parent.ComputingSetting(int(self.selected))
        print self.typeList[self.selected]
        temp = self.parent.bar.GetValue()+"\n"+u"当前选择计算："+self.typeList[self.selected]
        self.parent.Show_Content(temp)
        self.Show(False)

    def exit_out(self, event):
        self.Show(False)

    def OnClose(self, evt):
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
#frame = log() #调试用，跳过登陆界面
frame = Demo()
frame.Show()
app.MainLoop()
