# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:48:39 2017

@author: ssurabhi
"""

#import wx
#
#app = wx.App()
#
#frame = wx.Frame(None, -1, "sample.py")
#frame.Show()
#
#app.MainLoop()
import wx

class Example(wx.Frame):

    def __init__(self, parent, title):    
        super(Example, self).__init__(parent, title=title, 
            size=(450, 350))

        self.InitUI()
        self.Centre()
        self.Show()     

    def InitUI(self):
      
        panel = wx.Panel(self)
        
        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Load Combs Generator")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, 
            border=15)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), 
            flag=wx.EXPAND|wx.BOTTOM, border=10)


        text2 = wx.StaticText(panel, label="Load Combs csv file name")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)
        
        self.tc1 = wx.TextCtrl(panel)
        sizer.Add(self.tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)
        self.Bind(wx.EVT_TEXT, self.inputs, self.tc1)

        text3 = wx.StaticText(panel, label="TCL file name")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        self.tc2 = wx.TextCtrl(panel)
        sizer.Add(self.tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
        self.Bind(wx.EVT_TEXT, self.inputs, self.tc2)

#        button1 = wx.Button(panel, label="Browse...")
#        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)

        text4 = wx.StaticText(panel, label="Number of Loads")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        self.tc3 = wx.TextCtrl(panel)
        sizer.Add(self.tc3, pos=(4, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
        self.Bind(wx.EVT_TEXT, self.inputs, self.tc3)

#        button2 = wx.Button(panel, label="Browse...")
#        sizer.Add(button2, pos=(4, 4), flag=wx.TOP|wx.RIGHT, border=5)

        text5 = wx.StaticText(panel, label="Number of Loadcases")
        sizer.Add(text5, pos=(5, 0), flag=wx.TOP|wx.LEFT, border=10)

        self.tc4 = wx.TextCtrl(panel)
        sizer.Add(self.tc4, pos=(5, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
        self.Bind(wx.EVT_TEXT, self.inputs, self.tc4)
#        sb = wx.StaticBox(panel, label="Optional Attributes")
#
#        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
#        boxsizer.Add(wx.CheckBox(panel, label="Public"), 
#            flag=wx.LEFT|wx.TOP, border=5)
#        boxsizer.Add(wx.CheckBox(panel, label="Generate Default Constructor"),
#            flag=wx.LEFT, border=5)
#        boxsizer.Add(wx.CheckBox(panel, label="Generate Main Method"), 
#            flag=wx.LEFT|wx.BOTTOM, border=5)
#        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5), 
#            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

#        button3 = wx.Button(panel, label='Help')
#        sizer.Add(button3, pos=(7, 2), flag=wx.LEFT, border=10)

        button1 = wx.Button(panel, label="Generate")
        sizer.Add(button1, pos=(7, 3))
        button1.Bind(wx.EVT_BUTTON, self.generate_file)

#        button5 = wx.Button(panel, label="Cancel")
#        sizer.Add(button5, pos=(7, 4), span=(1, 1),  
#            flag=wx.BOTTOM|wx.RIGHT, border=5)

        sizer.AddGrowableCol(2)
        
        panel.SetSizer(sizer)

    def inputs(self, e):
        self.load_combs_file = self.tc1.GetValue()
        self.tcl_file = self.tc2.GetValue()
        self.number_of_loadcases = self.tc3.GetValue()
        self.number_of_loads = self.tc4.GetValue()

    def generate_file(self, e):
        try:
            load_combs_file_name = self.load_combs_file + '.csv'
            f = open(load_combs_file_name, 'r')
            file_table = []
            for I in f:
                file_table.append(I.split())
            f.close()

            N = int(self.number_of_loads)
            O = int(self.number_of_loadcases)
            # S = 2 #first load ID number

            all_combs = []
            for A in range(5, N + 6):
                all_combs.append(file_table[A][0].split(","))
            for B in range(1, N + 1):
                del all_combs[B][1]

            load_IDs = file_table[5][2].split(',')
            load_IDs.remove('IDs')

            loadcombs = []
            for X in range(1, O + 1):
                lcombs = all_combs[1][X]
                for J in range(2, N + 1):
                    lcombs += "," + all_combs[J][X]
                loadcombs.append(lcombs)

            tcl_file_name = self.tcl_file + '.tcl'
            h = open(tcl_file_name, 'w')
            for j in range(O):
                line = 'set lst' + str(j + 1) + ' [split "' + loadcombs[j] + '" ","]\n'
                h.write(line)

            names = []
            for n in range(N + 1):
                names.append(all_combs[n][0])

            for i in range(1, N + 1):
                load_places = []
                for lp in range(1, O + 1):
                    if all_combs[i][lp] != '0':
                        load_places.append(lp)
                M = len(load_places)
                line = 'set name ' + names[i] + '\n'
                h.write(line)
                line = 'set j [expr ' + str(i) + '+' + str(O) + ']\n'
                h.write(line)
                line = 'set k ' + str(M) + '\n'
                h.write(line)
                h.write('*startnotehistorystate {Created loadcollector $name}\n')
                h.write('*collectorcreate loadcols $name "" 11\n')
                h.write('*createmark loadcols 2 $name\n')
                h.write(
                    '*dictionaryload loadcols 2 "C:/Program Files/Altair/2017/templates/feoutput/optistruct/optistruct" "LOADADD"\n')
                h.write('*startnotehistorystate {Attached attributes to loadcol $name}\n')
                h.write('*attributeupdateint loadcols $j 3240 1 2 0 1\n')
                h.write('*attributeupdatedouble loadcols $j 379 1 2 0 1\n')
                h.write('*attributeupdateint loadcols $j 3236 1 0 0 1\n')
                h.write('*createdoublearray 1 0\n')
                h.write('*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1\n')
                h.write('*createarray 1 0\n')
                h.write('*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1\n')
                h.write('*endnotehistorystate {Attached attributes to loadcol $name}\n')
                h.write('*startnotehistorystate {Attached attributes to loadcol $name}\n')
                h.write('*attributeupdateint loadcols $j 3236 1 0 0 $k\n')
                line = 'set load1 [lindex $lst' + str(load_places[0]) + ' [expr ' + str(i) + '-1]]\n'
                h.write(line)
                loads = "$load1"
                for K in range(2, M + 1):
                    line = 'set load' + str(K) + ' [lindex $lst' + str(load_places[K - 1]) + ' [expr ' + str(
                        i) + '-1]]\n'
                    h.write(line)
                    loads += ' $load' + str(K)
                line = '*createdoublearray $k ' + loads + '\n'
                h.write(line)
                h.write('*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k\n')
                load_p = str(load_IDs[load_places[0] - 1])
                for P in range(1, M):
                    load_p += ' ' + str(load_IDs[load_places[P] - 1])
                line = '*createarray $k ' + load_p + '\n'
                h.write(line)
                h.write('*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k\n')
                h.write('*endnotehistorystate {Attached attributes to loadcol $name}\n')
                h.write('*endnotehistorystate {Created loadcollector $name}\n')
                line = '#iteration ' + str(i) + ' ends\n'
                h.write(line)
            h.close()
            print('LOADCOMBS TCL FILE IS GENERATED')
        except:
            print("LOADCOMBS TCL FILE IS NOT GENERATED")



if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title="Load Combs TCL file Generator")
    app.MainLoop()