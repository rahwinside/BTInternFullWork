import xlrd, sys, xlsxwriter, os
from xlsxwriter.utility import xl_rowcol_to_cell
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *


class Ui_load(object):
    def setupUi(self, load):
        load.setObjectName("load")
        load.resize(645, 583)
        self.gridLayout = QtWidgets.QGridLayout(load)
        self.gridLayout.setObjectName("gridLayout")
        self.continueLabel = QtWidgets.QLabel(load)
        self.continueLabel.setEnabled(True)
        self.continueLabel.setObjectName("continueLabel")
        self.gridLayout.addWidget(self.continueLabel, 6, 1, 1, 1)
        self.browseExcel = QtWidgets.QPushButton(load)
        self.browseExcel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseExcel.setObjectName("browseExcel")
        self.gridLayout.addWidget(self.browseExcel, 0, 2, 1, 1)
        self.excel_file = QtWidgets.QLineEdit(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.excel_file.sizePolicy().hasHeightForWidth())
        self.excel_file.setSizePolicy(sizePolicy)
        self.excel_file.setMinimumSize(QtCore.QSize(400, 0))
        self.excel_file.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.excel_file.setObjectName("excel_file")
        self.gridLayout.addWidget(self.excel_file, 0, 1, 1, 1)
        self.browseTCL = QtWidgets.QPushButton(load)
        self.browseTCL.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseTCL.setObjectName("browseTCL")
        self.gridLayout.addWidget(self.browseTCL, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(load)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pretSPC = QtWidgets.QLineEdit(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pretSPC.sizePolicy().hasHeightForWidth())
        self.pretSPC.setSizePolicy(sizePolicy)
        self.pretSPC.setMinimumSize(QtCore.QSize(400, 0))
        self.pretSPC.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pretSPC.setText("")
        self.pretSPC.setObjectName("pretSPC")
        self.gridLayout.addWidget(self.pretSPC, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 150))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.generate = QtWidgets.QPushButton(load)
        self.generate.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(load)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(load)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.errorLabel = QtWidgets.QLabel(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setMinimumSize(QtCore.QSize(50, 300))
        self.errorLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 9, 0, 1, 3)
        self.tcl_file = QtWidgets.QLineEdit(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tcl_file.sizePolicy().hasHeightForWidth())
        self.tcl_file.setSizePolicy(sizePolicy)
        self.tcl_file.setMinimumSize(QtCore.QSize(400, 0))
        self.tcl_file.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tcl_file.setObjectName("tcl_file")
        self.gridLayout.addWidget(self.tcl_file, 1, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(load)
        self.checkBox.setChecked(False)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 1, 1, 1)
        self.continue_2 = QtWidgets.QPushButton(load)
        self.continue_2.setEnabled(True)
        self.continue_2.setCheckable(False)
        self.continue_2.setObjectName("continue_2")
        self.gridLayout.addWidget(self.continue_2, 7, 1, 1, 1)
        self.resetButton = QtWidgets.QPushButton(load)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 10, 2, 1, 1)

        self.retranslateUi(load)
        QtCore.QMetaObject.connectSlotsByName(load)
        load.setTabOrder(self.excel_file, self.tcl_file)
        load.setTabOrder(self.tcl_file, self.pretSPC)
        load.setTabOrder(self.pretSPC, self.checkBox)
        load.setTabOrder(self.checkBox, self.generate)
        load.setTabOrder(self.generate, self.continue_2)
        load.setTabOrder(self.continue_2, self.resetButton)

    def retranslateUi(self, load):
        _translate = QtCore.QCoreApplication.translate
        load.setWindowTitle(_translate("load", "Loadcase and Loadstep Generator for Hypermesh"))
        self.continueLabel.setText(_translate("load", "<html><head/><body><p align=\"center\">Fill the generated Excel sheet and click &quot;Continue&quot; to generate TCL</p></body></html>"))
        self.browseExcel.setText(_translate("load", "Browse"))
        self.browseTCL.setText(_translate("load", "Browse"))
        self.label_2.setText(_translate("load", "Path to save TCL file:"))
        self.pretSPC.setPlaceholderText(_translate("load", "Empty if no Pretension"))
        self.label_6.setText(_translate("load", "<html><head/><body><p><span style=\" font-weight:600; color:#e70000;\">Check the following in HyperMesh before using this tool:</span></p><p><span style=\" font-weight:600;\">1. All load collectors and load steps don't have spaces in their names (underscores are allowed).</span></p><p><span style=\" font-weight:600;\">2. The name of all SPCs start with &quot;SPC&quot;.</span></p><p><span style=\" font-weight:600;\">3. All cards are deleted.</span></p><p><span style=\" font-weight:600;\">4. The export_entity_data.tcl script is run in HyperMesh.</span></p><p align=\"center\"><span style=\" font-weight:600; font-style:italic; color:#095cc1;\">Error/Activity Log</span></p></body></html>"))
        self.generate.setText(_translate("load", "Generate Excel Workbook"))
        self.label_5.setText(_translate("load", "SPC ID for Pretension:"))
        self.label.setText(_translate("load", "Path to generate Excel file:"))
        self.checkBox.setText(_translate("load", "NLPARM (LGDISP)"))
        self.continue_2.setText(_translate("load", "Continue"))
        self.resetButton.setText(_translate("load", "Reset"))

global_dict = {}
l1 = []
hyper_path = ''
spcList = []
selSPCNoDupl = []
ls_id_list = []
spcAddDict = {}
max_LS = 0
pret_ls_id = 1
ls_list = []
lc_id = []
loadadd_name = []
loadadd_id = []
spcadd_name = []
spcadd_id = []
spcname = []
spcid = []
lc_entity_fin = []
lc_id_fin = []
max_SPC_add_count = 1
nlparm = True
nlparm_id = 10000

