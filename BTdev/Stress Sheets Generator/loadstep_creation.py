import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(450, 200))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)
        text1 = wx.StaticText(panel, label="Load Step Generator")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
          border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
          flag=wx.EXPAND | wx.BOTTOM, border=10)
        text2 = wx.StaticText(panel, label="Load Step xlsx file name")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)
        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)
        self.Bind(wx.EVT_TEXT, self.inputs, self.tc1)
        text3 = wx.StaticText(panel, label="TCL file name")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)
        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND, border=5)
        self.Bind(wx.EVT_TEXT, self.inputs, self.tc2)
        button1 = wx.Button(panel, label="Generate")
        sizer.Add(button1, pos=(4, 3))
        button1.Bind(wx.EVT_BUTTON, self.generate_file)
        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)

    def inputs(self, e):
        self.load_step_file = self.tc1.GetValue()
        self.tcl_file = self.tc2.GetValue()

    def generate_file(self, e):
        try:
            import openpyxl

            excel_input = openpyxl.load_workbook(self.load_step_file + '.xlsx')
            loadstep_sheet = excel_input.active
            loadstep_matrix = [[str(i.value) for i in j] for j in loadstep_sheet]
            no_of_loadsteps = len(loadstep_matrix) - 4
            no_of_loadcombs = len(loadstep_matrix[4]) - 2
            loadsteps_IDs = []

            for j1 in range(9, len(loadstep_matrix)):
                for j2 in range(2, len(loadstep_matrix[4])):
                    if loadstep_matrix[j1][j2] == "1":
                        loadsteps_IDs.append(loadstep_matrix[7][j2])
                        loadsteps_IDs.append(loadstep_matrix[8][j2])

            no = []
            g = 0
            for l in range(1, no_of_loadsteps + 1):
                g += 1
                no.append(g)

            #print(loadsteps_IDs)

            k = 0
            u = 0
            tcl_file_name = self.tcl_file + '.tcl'
            h = open(tcl_file_name, 'w')
            for i in range(9, len(loadstep_matrix)):
                h.write('*startnotehistorystate {LoadSteps Creation}\n')
                line = '*createmark loadcols 1"' + loadsteps_IDs[k] + '" "' + loadsteps_IDs[k + 2] + '"' + '\n'
                h.write(line)
                h.write('*createmark outputblocks 1\n')
                h.write('*createmark groups 1\n')
                line = '*loadstepscreate "' + loadstep_matrix[i][0] + '" 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 4143 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 4709 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateentity loadsteps ' + str(no[u]) + ' 4145 1 1 0 loadcols ' + loadsteps_IDs[
                    k + 3] + '\n'
                h.write(line)
                line = '*attributeupdateentity loadsteps ' + str(no[u]) + ' 4147 1 1 0 loadcols ' + loadsteps_IDs[
                    k + 1] + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 3800 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 707 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 2396 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 8134 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 2160 1 1 0 1' + '\n'
                h.write(line)
                line = '*attributeupdateint loadsteps ' + str(no[u]) + ' 10212 1 1 0 1' + '\n'
                h.write(line)
                h.write('*endnotehistorystate {LoadSteps Creation}\n')
                k += 4
                u += 1
            h.close()
            print('LOADSTEP TCL FILE IS GENERATED')

        except:
            print('LOADSTEP TCL FILE IS NOT GENERATED')


if __name__ == '__main__':
    app = wx.App()
    Example(None, title="Load Step TCL file Generator")
    app.MainLoop()























