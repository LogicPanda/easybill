import easygui as w

# w.egdemo() # view the all function of easygui
w.msgbox('欢迎使用easybill')
class Bill:
    '''
    A easy bill built in easygui
    You can use this script：
    addaffair
    displayaffairs
    removeaffair
    finishaffair
'''
    def __init__(self):
        self.schedule_file = '待办事件'
        self.achieve_file = '完成记录'

    def getAll(self, file):
        f = open(file)
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        return lines
            
    def appendaffair(self):
        """添加待办事件"""
        f = open(self.schedule_file , 'a')
        f.write(w.enterbox())
        f.write('\n')
        f.close()

    def displaySchedule(self):
        """Display the Schedule！"""
        f = open('待办事件', 'r')
        w.textbox('待办事件', 'Display', f)
        f.close()

    def removeAffair(self, file, affair):
        f = open(file, 'r')
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        if affair in lines:
            lines.remove(affair)
            f = open(file, 'w')
            for each in lines:
                f.write(each)
            f.close
        else:
            pass

    def delSchedule(self):
        f = open('待办事件', 'r')
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        if len(lines) > 0:
            getDelSchedule = w.choicebox('选择要删除的事件','', lines)
            lines.remove(getDelSchedule)
            f = open('待办事件', 'w')
            for each in lines:
                f.write(each)
            f.close()
            w.msgbox("已经成功删除了 %s " % getDelSchedule)
        else:
            w.msgbox("没有待办事件！")

    

    def finishSchedule(self):
        """Move the affair to the Record"""
        f = open('待办事件')
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        getRecord = w.choicebox('选择已完成的事件','', lines)
        self.removeAffair('待办事件',getRecord)
        f = open('完成记录', 'a')
        f.write(getRecord)
        f.write('\n')
        f.close()

    def displayRecord(self):
        '''Display the Record of the having finished'''
        f = open('完成记录', 'r')
        w.textbox('完成记录', 'Display', f)
        f.close()

    def delRecord(self):
        f = open('完成记录')
        lines = []
        for each_line in f:
            lines.append(each_line)
        f.close()
        if len(lines) > 0:
            getRecord = w.choicebox('请选择要删除的记录\n删除之后会显示所有记录\n','删除记录', lines)
            self.removeAffair('完成记录', getRecord)
            self.displayRecord()
        else:
            w.msgbox("还没有记录，赶紧去完成事件吧。")
        pass

    def choiceFunction(self):
        while True:
            getfun = w.choicebox('要做什么呢？', '', ('添加事件', '查看事件', '删除事件',
                                   '完成事件', '查看记录','删除记录', '退出'))
            if   getfun == '添加事件':
                self.appendaffair()
            elif getfun == '查看事件':
                self.displaySchedule()
            elif getfun == '完成事件':
                self.finishSchedule()
            elif getfun == '删除事件':
                self.delSchedule()
            elif getfun == '查看记录':
                self.displayRecord()
            elif getfun == '删除记录':
                self.delRecord()
            else:
                exit(1)


start = Bill()
start.choiceFunction()
