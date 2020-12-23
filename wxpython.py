#!/usr/bin/env python

'''
静态文本、可控文本、对话框、GetApp()
'''
import wx,time


class Frame(wx.Frame):
    def __init__(self):
        # super(Frame, self).__init__(self,parent=None,title ='備品識別系統',size=(900,600))
        # style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX
        wx.Frame.__init__(self, parent = None, title = u'備品識別系統', size = (1000,600))
        global current_app
        self.OptionPanel_1 = None
        self.OptionPanel_2 = None
        self.OptionPanel_3 = None
        self.setupStatusBar()  # 初始化狀態欄
        self.InitCelan()



    def InitCelan(self):
        # self.MPL = wx.Panel(self, -1)
        LeftPanel = wx.Panel(self,-1) # 左側導航畫板
        self.RightPanel = wx.Panel(self,-1)  # 右側顯示界面默認畫板
        


        # ***********************左側導航設置******************
        vboxnetA = wx.BoxSizer(wx.VERTICAL)  # 纵向box 
        self.HBoxPanel = wx.BoxSizer(wx.HORIZONTAL)  # 橫向box

        # 初始化按鈕
        LeftInput_Box = wx.StaticBox(LeftPanel, -1, u'功能選擇')
        menu_btn_1 = wx.Button(LeftPanel, -1, u'圖像收集')
        menu_btn_2 = wx.Button(LeftPanel, -1, u'模型訓練')
        menu_btn_3 = wx.Button(LeftPanel, -1, u'備品識別')

        # 按鈕添加到sizer
        LeftInput_Sizer = wx.StaticBoxSizer(LeftInput_Box, wx.VERTICAL)
        LeftInput_Sizer.Add(menu_btn_1,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=0)
        LeftInput_Sizer.Add(menu_btn_2,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=0)
        LeftInput_Sizer.Add(menu_btn_3,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=0)

        # siert添加到縱向box
        vboxnetA.Add(LeftInput_Sizer,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=0)
        # box添加到左側panel
        LeftPanel.SetSizer(vboxnetA)

        # 左側導航box添加到橫向panel
        self.HBoxPanel.Add(LeftPanel,proportion = 1, border = 2,flag = wx.ALL | wx.EXPAND)
        # 右側界面box添加到橫向panel
        self.HBoxPanel.Add(self.RightPanel,proportion = 4, border = 2,flag = wx.ALL | wx.EXPAND)

        # 右側畫板設置以及綁定左側導航的按鈕
        self.Bind(wx.EVT_BUTTON, self.Button1Event, menu_btn_1)  # 圖像收集點擊事件
        self.Bind(wx.EVT_BUTTON, self.Button2Event, menu_btn_2)  # 模型訓練點擊事件
        self.Bind(wx.EVT_BUTTON, self.Button3Event, menu_btn_3)  # 備品識別點擊事件
        self.SetSizer(self.HBoxPanel)

    # 圖像收集點擊事件
    def Button1Event(self, event):

        # 创建选项栏目面板
        # 點擊圖像收集,需要顯示的panel
        def init_1(self):
            self.OptionPanel_1 = wx.Panel(self)
            menu_btn_1 = wx.Button(self.OptionPanel_1, -1, u'這是圖像收集面板')

        if self.OptionPanel_1:
            pass
        elif self.OptionPanel_2:
            init_1(self)
            self.HBoxPanel.Replace(self.OptionPanel_2, self.OptionPanel_1)
        elif self.OptionPanel_3:
            init_1(self)
            self.HBoxPanel.Replace(self.OptionPanel_3, self.OptionPanel_1)
        else:
            init_1(self)
            self.HBoxPanel.Replace(self.RightPanel, self.OptionPanel_1)

        # 刪除其他畫板裡面的控件
        if self.OptionPanel_2:
            self.OptionPanel_2.DestroyChildren()
            self.OptionPanel_2 = None
        if self.OptionPanel_3:
            self.OptionPanel_3.DestroyChildren()
            self.OptionPanel_3 = None
        # 強制渲染
        self.SetSizer(self.HBoxPanel)
        self.HBoxPanel.Layout()
    # 模型訓練點擊事件
    def Button2Event(self, event):
        def init_2(self):
            self.OptionPanel_2 = wx.Panel(self)
            menu_btn_2 = wx.Button(self.OptionPanel_2, -1, u'這是模型訓練面板')
        
        if self.OptionPanel_2:
            pass
        elif self.OptionPanel_1:
            init_2(self)
            self.HBoxPanel.Replace(self.OptionPanel_1, self.OptionPanel_2)
        elif self.OptionPanel_3:
            init_2(self)
            self.HBoxPanel.Replace(self.OptionPanel_3, self.OptionPanel_2)
        else:
            init_2(self)
            self.HBoxPanel.Replace(self.RightPanel, self.OptionPanel_2)

        # 刪除其他畫板裡面的控件
        if self.OptionPanel_1:
            self.OptionPanel_1.DestroyChildren()
            self.OptionPanel_1 = None
        if self.OptionPanel_3:
            self.OptionPanel_3.DestroyChildren()
            self.OptionPanel_3 = None
        # 強制渲染
        self.SetSizer(self.HBoxPanel)
        self.HBoxPanel.Layout()
    # 備品識別點擊事件
    def Button3Event(self, event):
        def init_3(self):
            self.OptionPanel_3 = wx.Panel(self)
            menu_btn_3 = wx.Button(self.OptionPanel_3, -1, u'這是備品識別面板')

        if self.OptionPanel_3:
            pass
        elif self.OptionPanel_1:
            init_3(self)
            self.HBoxPanel.Replace(self.OptionPanel_1, self.OptionPanel_3)
        elif self.OptionPanel_2:
            init_3(self)
            self.HBoxPanel.Replace(self.OptionPanel_2, self.OptionPanel_3)
        else:
            init_3(self)
            self.HBoxPanel.Replace(self.RightPanel, self.OptionPanel_3)

        # 刪除其他畫板裡面的控件
        if self.OptionPanel_1:
            self.OptionPanel_1.DestroyChildren()
            self.OptionPanel_1 = None
        if self.OptionPanel_2:
            self.OptionPanel_2.DestroyChildren()
            self.OptionPanel_2 = None
        # 強制渲染
        self.SetSizer(self.HBoxPanel)
        self.HBoxPanel.Layout()

# ****************************************初始化狀態欄********************************
    # 初始化状态栏
    def setupStatusBar(self):
        # 状态栏
        sb = self.CreateStatusBar(2)  # 2代表将状态栏分为两个
        self.SetStatusWidths([-1, -4])  # 比例为1：2
        self.SetStatusText("Ready", 0)  # 0代表第一个栏，Ready为内容
        # timmer
        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000, wx.TIMER_CONTINUOUS)
        self.Notify()

    # 实时显示时间
    def Notify(self):
        t = time.localtime(time.time())
        st = time.strftime('%Y-%m-%d %H:%M:%S', t)
        self.SetStatusText(st, 1)  # 这里的1代表将时间放入状态栏的第二部分上



class App(wx.App):
    def __init__(self):
    #如果要重写__init__,必须调用wx.App的__init__,否则OnInit方法不会被调用
        wx.App.__init__(self)
    def OnInit(self):
        self.frame=Frame()
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
if __name__=="__main__":
    app = App()
    app.MainLoop()
