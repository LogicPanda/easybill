import os
import datetime
import easygui as eg
import os.path as op

weekdays = ["Sun", "Mon","Tue","Wed","Thu","Fri","Sat"]
def getdatetime(): # get datetime
    today = datetime.datetime.today()
    year, month, day = today.year, today.month, today.day
    hour, minute, second = today.hour, today.minute, today.second
    weekday = weekdays[today.weekday()]
    return str(year)+"/"+str(month)+"/"+str(day)+' '+weekday+' '+str(hour)+":"+str(minute)

# main class
class Bill():

    def __init__(self) :
        self.affairs = '待办事件'
        self.records = '完成记录'
        self.bil = '清单'
        self.rec = '记录单'
        self.item = '事件'
        self.recd = '记录'
        self.title = 'EasyBill'

    def gettime(self):
        t = datetime.datetime.today()
        return t.year, t.month, t.day, t.hour, t.minute, t.second

    def cd(self, dst = None):
        if dst == self.bil :
            os.chdir(self.affairs)
        if dst == self.rec :
            os.chdir(self.records)

    def exist(self):
        if not op.exists(self.affairs) or op.isdir(self.affairs) :
            try:
                os.mkdir(self.affairs)
            except:
                pass
        else:
            pass
        if not op.exists(self.records) or op.isdir(self.records):
            try:
                os.mkdir(self.records)
            except:
                pass
        else:
            pass
        
    # 创建新清单和创建新记录
    def makebill(self, kind = None):
        
        self.cd(kind)
        
        newbill = eg.enterbox('给新'+ kind + '取个名字吧^_^ ',self.title)
        if not op.exists(newbill):
            f = open(newbill, 'w')
            f.close()
            if op.exists(newbill):
                eg.msgbox('成功新'+ kind + "\"" + newbill+ "\""+'!',"EasyBill")
        else:
            eg.msgbox(kind + "\"" + newbill + "\""+'已存在!',"EasyBill")

        os.chdir('..')
            
    # 修改清单内容或修改记录内容
    def modifybill(self, kind = None):
        self.cd(kind)
        typefile = eg.choicebox('选择要添加内容的'+ kind,'EasyBill', os.listdir('.'))
        newitem = eg.enterbox('请输入新内容：','EasyBill')
        f = open(typefile, 'a')
        newtime = getdatetime()
        f.write(newtime + ' | ' + newitem+'\n')
        f.close()
        eg.msgbox('新内容\"'+newitem+'\"已添加到'+typefile ,"EasyBill")
        os.chdir('..') 
        

    # 显示清单内容或显示记录内容
    def disbill(self, kind = None):

        self.cd(kind)
        
        typefile = eg.choicebox('选择要显示的'+ kind,'EasyBill', os.listdir('.'))
        f = open(typefile, 'r')
        eg.textbox(typefile, 'EasyBill', f)
        f.close
        os.chdir('..')


    # 删除清单内容或删除记录内容
    def rmitem(self, kind):

        self.cd(kind)
        typefile = eg.choicebox('选择要删除内容的'+ kind,'EasyBill', os.listdir('.'))
        f = open(typefile, 'r')
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        affair = eg.choicebox('请选择要删除的内容', 'EasyBill', lines)
        lines.remove(affair)
        f = open(typefile, 'w')
        for each in lines:
            f.write(each)
        f.close
        os.chdir('..')

    
    # 删除现存清单或删除现存记录
    def rmbill(self, kind = None):
        
        self.cd(kind)

        rmbn = eg.choicebox('选择要删除的'+ kind,'EasyBill', os.listdir('.'))
        os.remove(rmbn)
        eg.msgbox(kind + '\"'+rmbn+ '\"' + '已删除')
        os.chdir('..')

    # 完成事件，即，将待办事件中的内容搬运到完成记录中
    def finishitem(self):
        self.cd(self.bil)
        typefile = eg.choicebox('选择要完成事件的'+ self.bil,'EasyBill', os.listdir('.'))
        f = open(typefile, 'r')
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        affair = eg.choicebox('请选择要完成的事件', 'EasyBill', lines)
        newitem = affair.split('|')
        lines.remove(affair)
        f = open(typefile, 'w')
        for each in lines:
            f.write(each)
        f.close()
        os.chdir('..')
        self.cd(self.rec)
        typefile = eg.choicebox('选择要记录内容的'+ self.rec,'EasyBill', os.listdir('.'))
        f = open(typefile, 'a')
        newtime = getdatetime()
        f.write(newtime + ' | ' + newitem[1].strip() +'\n')
        f.close()
        eg.msgbox('新内容\"'+newitem[1].strip()+'\"已添加到'+typefile ,"EasyBill")
        os.chdir('..')

    # 最初，功能选择
    def choosefuncs(self):
        allfuncs = ('创建清单','添加事件','显示事件','完成事件','删除事件','删除清单','创建记录单','添加记录','显示记录','删除记录','删除记录单','退出')
        while True:
            getfunc = eg.choicebox('要做什么呢？','EasyBill', allfuncs)
            if getfunc == '创建清单':
                self.makebill(kind = self.bil)
            elif getfunc == '添加事件':
                self.modifybill(kind = self.bil)
            elif getfunc == '显示事件':
                self.disbill(kind = self.bil)
            elif getfunc == '完成事件':
                self.finishitem()
            elif getfunc == '删除事件':
                self.rmitem(kind = self.bil)
            elif getfunc == '删除清单':
                self.rmbill(kind = self.bil)
            elif getfunc == '创建记录单':
                self.makebill(kind = self.rec)
            elif getfunc == '添加记录':
                self.modifybill(kind = self.rec)
            elif getfunc == '显示记录':
                self.disbill(kind = self.rec)
            elif getfunc == '删除记录':
                self.rmitem(kind = self.rec)
            elif getfunc == '删除记录单':
                self.rmbill(kind = self.rec)
            else:
                eg.msgbox('感谢使用EasyBillv1.1 <^_^>',"EasyBill")
                exit()
    

if __name__ == "__main__":
    eg.msgbox('欢迎使用EasyBillv1.1',"EasyBill")
    t = Bill()
    t.exist()
    t.choosefuncs()