class UX(QDialog, Ui_load):
    def __init__(self):
        QDialog.__init__(self)
        Ui_load.__init__(self)
        self.setupUi(self)
        self.reset()
        self.browseExcel.clicked.connect(self.setPathExcel)
        self.browseTCL.clicked.connect(self.setPathTCL)
        self.generate.clicked.connect(self.gen_excel)
        self.continue_2.clicked.connect(self.main)
        self.resetButton.clicked.connect(self.reset)

    def setPathExcel(self):
        excelfname = QFileDialog.getSaveFileName()[0]
        if not excelfname.endswith('.xlsx'):
            excelfname += '.xlsx'
        self.excel_file.setText(excelfname)

    def setPathTCL(self):
        tclfname = QFileDialog.getSaveFileName()[0]
        if not tclfname.endswith('.tcl'):
            tclfname += '.tcl'
        self.tcl_file.setText(tclfname)

    def reset(self):
        self.excel_file.setText('')
        self.tcl_file.setText('')
        self.errorLabel.setText('')
        self.pretSPC.setText('')
        self.continueLabel.hide()
        self.continue_2.hide()

    def gen_excel(self):
        global hyper_path, max_LS, nlparm, nlparm_id, ls_list, pret_ls_id, ls_id_list, lc_id, max_SPC_add_count, loadadd_id, loadadd_name, spcid, spcname, spcadd_id, spcadd_name, lc_entity_fin, lc_id_fin
        nlparm = True
        nlparm_id = 10000
        try:
            try:
                raw_data = open(os.path.expanduser("~").replace(repr('\n').strip("'").strip('n'), "/")+"/Documents/collector.txt", 'r')
            except:
                self.errorLabel.setText(self.errorLabel.text() + 'Error: Run TCL first to export entity information\n')
            try:
                if self.excel_file.text()=='' or self.tcl_file.text()=='':
                    raise Exception
            except:
                self.errorLabel.setText(self.errorLabel.text() + 'Error: Have you entered the correct path?\n')
            wkbook = self.excel_file.text()
            entity_name = raw_data.readline().split()
            entity_id = raw_data.readline().split()
            lc_id = []
            for item in entity_id:
                lc_id.append(item)
            for i in range(len(lc_id)):
                lc_id[i] = int(lc_id[i])
            hyper_path = raw_data.readline().rstrip('\n')
            ls_id_list = raw_data.readline().rstrip('\n').split()

            for i in range(len(ls_id_list)):
                ls_id_list[i] = int(ls_id_list[i])

            if not len(ls_id_list) == 0:
                check = max(ls_id_list)
                if check == '' or check == ' ' or check == 0:
                    check = 0
                max_LS = int(check)
            else:
                max_LS = 0

            ls_list = raw_data.readline().split()
            spcid = raw_data.readline().split()
            for m in range(len(spcid)):
                spcid[m] = int(spcid[m])

            spcname = raw_data.readline().split()

            loadadd_id = raw_data.readline().split()
            for m in range(len(loadadd_id)):
                loadadd_id[m] = int(loadadd_id[m])

            loadadd_name = raw_data.readline().split()

            spcadd_id = raw_data.readline().split()
            for m in range(len(spcadd_id)):
                spcadd_id[m] = int(spcadd_id[m])

            spcadd_name = raw_data.readline().split()

            pret_ls_id = 1
            if 'Pretension' in ls_list:
                pret_ls_id = int(ls_id_list[ls_list.index('Pretension')])

            temp_list = []
            for i in range(0, len(entity_name)):
                temp_list.append((entity_name[i], entity_id[i]))
            if "NLPARM" in entity_name:
                nlparm = False
                x = entity_name.index("NLPARM")
                nlparm_id = int(entity_id[x])
                temp_list.remove(("NLPARM", str(nlparm_id)))
                entity_name.remove("NLPARM")
                entity_id.remove(str(nlparm_id))
            temp_dict = dict(temp_list)

            # marker 1
            max_SPC_add_count = 1
            for item in spcadd_name:
                if item.startswith("SPCADD_"):
                    r = item[7:]
                    if r.isnumeric():
                        if int(r) >= max_SPC_add_count:
                            max_SPC_add_count = int(r) + 1


            wkbk = xlsxwriter.Workbook(wkbook)
            ldcase = wkbk.add_worksheet('CREATE_LOADADD')
            ldstep = wkbk.add_worksheet('CREATE_LOADSTEP')

            cell_format = wkbk.add_format({'bold': True, 'font_color': 'red'})

            i = 0

            lc_entity_fin = []
            lc_id_fin = []
            for i in range(len(entity_name)):
                if entity_name[i] in spcname or entity_name[i] in loadadd_name or entity_name[i] in spcadd_name:
                    continue
                else:
                    lc_entity_fin.append(entity_name[i])
                    lc_id_fin.append(lc_id[i])

            print(lc_entity_fin, lc_id_fin)

            i = 0
            for x in lc_entity_fin:
                if x == "Pretension":
                    continue
                ldcase.write(i + 2, 1, str(x))
                ldcase.write(i + 2, 0, int(lc_id_fin[lc_entity_fin.index(x)]))
                i += 1
            if "Pretension" in entity_name:
                ldcase.write(i + 2, 1, "Pretension")
                ldcase.write(i + 2, 0, int(temp_dict["Pretension"]))

            ldcase.write(1, 0, 'Enter LC names ->', cell_format)
            ldcase.write(0, 2, 'Enter scaling factors for required loads against each load case', cell_format)

            i = 0
            for x in spcname:
                ldstep.write(1, i + 3, str(x))
                ldstep.write(2, i + 3, int(spcid[spcname.index(x)]))
                i += 1
            ldstep.write(2, 0, 'Loadstep name')
            ldstep.write(2, 1, 'Loadstep type')
            ldstep.write(2, 2, 'Pretension')
            merge_format = wkbk.add_format({
                'bold': 1,
                'align': 'center',
                'valign': 'vcenter',
                'fg_color': 'yellow'})
            if not len(spcname) == 1:
                ldstep.merge_range('D1:'+chr(68+len(spcname)-1)+'1', 'SPC', merge_format)
            else:
                ldstep.write(0, 3, 'SPC', merge_format)


            ldstep.data_validation('B3:B1048576', {'validate': 'list',
                                                   'source': ['linear static', 'non-linear quasi-static']})
            ldstep.data_validation('C3:C1048576', {'validate': 'list',
                                                   'source': ['Yes', 'No']})


            for j in range(0, 16370):
                cell = xl_rowcol_to_cell(1, j + 2)
                print(cell)
                ldstep.write(1, j + i + 3,
                             '=IF(CREATE_LOADADD!'+cell+'="","",CREATE_LOADADD!'+cell+')')
            wkbk.close()
            self.continue_2.show()
            self.continueLabel.show()
            self.errorLabel.setText('')
        except Exception as e:
            self.errorLabel.setText(self.errorLabel.text()+'Error: Workbook is possibly open!\nPlease close the workbook and try again!\n')
            print(e)

    def spcAdd(self, wkbook, id):
        global hyper_path, spcList, selSPCNoDupl, spcAddDict, l1, ls_list, ls_id_list, max_SPC_add_count, spcname
        spcList = []
        spcAddDict = []
        selSPCNoDupl = []
        wkbk = xlrd.open_workbook(wkbook)
        sheet = wkbk.sheet_by_index(1)
        nLoadsteps = sheet.nrows

        spcList = []
        for item in spcname:
            spcList.append(item)

        selSPCArray = []

        for i in range(3, nLoadsteps):
            checked = []
            for j in range(3, len(spcList)+3):
                if str(sheet.cell_value(i, j)).split('.')[0] == str(1):
                    checked.append(1)
                else:
                    checked.append(0)
            if checked.count(1)>1:
                selSPCArray.append(checked)

        for x in selSPCArray:
            if x not in selSPCNoDupl:
                selSPCNoDupl.append(x)

        path = self.tcl_file.text()
        new_tcl = open(path, 'a')

        iter = max_SPC_add_count
        spcDictHelper = []
        for item in selSPCNoDupl:
            new_tcl.write('*collectorcreate loadcols "SPCADD_'+str(iter)+'" "" 11\n')
            new_tcl.write('*createmark loadcols 2 "SPCADD_'+str(iter)+'"\n')
            new_tcl.write('*dictionaryload loadcols 2 "'+hyper_path+'/templates/feoutput/optistruct/optistruct" "SPCADD"\n')
            new_tcl.write('*startnotehistorystate {Attached attributes to loadcol "SPCADD_'+str(iter)+'"}\n')
            new_tcl.write('*attributeupdateint loadcols '+str(id)+' 3240 1 2 0 1\n')
            new_tcl.write('*attributeupdateint loadcols '+str(id)+' 3235 1 0 0 '+str(item.count(1))+'\n')
            text = '*createarray '+str(item.count(1))+' '
            for i in range(0, len(spcList)):
                if item[i] == 1:
                    text += str(int(sheet.cell_value(2, i+3))) + ' '
            text += '\n'
            new_tcl.write(text)
            new_tcl.write('*attributeupdateentityidarray loadcols '+str(id)+' 370 1 2 0 loadcols 1 ' + str(item.count(1))+'\n')
            new_tcl.write('*endnotehistorystate {Attached attributes to loadcol "SPCADD_'+str(iter)+'""}\n')
            tupl = (str(item), "SPCADD_" + str(iter))
            spcDictHelper.append(tupl)
            tupl = ("SPCADD_" + str(iter), str(id))
            if (tupl not in l1):
                l1.append(tupl)
            iter += 1
            id += 1


        spcAddDict = dict(spcDictHelper)
        new_tcl.close()
        return id


    def main(self):
        wkbook = self.excel_file.text()
        self.loadcase(wkbook)
        self.loadstep(wkbook)

    def loadcase(self, wkbook):
        global global_dict
        global l1
        global hyper_path
        global nlparm, nlparm_id, lc_id
        global lc_entity_fin, lc_id_fin

        l1 = []

        try:
            loadcasesheet = xlrd.open_workbook(wkbook)
            sheet = loadcasesheet.sheet_by_index(0)
            nlcase = sheet.ncols - 2  # no of load cases

            if (sheet.cell_value(sheet.nrows - 1, 1) == 'Pretension'):
                nlcount = sheet.nrows - 3  # no of load counter
            else:
                nlcount = sheet.nrows - 2  # no of load counter

            path = self.tcl_file.text()
            new_tcl = open(path, 'w')

            LCount = []
            for i in range(2, nlcase + 2):
                x = []
                for j in range(2, nlcount + 2):
                    x.append(sheet.cell_value(j, i))
                LCount.append(x)

            for m in range(len(LCount)):
                for n in range(len(LCount[m])):
                    if LCount[m][n] == '':
                        LCount[m][n] = float(0)

            if (len(LCount) == 0):
                self.errorLabel.setText(self.errorLabel.text() + 'Error: Workbook is possibly empty!\n')
                raise Exception

            # transpose LCount
            tLCount = [[LCount[j][i] for j in range(len(LCount))] for i in range(len(LCount[0]))]
            print(tLCount)
            for q in range(0, len(tLCount)):
                for w in range(0, len(tLCount[q])):
                    if tLCount[q][w] == '':
                        tLCount[q][w] = float(0)
                    print(type(tLCount[q][w]))

            print(tLCount)

            # iter to write lst data to tcl file
            ctr = 0
            for x in tLCount:
                ctr = ctr + 1
                lstdata = str(x)[1:-1]
                new_tcl.write("set lst" + str(ctr) + ' [split "' + lstdata + '" ","]\n')

            # iter to get loadcase names
            lcase_name = []
            for i in range(nlcase):
                lcase_name.append(sheet.cell_value(1, i + 2))

            highestIDVal = max(lc_id)

            # append all collector and IDs
            # marker 2
            for item in lc_entity_fin:
                if ((item, int(lc_id_fin[lc_entity_fin.index(item)])) not in l1):
                    l1.append((item, int(lc_id_fin[lc_entity_fin.index(item)])))

            # iter to write tcl script for each case
            for i in range(0, nlcase):
                new_tcl.write("set name " + lcase_name[i] + "\n")
                new_tcl.write("set j [expr " + str(i + 1) + "+" + str(
                    highestIDVal) + "]\n")  # tcl: j is the ID of the loadcase being created (not nlcount+2)
                l1.append((lcase_name[i], i + highestIDVal + 1))
                k = nlcount - LCount[i].count(0) - LCount[i].count(
                    str(0.0))  # tcl: k is no. of non-zero scaling factors in a loadcase (non-zero cells in a excel row)
                new_tcl.write("set k " + str(k) + "\n")
                new_tcl.write('*startnotehistorystate {Created loadcollector $name}\n')
                new_tcl.write('*collectorcreate loadcols $name "" 11\n')
                new_tcl.write('*createmark loadcols 2 $name\n')
                new_tcl.write(
                    '*dictionaryload loadcols 2 "' + hyper_path + '/templates/feoutput/optistruct/optistruct" "LOADADD"\n')
                new_tcl.write('*startnotehistorystate {Attached attributes to loadcol $name}\n')
                new_tcl.write('*attributeupdateint loadcols $j 3240 1 2 0 1\n')
                new_tcl.write('*attributeupdatedouble loadcols $j 379 1 2 0 1\n')
                new_tcl.write('*attributeupdateint loadcols $j 3236 1 0 0 1\n')
                new_tcl.write('*createdoublearray 1 0\n')
                new_tcl.write('*attributeupdatedoublearray loadcols $j 380 1 2 0 1 1\n')
                new_tcl.write('*createarray 1 0\n')
                new_tcl.write('*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 1\n')
                new_tcl.write('*endnotehistorystate {Attached attributes to loadcol $name}\n')
                new_tcl.write('*startnotehistorystate {Attached attributes to loadcol $name}\n')
                new_tcl.write('*attributeupdateint loadcols $j 3236 1 0 0 $k\n')

                # iter to get all non-zero scaling factor indices
                nonzerolistindices = [x for x in range(len(LCount[i])) if not (LCount[i][x] == 0
                                                                               or str(LCount[i][x]) == '0.0')]
                for x in range(0, len(nonzerolistindices)):
                    nonzerolistindices[x] += 1
                loadNumStr = ""
                for j in range(1, k + 1):
                    new_tcl.write(
                        "set load" + str(j) + " [lindex $lst" + str(nonzerolistindices[j - 1]) + " [expr " + str(
                            i + 1) + "-1]]\n")
                    loadNumStr += "$load" + str(j) + " "

                # iter to form IDList (non-zero ones)
                RefIDList = []
                for t in nonzerolistindices:
                    RefIDList.append(int(sheet.cell_value(t + 1, 0)))

                new_tcl.write('*createdoublearray $k ' + loadNumStr[:-1] + '\n')
                new_tcl.write('*attributeupdatedoublearray loadcols $j 380 1 2 0 1 $k\n')
                new_tcl.write("*createarray $k " + str(RefIDList)[1:-1].replace(",", "") + "\n")
                new_tcl.write('*attributeupdateentityidarray loadcols $j 383 1 2 0 loadcols 1 $k\n')
                new_tcl.write('*endnotehistorystate {Attached attributes to loadcol $name}\n')
                new_tcl.write('*endnotehistorystate {Created loadcollector $name}\n')
                new_tcl.write('#iteration ' + str(i + 1) + ' ends\n')

            new_tcl.close()


            nlparmID = str(int(i) + int(highestIDVal) + 1)

            try:
                id = self.spcAdd(wkbook, int(nlparmID)+1)
            except Exception as e:
                self.errorLabel.setText(self.errorLabel.text()+"Error: Failed to generate SPCADD!\n")
                print(e)

            # NLPARM gen
            if nlparm == True:
                new_tcl = open(path, 'a')
                nlparmID = str(id)
                new_tcl.write('*startnotehistorystate {Created loadcollector "NLPARM"}\n')
                new_tcl.write('*collectorcreate loadcols "NLPARM" "" 11\n')
                new_tcl.write('*createmark loadcols 2 "NLPARM"\n')
                new_tcl.write(
                    '*dictionaryload loadcols 2 "' + hyper_path + '/templates/feoutput/optistruct/optistruct" "NLPARM"\n')
                new_tcl.write('*startnotehistorystate {Attached attributes to loadcol "NLPARM"}\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 3240 1 2 0 1\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 4113 1 0 0 10\n')
                new_tcl.write('*attributeupdatedouble loadcols ' + nlparmID + ' 4232 1 2 0 0\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 4234 1 0 0 6\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 4088 1 0 0 25\n')
                new_tcl.write('*attributeupdatestring loadcols ' + nlparmID + ' 4089 1 0 0 "UPW"\n')
                new_tcl.write('*attributeupdatedouble loadcols ' + nlparmID + ' 4090 1 0 0 0.001\n')
                new_tcl.write('*attributeupdatedouble loadcols ' + nlparmID + ' 4091 1 0 0 0.001\n')
                new_tcl.write('*attributeupdatedouble loadcols ' + nlparmID + ' 4092 1 0 0 1e-007\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 4238 1 0 0 20\n')
                new_tcl.write('*attributeupdatedouble loadcols ' + nlparmID + ' 4240 1 0 0 0.001\n')
                new_tcl.write('*attributeupdatedouble loadcols ' + nlparmID + ' 10201 1 0 0 1\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 10614 1 2 0 1\n')
                new_tcl.write('*endnotehistorystate {Attached attributes to loadcol "NLPARM"}\n')
                new_tcl.write('*startnotehistorystate {Attached attributes to loadcol "NLPARM"}\n')
                new_tcl.write('*attributeupdateint loadcols ' + nlparmID + ' 4113 1 1 0 10\n')
                new_tcl.write('*endnotehistorystate {Attached attributes to loadcol "NLPARM"}\n')
                new_tcl.write('*endnotehistorystate {Created loadcollector "NLPARM"}\n')
                l1.append(('nlparmID', int(nlparmID)))
                new_tcl.close()
            else:
                l1.append(('nlparmID', int(nlparm_id)))

            self.errorLabel.setText("TCL generated for loadcase!\n")
            new_tcl.close()
            global_dict = dict(l1)
            # print(global_dict)

        except Exception as e:
            self.errorLabel.setText("Error generating TCL file! (Unhandled Exception)\n")
            print(e)

    def loadstep(self, wkbook):
        global global_dict, max_LS, ls_list, pret_ls_id, spcname, spcid
        global l1, selSPCNoDupl, spcAddDict, spcList
        errorCount = 0
        lgdisp = int(self.checkBox.checkState())
        try:
            excel_input = xlrd.open_workbook(wkbook)
            loadstep_sheet = excel_input.sheet_by_index(1)
            pretsheet = excel_input.sheet_by_index(0)
            nLoadsteps = loadstep_sheet.nrows - 3
            nls_attributes = 0
            i = 3
            while (i < 16384):
                if not (loadstep_sheet.cell_value(0, i) in [0, '']):
                    nls_attributes += 1
                    i += 1
                else:
                    break

            loadstep_matrix = [[0 if loadstep_sheet.cell_value(i + 3, j + 3) == '' else int(loadstep_sheet.cell_value(i + 3, j + 3)) for j in range(nls_attributes)] for i in
                               range(nLoadsteps)]

            for x in loadstep_matrix:
                if 1 not in x:
                    print('here')
                    self.errorLabel.setText(self.errorLabel.text() + 'Error: No SPC or Load selected in step ' + str(
                        loadstep_matrix.index(x) + 1) + '!\n')
                    errorCount += 1

            pretension = []
            try:
                for i in range(0, nLoadsteps):
                    if (loadstep_sheet.cell_value(i + 3, 2) == 'Yes'):
                        pretension.append(1)
                    elif (loadstep_sheet.cell_value(i + 3, 2) == 'No'):
                        pretension.append(0)
                    else:
                        raise Exception
            except Exception as e:
                self.errorLabel.setText(self.errorLabel.text() + "Invalid Pretension Value!\n")
                print(e)
                errorCount += 1

            tcl_file_name = self.tcl_file.text()
            new_tcl = open(tcl_file_name, 'a')

            print(pretension)
            pretensionEnabled = False
            pret_ID = str(1)
            y = -1
            try:
                if (1 in pretension):
                    pretensionEnabled = True
                    if 'Pretension' in ls_list:
                        pret_ID = str(pret_ls_id)
                        y = 0
                    else:
                        pret_ID = str(max_LS + 1)
                        if(self.pretSPC.text() == ''):
                            raise Exception
                        pretspcid = int(self.pretSPC.text())
                        if (pretsheet.cell_value(pretsheet.nrows - 1, 1) == 'Pretension'):
                            pretloadid = int(pretsheet.cell_value(pretsheet.nrows - 1, 0))
                        else:
                            self.errorLabel.setText(self.errorLabel.text()+"Warning: No Pretension found, will use 0 as Pretension ID.\n")
                            pretloadid = 0
                        new_tcl.write('*startnotehistorystate {LoadSteps Creation}\n')
                        new_tcl.write('*createmark loadcols 1\n')
                        new_tcl.write('*createmark outputblocks 1\n')
                        new_tcl.write('*createmark groups 1\n')
                        new_tcl.write('*loadstepscreate "Pretension" 1\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 4143 1 1 0 1\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 4709 1 1 0 9\n')
                        new_tcl.write('*attributeupdateentity loadsteps '+pret_ID+' 4145 1 1 0 loadcols ' + str(int(pretspcid)) + '\n')
                        if lgdisp == 0:
                            new_tcl.write('*attributeupdateentity loadsteps '+pret_ID+' 4187 1 1 0 loadcols ' + str(global_dict['nlparmID']) + '\n')
                        else:
                            new_tcl.write('*attributeupdateentity loadsteps '+pret_ID+' 9931 1 1 0 loadcols ' + str(global_dict['nlparmID']) + '\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 3800 1 1 0 0\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 707 1 1 0 0\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 2396 1 1 0 0\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 8134 1 1 0 0\n')
                        new_tcl.write('*attributeupdateentity loadsteps '+pret_ID+' 2159 1 1 0 loadcols ' + str(int(pretloadid)) + '\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 2160 1 1 0 0\n')
                        new_tcl.write('*attributeupdateint loadsteps '+pret_ID+' 10212 1 1 0 0\n')
                        new_tcl.write('*endnotehistorystate {LoadSteps Creation}\n')
                        new_tcl.write('#Pretension Created!\n')
            except:
                self.errorLabel.setText(self.errorLabel.text() + 'Error: SPC ID for Pretension is not defined!\n')
                errorCount += 1

            # store SPC name and ID to dict
            SPC_count = 0
            for item in spcname:
                SPC_count += 1
                l1.append((item, str(int(spcid[spcname.index(item)]))))
            global_dict = dict(l1)
            print(global_dict)

            # set nlCase
            nLCase = nls_attributes - SPC_count

            for i in range(0, len(loadstep_matrix)):
                if (pretensionEnabled):
                    id = str(i + 2 + max_LS)
                    if y == 0:
                        id = str(i + 1 + max_LS)
                else:
                    id = str(i + 1 + max_LS)
                new_tcl.write('*startnotehistorystate {LoadSteps Creation}\n')

                if (loadstep_matrix[i].count(1) == 2):
                    line = '*createmark loadcols 1 "' + str(
                        loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)) + '" "'
                    line += str(loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) - loadstep_matrix[i][::-1].index(
                        1) - 1 + 3)) + '"' + '\n'
                elif loadstep_matrix[i].count(1) == 1:
                    line = '*createmark loadcols 1 "' + str(
                        loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)) + '"' + '\n'
                else:
                    line = ''
                    pass

                new_tcl.write(line)
                new_tcl.write('*createmark outputblocks 1\n')
                new_tcl.write('*createmark groups 1\n')
                new_tcl.write('*loadstepscreate "' + str(loadstep_sheet.cell_value(i + 3, 0)) + '" 1' + '\n')

                # check for linear static
                if (loadstep_sheet.cell_value(i + 3, 1) == 'linear static'):
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 4143 1 1 0 1' + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 4709 1 1 0 1' + '\n')

                    # run if only SPC or Load available
                    if (loadstep_matrix[i].count(1) == 1):
                        # run if only Load is available
                        if not (str(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)) in spcname):
                            # line = '*attributeupdateentity loadsteps ' + id + ' 4147 1 1 0 loadcols ' + str(
                            #     global_dict[loadstep_sheet.cell_value(0, loadstep_matrix[i].index(1) + 4)]) + '\n'
                            # new_tcl.write(line)
                            self.errorLabel.setText(
                                self.errorLabel.text() + 'Error: Only Load is selected in step ' + str(i + 1) + '!\nPlease select atleast one SPC\n')
                            errorCount += 1
                        # run if only SPC is available
                        else:
                            line = '*attributeupdateentity loadsteps ' + id + ' 4145 1 1 0 loadcols ' + str(
                                global_dict[loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)]) + '\n'
                            new_tcl.write(line)
                            self.errorLabel.setText(
                                self.errorLabel.text() + 'Warning: Only SPC is selected! in step ' + str(i + 1) + '\n')


                    # run if SPC&Load is available
                    elif (loadstep_matrix[i].count(1) > 1):
                        try:
                            spcArray = loadstep_matrix[i][0:len(spcList)]
                            for z in range(0, len(spcArray)):
                                if spcArray[z] == '':
                                    spcArray[z] = 0

                            loadArray = loadstep_matrix[i][len(spcList):]
                            print(spcList)
                            print(loadstep_matrix[i])
                            print(spcArray, loadArray)
                            print(spcAddDict)

                            if(loadArray.count(1)>1):
                                self.errorLabel.setText(
                                    self.errorLabel.text() + 'Error: More than one load selected in step ' + str(
                                        i + 1)+'\n')
                                raise Exception

                            if(spcArray.count(1) == 0):
                                self.errorLabel.setText(
                                    self.errorLabel.text() + 'Error: No SPC selected in step ' + str(
                                        i + 1)+'\n')
                                raise Exception


                            if(spcArray.count(1)>1):
                                self.errorLabel.setText(
                                    self.errorLabel.text() + 'Warning: More than one SPC selected in step ' + str(
                                        i + 1)+'\n')
                                print(spcAddDict[str(spcArray)])
                                line = '*attributeupdateentity loadsteps ' + id + ' 4145 1 1 0 loadcols ' + str(
                                    global_dict[spcAddDict[str(spcArray)]]) + '\n'
                                new_tcl.write(line)
                                line = '*attributeupdateentity loadsteps ' + id + ' 4147 1 1 0 loadcols ' + str(
                                    global_dict[loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) -
                                                                          loadstep_matrix[i][::-1].index(
                                                                              1) - 1 + 3)]) + '\n'
                                new_tcl.write(line)

                            if spcArray.count(1) == 1:
                                line = '*attributeupdateentity loadsteps ' + id + ' 4145 1 1 0 loadcols ' + str(
                                    global_dict[loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)]) + '\n'
                                new_tcl.write(line)
                                print(loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) -
                                                                          loadstep_matrix[i][::-1].index(
                                                                              1) - 1 + 3))
                                line = '*attributeupdateentity loadsteps ' + id + ' 4147 1 1 0 loadcols ' + str(
                                    global_dict[loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) -
                                                                          loadstep_matrix[i][::-1].index(
                                                                              1) - 1 + 3)]) + '\n'
                                new_tcl.write(line)

                        except Exception as e:
                            self.errorLabel.setText(
                                self.errorLabel.text() + "Error in Excel sheet, check whether SPC and Loadcases\nare selected properly for step " + str(
                                    i + 2) + "! \nFailed to generate TCL for Loadstep!\n")
                            # os.system("pause")
                            errorCount += 1
                            continue

                    # check pretension==yes
                    if (pretension[i] == 0):
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 3800 1 1 0 1' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 707 1 1 0 1' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2396 1 1 0 1' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 8134 1 1 0 1' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2160 1 1 0 1' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 10212 1 1 0 1' + '\n')
                    else:
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 3800 1 1 0 0' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 707 1 1 0 0' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2396 1 1 0 0' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 8134 1 1 0 0' + '\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2160 1 1 0 0' + '\n')
                        new_tcl.write('*createarray 1 ' + pret_ID + '\n')
                        new_tcl.write('*attributeupdateentityidarray loadsteps ' + id + ' 2161 1 1 0 loadsteps 1 1\n')
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 10212 1 1 0 0\n')

                # non-linear quasi-static
                elif (loadstep_sheet.cell_value(i + 3, 1) == 'non-linear quasi-static'):
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 4143 1 1 0 1' + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 4709 1 1 0 9' + '\n')

                    # run if only SPC or Load available
                    if (loadstep_matrix[i].count(1) == 1):
                        # run if only load is available
                        if not (str(loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)) in spcname):
                            # line = '*attributeupdateentity loadsteps ' + id + ' 4147 1 1 0 loadcols ' + str(
                            #     global_dict[loadstep_sheet.cell_value(0, loadstep_matrix[i].index(1) + 4)]) + '\n'
                            # new_tcl.write(line)
                            self.errorLabel.setText(
                                self.errorLabel.text() + 'Error: Only Load is selected in step ' + str(i + 1) + '1\nPlease select atleast one SPC.\n')
                            errorCount += 1
                        # run if only SPC is available
                        else:
                            line = '*attributeupdateentity loadsteps ' + id + ' 4145 1 1 0 loadcols ' + str(
                                global_dict[loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)]) + '\n'
                            new_tcl.write(line)
                            self.errorLabel.setText(
                                self.errorLabel.text() + 'Warning: Only SPC is selected! in step ' + str(i + 1) + '\n')

                    if (loadstep_matrix[i].count(1) == 0):
                        errorCount += 1
                        continue

                    elif (loadstep_matrix[i].count(1) > 1):
                        try:
                            spcArray = loadstep_matrix[i][0:len(spcList)]
                            for z in range(0, len(spcArray)):
                                if spcArray[z] == '':
                                    spcArray[z] = 0
                            loadArray = loadstep_matrix[i][len(spcList):]

                            if (loadArray.count(1) > 1):
                                self.errorLabel.setText(
                                    self.errorLabel.text() + 'Error: More than one load selected in step ' + str(
                                        i + 1)+'\n')
                                raise Exception

                            if (spcArray.count(1) == 0):
                                self.errorLabel.setText(
                                    self.errorLabel.text() + 'Error: No SPC selected in step ' + str(
                                        i + 1)+'\n')
                                raise Exception

                            if (spcArray.count(1) > 1):
                                self.errorLabel.setText(
                                    self.errorLabel.text() + 'Warning: More than one SPC selected in step ' + str(
                                        i + 1)+'\n')

                                line = '*attributeupdateentity loadsteps ' + id + ' 4145 1 1 0 loadcols ' + str(
                                    global_dict[spcAddDict[str(spcArray)]]) + '\n'
                                new_tcl.write(line)
                                line = '*attributeupdateentity loadsteps ' + id + ' 4147 1 1 0 loadcols ' + str(
                                    global_dict[loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) -
                                                                          loadstep_matrix[i][::-1].index(
                                                                              1) - 1 + 3)]) + '\n'
                                new_tcl.write(line)

                            if spcArray.count(1) == 1:
                                line = '*attributeupdateentity loadsteps ' + id + ' 4145 1 1 0 loadcols ' + str(
                                    global_dict[
                                        loadstep_sheet.cell_value(1, loadstep_matrix[i].index(1) + 3)]) + '\n'
                                new_tcl.write(line)
                                line = '*attributeupdateentity loadsteps ' + id + ' 4147 1 1 0 loadcols ' + str(
                                    global_dict[loadstep_sheet.cell_value(1, len(loadstep_matrix[i]) -
                                                                          loadstep_matrix[i][::-1].index(
                                                                              1) - 1 + 3)]) + '\n'
                                new_tcl.write(line)
                        except Exception as e:
                            self.errorLabel.setText(
                                self.errorLabel.text() + "Error in Excel sheet, check whether SPC and Loadcases\nare selected properly for step " + str(
                                    i + 2) + "!\nFailed to generate TCL for Loadstep!\n")
                            # os.system("pause")
                            errorCount += 1
                            continue
                    elif (loadstep_matrix[i].count(1) > 2):
                        self.errorLabel.setText(
                            self.errorLabel.text() + "Error: Load+SPC count is more than 2 in step " + id + "!\nPlease select only one load and one SPC\n")
                        continue
                    if lgdisp == 0:
                        new_tcl.write('*attributeupdateentity loadsteps ' + id + ' 4187 1 1 0 loadcols ' + str(
                            global_dict['nlparmID']) + '\n')
                    else:
                        new_tcl.write('*attributeupdateentity loadsteps ' + id + ' 9931 1 1 0 loadcols ' + str(
                            global_dict['nlparmID']) + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 3800 1 1 0 0' + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 707 1 1 0 0' + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2396 1 1 0 0' + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 8134 1 1 0 0' + '\n')
                    if (pretension[i] == 1):
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2160 1 1 0 1' + '\n')
                        new_tcl.write('*createarray 1 ' + pret_ID + '\n')
                        new_tcl.write(
                            '*attributeupdateentityidarray loadsteps ' + id + ' 2161 1 1 0 loadsteps loadsteps 1 1\n')
                    elif pretension[i] == 0:
                        new_tcl.write('*attributeupdateint loadsteps ' + id + ' 2160 1 1 0 0' + '\n')
                    new_tcl.write('*attributeupdateint loadsteps ' + id + ' 10212 1 1 0 0' + '\n')

                else:
                    self.errorLabel.setText(self.errorLabel.text() + "Check Loadstep Type!")
                new_tcl.write('*endnotehistorystate {LoadSteps Creation}\n')
                new_tcl.write("#end of iter " + str(i + 1) + '\n')
            if (errorCount == 0):
                # cards
                new_tcl.write('*startnotehistorystate {Modified control card}\n')
                new_tcl.write('*cardcreate "GLOBAL_OUTPUT_REQUEST"\n')
                new_tcl.write('*startnotehistorystate {Attached attributes to card}\n')
                new_tcl.write('*attributeupdateint cards 1 3321 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9630 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9307 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9317 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9327 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3880 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 4119 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 4114 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7121 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 2938 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 10688 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 523 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 2385 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 4052 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3712 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 3885 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 274 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3057 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7113 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 8500 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 2419 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 9709 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3809 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7125 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 4877 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9337 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9347 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9357 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3325 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7093 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3333 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 2423 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 4047 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 9275 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 5463 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 8949 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 10440 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7329 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7333 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 2427 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 8153 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 8150 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 8144 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3642 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 2431 1 2 0 1\n')
                new_tcl.write('*attributeupdateint cards 1 7337 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 7117 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3891 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 3329 1 2 0 0\n')
                new_tcl.write('*attributeupdateint cards 1 1902 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3881 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3882 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3883 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 1901 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "SORT1"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4871 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "H3D"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4315 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4008 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4876 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2174 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2287 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2175 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9621 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 10026 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 10027 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2939 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 1906 1 0 0 2\n')
                new_tcl.write('*createstringarray 2 "        " "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2177 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "OPTI"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4316 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3336 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 10996 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2176 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2290 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 8137 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "ALL" "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3713 1 2 0 1 2\n')
                new_tcl.write('*attributeupdateint cards 1 1910 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4318 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4867 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2292 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2420 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 1916 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4321 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3318 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2424 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 8950 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 8951 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "YES"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 8952 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 1921 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9609 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4323 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3342 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3343 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2294 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2428 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 1922 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "SORT1"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4872 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "H3D"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4324 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3338 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3339 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "CORNER"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9603 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 696 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9606 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9997 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9933 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3643 1 2 0 1 1\n')
                new_tcl.write('*attributeupdateint cards 1 1923 1 0 0 1\n')
                new_tcl.write('*createstringarray 1 "SORT1"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4873 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "H3D"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4325 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3386 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 3387 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "CORNER"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 4839 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 1221 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2295 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 8136 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 8430 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 9932 1 2 0 1 1\n')
                new_tcl.write('*createstringarray 1 "        "\n')
                new_tcl.write('*attributeupdatestringarray cards 1 8429 1 2 0 1 1\n')
                new_tcl.write('*createdoublearray 1 0\n')
                new_tcl.write('*attributeupdatedoublearray cards 1 9254 1 0 0 1 1\n')
                new_tcl.write('*createdoublearray 1 0\n')
                new_tcl.write('*attributeupdatedoublearray cards 1 9255 1 0 0 1 1\n')
                new_tcl.write('*createarray 1 0\n')
                new_tcl.write('*attributeupdateintarray cards 1 9280 1 0 0 1 1\n')
                new_tcl.write('*createdoublearray 1 0\n')
                new_tcl.write('*attributeupdatedoublearray cards 1 9281 1 0 0 1 1\n')
                new_tcl.write('*createstringarray 1 "YES"\n')
                new_tcl.write('*attributeupdatestringarray cards 1 2432 1 2 0 1 1\n')
                new_tcl.write('*endnotehistorystate {Attached attributes to card}\n')
                new_tcl.write('*endnotehistorystate {Modified control card}\n')
                new_tcl.write('*startnotehistorystate {Modified control card}\n')
                new_tcl.write('*cardcreate "OUTPUT"\n')
                new_tcl.write('*startnotehistorystate {Attached attributes to card}\n')
                new_tcl.write('*attributeupdateint cards 2 3850 1 0 0 2\n')
                new_tcl.write('*attributeupdatestring cards 2 130 1 0 0 "0"\n')
                new_tcl.write('*createstringarray 2 "H3D" "OP2"\n')
                new_tcl.write('*attributeupdatestringarray cards 2 3851 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "        " "MODEL"\n')
                new_tcl.write('*attributeupdatestringarray cards 2 3854 1 2 0 1 2\n')
                new_tcl.write('*createstringarray 2 "ALL" "ALL"\n')
                new_tcl.write('*attributeupdatestringarray cards 2 3852 1 2 0 1 2\n')
                new_tcl.write('*endnotehistorystate {Attached attributes to card}\n')
                new_tcl.write('*endnotehistorystate {Modified control card}\n')
                new_tcl.write('*startnotehistorystate {Modified control card}\n')
                new_tcl.write('*endnotehistorystate {Modified control card}\n')

            else:
                self.errorLabel.setText(self.errorLabel.text() +
                                        'Error: TCL file is not generated! Please check the excel file!\n')
            new_tcl.close()

            if errorCount == 0:
                self.errorLabel.setText(self.errorLabel.text() + 'TCL generated for loadstep!\n')
                self.errorLabel.setText(self.errorLabel.text() + 'All OK!\n')
        except Exception as e:
            self.errorLabel.setText(
                self.errorLabel.text() + 'Error: TCL generation failed for loadstep! (Unhandled Exception)\n' + "\n")
            print(e)
        errorCount = 0


app = QApplication(sys.argv)
ux = UX()
ux.show()
app.exec_()
