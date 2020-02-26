import sys, xlwt, xlrd, openpyxl
from xlutils import copy
from PyQt5.QtWidgets import *
from tinydb import TinyDB
import finui

bolt_size = 1.6  # diameter of bolt

# global content collectors
bolt_data = {}
clamped_data = []
threaded_data = {}
extLoad_data = {}


class UX(QDialog, finui.Ui_bolt_ui):
    def __init__(self):
        QDialog.__init__(self)
        finui.Ui_bolt_ui.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.db = TinyDB('boltdata.json')
        self.old_clamp_count = 0

        self.nutCombo.hide()
        self.gradeNutCombo.hide()
        self.renutlineEdit.hide()
        self.rmnutlineEdit.hide()
        self.recnutlineEdit.hide()

        self.populateTypeList()
        self.populateGradeList()
        self.populatePartList()
        self.getMaterialData()
        self.getNutMaterialData()

        self.nClampedPartsText.editingFinished.connect(self.populateClampTab)
        self.typeCombo.currentTextChanged.connect(self.populateSizeList)
        self.sizeCombo.currentTextChanged.connect(self.setBoltSize)
        self.gradeCombo.currentTextChanged.connect(self.getMaterialData)
        self.gradeNutCombo.currentTextChanged.connect(self.getNutMaterialData)
        self.partCombo.currentTextChanged.connect(self.populatePartComponentList)
        self.saveInput.clicked.connect(self.saveInputData)
        self.resetInput.clicked.connect(self.resetInputData)
        self.saveClamp.clicked.connect(self.saveClampData)
        self.resetClamp.clicked.connect(self.resetClampData)
        self.calculateEL.clicked.connect(self.saveExtData)
        self.resetEL.clicked.connect(self.resetExtData)
        self.renutlineEdit.editingFinished.connect(self.setREC)
        self.rmnutlineEdit.editingFinished.connect(self.setREC)

    def saveInputData(self):
        try:
            global bolt_data, threaded_data, bolt_size
            data = []
            data2 = []
            type = self.typeCombo.currentText().split()[0]
            size = self.sizeCombo.currentText()
            material = self.gradeCombo.currentText().split()[0]
            if material == 'Stainless':
                e = 191000
            else:
                e = 210000
            re = self.relineedit.text()
            rm = self.rmlineedit.text()
            length = self.lengthText.text()
            bolttab = self.db.table(type)

            for item in bolttab:
                if str(item['size']) == str(size):
                    data.append(('height', item['k']))
                    data.append(('dw', item['dw']))
                    data.append(('pitch', item['pitch']))
                    data.append(('re', float(re)))
                    data.append(('rm', float(rm)))
                    data.append(('length', float(length)))
                    data.append(('e', e))
                    break
            print(data)
            bolt_data = dict(data)

            thread_type = self.partCombo.currentText()
            if(thread_type == 'Nut'):
                nutStd = self.nutCombo.currentText().split()[0]
                nuttab = self.db.table(nutStd)
                for item in nuttab:
                    if float(item['size']) == float(bolt_size):
                        dia = float(item['dw'])
                        h = float(item['m'])
                        data2.append(('dia',dia))
                        data2.append(('height', h))
                        break
            else:
                r = float(self.rBlock.text())
                s = float(self.sBlock.text())
                t = float(self.tBlock.text())
                u = float(self.uBlock.text())
                dia = abs(r-t) if (abs(r-t)<abs(s-u)) else abs(s-u)
                data2.append(('dia', dia))
                h = float(self.nutHeight.text())
                data2.append(('height', h))
            re = self.renutlineEdit.text()
            rm = self.rmnutlineEdit.text()
            data2.append(('re', float(re)))
            data2.append(('rm', float(rm)))

            print(data2)
            threaded_data = dict(data2)
        except:
            print('Missing data!')

    def resetInputData(self):
        pass

    def saveClampData(self):
        global clamped_data
        clamped_data.clear()
        try:
            for i in range(self.scrollLayout.count()):
                l = []
                x: Generator = self.scrollLayout.itemAt(i).widget()
                l.append(('re', float(x.yieldWasher.text())))
                l.append(('rm', float(x.ultiWasher.text())))
                l.append(('e', float(x.eModulus.text())))
                l.append(('material', x.materialWasher.text()))
                l.append(('thick', float(x.thicklineEdit.text())))
                if x.partComboBox.currentText() == 'Rectangular':
                    dimen = [float(x.rEdit.text()),
                             float(x.sEdit.text()),
                             float(x.tEdit.text()),
                             float(x.uEdit.text())]
                    l.append(('insdia', float(x.holeDia.text())))
                    outdia = min(dimen)
                    l.append(('outdia', outdia))

                    if x.typeComboBox.currentText() == 'Oblong hole':
                        l.append(('r', dimen[0]))
                        l.append(('s', dimen[1]))
                        l.append(('t', dimen[2]))
                        l.append(('u', dimen[3]))
                        l.append(('d', float(x.holeDia.text())))
                        l.append(('l', float(x.holeLength.text())))
                else:
                    l.append(('insdia', float(x.insdialineEdit.text())))
                    l.append(('outdia', float(x.outdialineEdit.text())))
                clamped_data.append(dict(l))
            print(clamped_data)
        except:
            print('Enter all data!')

    def resetClampData(self):
        pass

    def saveExtData(self):
        try:
            global extLoad_data
            fa = float(self.axialForcelineEdit.text())
            ft = float(self.shearForcelineEdit.text())
            beta = float(self.betalineEdit.text())
            umin = float(self.uminlineEdit.text())
            torque = float(self.torquelineEdit.text())
            ttAcc = float(self.tightAccuracylineEdit.text())
            ut = float(self.utlineEdit.text())
            delut = float(self.delutlineEdit.text())
            ub = float(self.ublineEdit.text())
            delub = float(self.delublineEdit.text())
            ye = float(self.yelineEdit.text())

            data = [
                ('axialForce', fa),
                ('shearForce', ft),
                ('beta', beta),
                ('fricCoeff', umin),
                ('torque', torque),
                ('tightTorqAcc', ttAcc),
                ('ut', ut),
                ('delut', delut),
                ('ub', ub),
                ('delub', delub),
                ('eqStressTightRatio', ye)
            ]

            extLoad_data = dict(data)
            print(extLoad_data)

            self.fillSpreadsheet()
        except:
            print('Empty or invalid fields!')

    def resetExtData(self):
        pass

    def populateTypeList(self):
        l = []
        nametable = self.db.table('boltnames')
        for item in nametable:
            item = str(item['name']+' '+item['type'])
            l.append(str(item))
        self.typeCombo.clear()
        self.typeCombo.addItems(l)
        self.populateSizeList()

    def populateSizeList(self):
        type = self.typeCombo.currentText().split()[0]
        sizetab = self.db.table(type)
        l = []
        for item in sizetab:
            l.append(str(item['size']))
        self.sizeCombo.clear()
        self.sizeCombo.addItems(l)
        self.setBoltSize()

    def setBoltSize(self):
        global bolt_size
        if not (self.sizeCombo.currentText() == ''):
            bolt_size = float(self.sizeCombo.currentText().lstrip('M'))
        self.populatePartComponentList()
        # self.populateClampTab()

    def populateGradeList(self):
        gradetab = self.db.table('boltnutmaterial')
        l = []
        for item in gradetab:
            l.append(str(item['material']+" "+str(item['size'])))
        self.gradeCombo.clear()
        self.gradeCombo.addItems(l)
        self.gradeNutCombo.clear()
        self.gradeNutCombo.addItems(l)

    def getMaterialData(self):
        size = self.gradeCombo.currentText().split()[-1]
        gradetab = self.db.table('boltnutmaterial')
        for item in gradetab:
            if(str(item['size'])==size):
                re = item['Re']
                rm = item['Rm']
                rec = (item['Re']+item['Rm'])/2
                self.relineedit.setText(str(re))
                self.rmlineedit.setText(str(rm))
                self.reclineedit.setText(str(rec))

    def getNutMaterialData(self):
        size = self.gradeNutCombo.currentText().split()[-1]
        gradetab = self.db.table('boltnutmaterial')
        for item in gradetab:
            if(str(item['size'])==size):
                re = item['Re']
                rm = item['Rm']
                rec = (item['Re']+item['Rm'])/2
                self.renutlineEdit.setText(str(re))
                self.rmnutlineEdit.setText(str(rm))
                self.recnutlineEdit.setText(str(rec))

    def populatePartList(self):
        self.partCombo.clear()
        self.partCombo.addItems(['Nut', 'Block'])
        self.populatePartComponentList()

    def populatePartComponentList(self):
        global bolt_size
        if self.partCombo.currentText() == 'Nut':
            self.label_32.hide()
            self.label_33.hide()
            self.label_34.hide()
            self.label_35.hide()
            self.label_36.hide()
            self.label_37.hide()
            self.rBlock.hide()
            self.sBlock.hide()
            self.tBlock.hide()
            self.uBlock.hide()
            self.matBlock.hide()
            self.nutHeight.hide()
            self.recnutlineEdit.setReadOnly(True)
            self.renutlineEdit.setReadOnly(True)
            self.rmnutlineEdit.setReadOnly(True)
            self.label_9.show()
            self.label_10.show()
            self.nutCombo.show()
            self.gradeNutCombo.show()
            self.renutlineEdit.show()
            self.rmnutlineEdit.show()
            self.recnutlineEdit.show()

            nuttab = self.db.table('nutnames')
            l = []
            for item in nuttab:
                stdtab = self.db.table(str(item['std']))
                for x in stdtab:
                    if str(x['size']).lstrip('M').split('x')[0] == str(bolt_size):
                        l.append(str(item['std']) + ' ' + item['type'])
                        break

            self.nutCombo.clear()
            self.nutCombo.addItems(l)
            self.getNutMaterialData()
        else:
            self.nutCombo.hide()
            self.gradeNutCombo.hide()
            self.label_9.hide()
            self.label_10.hide()
            self.label_32.show()
            self.label_33.show()
            self.label_34.show()
            self.label_35.show()
            self.label_36.show()
            self.label_37.show()
            self.rBlock.show()
            self.sBlock.show()
            self.tBlock.show()
            self.uBlock.show()
            self.matBlock.show()
            self.nutHeight.show()
            self.renutlineEdit.setReadOnly(False)
            self.rmnutlineEdit.setReadOnly(False)
            self.recnutlineEdit.clear()
            self.renutlineEdit.clear()
            self.rmnutlineEdit.clear()

    def setREC(self):
        re = self.renutlineEdit.text()
        rm = self.rmnutlineEdit.text()
        try:
            if(re == '' or rm == ''):
                pass
            else:
                rec = (float(re) + float(rm)) / 2
                self.recnutlineEdit.setText(str(rec))
        except:
            print('Enter numerical values only!')

    def populateClampTab(self):
        x = self.nClampedPartsText.text()
        if(x == '' or x.isalpha()):
            self.scrollLayout.addRow(QLabel('Enter valid number of clamps.'))
            return
        count = int(x)
        if not(self.old_clamp_count == count):
            for i in range(self.scrollLayout.count()):
                self.scrollLayout.itemAt(i).widget().close()
            try:
                if count in range(2, 11):
                    for i in range(0, count):
                        self.scrollLayout.addRow(Generator(i))
                else:
                    self.scrollLayout.addRow(QLabel('Number of clamps should be between 2 and 10.'))
                self.old_clamp_count = count
            except Exception:
                self.scrollLayout.addRow(QLabel('Unhandled Exception.'))

    def fillSpreadsheet(self):
        try:
            global bolt_data, bolt_size, threaded_data, extLoad_data, clamped_data

            wb = openpyxl.load_workbook('calcbook.xlsx')
            ws = wb['calculation']

            # write bolt data to sheet
            ws['L2'] = bolt_data['height']
            ws['L3'] = bolt_data['e']
            ws['L4'] = bolt_data['dw']
            ws['L5'] = bolt_size
            ws['L6'] = bolt_data['pitch']
            ws['L7'] = bolt_data['re']
            ws['L8'] = bolt_data['rm']
            ws['L9'] = bolt_data['length']

            # write thread data to sheet
            ws['L32'] = threaded_data['height']
            ws['L33'] = threaded_data['dia']
            ws['L35'] = threaded_data['re']
            ws['L36'] = threaded_data['rm']

            # write ext data to sheet
            ws['L40'] = extLoad_data['axialForce']
            ws['L41'] = extLoad_data['shearForce']
            ws['L42'] = extLoad_data['beta']
            ws['L43'] = extLoad_data['fricCoeff']
            ws['L44'] = extLoad_data['torque']
            ws['L45'] = extLoad_data['tightTorqAcc']
            ws['L47'] = extLoad_data['ut']
            ws['M47'] = extLoad_data['delut']
            ws['L48'] = extLoad_data['ub']
            ws['M48'] = extLoad_data['delub']
            ws['L49'] = extLoad_data['eqStressTightRatio']

            # write clamp data to sheet
            i = 16
            for item in clamped_data:
                ws['K'+str(i)] = item['thick']
                ws['L'+str(i)] = item['insdia']
                ws['M'+str(i)] = item['outdia']
                ws['N'+str(i)] = item['material']
                ws['O'+str(i)] = item['re']
                ws['P'+str(i)] = item['rm']
                ws['R'+str(i)] = item['e']
                i += 1
            while i < 26:
                ws['K'+str(i)] = 0
                ws['L' + str(i)] = 0
                ws['M' + str(i)] = 0
                ws['N' + str(i)] = 0
                ws['O' + str(i)] = 0
                ws['P' + str(i)] = 0
                ws['R' + str(i)] = 1
                i += 1

            wb.save('calcbook.xlsx')

        except Exception as e:
            print('Error in spreadblock!')
            print(e)


class Generator(QWidget):
    def __init__(self, i, parent=None):
        super(Generator, self).__init__(parent)
        self.db = TinyDB('boltdata.json')
        self.formLayout = QFormLayout()
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel('<b>Part '+str(i+1)+"</b>")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)
        self.label_2 = QLabel('Type of part:')
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)
        self.partComboBox = QComboBox()
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.partComboBox)
        self.label_3 = QLabel('Type of washer:')
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)
        self.washerComboBox = QComboBox()
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.washerComboBox)
        self.label_4 = QLabel('Standard:')
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)
        self.standardComboBox = QComboBox()
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.standardComboBox)

        self.label_5 = QLabel('Type:')
        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)
        self.typeComboBox = QComboBox()
        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.typeComboBox)

        self.label_6 = QLabel('Inside Diameter:')
        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)
        self.insdialineEdit = QLineEdit()
        self.insdialineEdit.setReadOnly(True)
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.insdialineEdit)
        self.label_7 = QLabel('Outside Diameter:')
        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)
        self.outdialineEdit = QLineEdit()
        self.outdialineEdit.setReadOnly(True)
        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.outdialineEdit)
        self.label_8 = QLabel('Thickness:')
        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_8)
        self.thicklineEdit = QLineEdit()
        self.thicklineEdit.setReadOnly(True)
        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.thicklineEdit)

        self.label_9 = QLabel('u:')
        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_9)
        self.uEdit = QLineEdit()
        self.uEdit.setReadOnly(False)
        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.uEdit)

        self.label_15 = QLabel('Hole length (L):')
        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_15)
        self.holeLength = QLineEdit()
        self.holeLength.setReadOnly(False)
        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.holeLength)

        self.label_16 = QLabel('Hole height (d):')
        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_16)
        self.holeDia = QLineEdit()
        self.holeDia.setReadOnly(False)
        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.holeDia)

        self.label_10 = QLabel('Thickness:')
        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_10)
        self.rectThickness = QLineEdit()
        self.rectThickness.setReadOnly(False)
        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.rectThickness)

        self.label_14 = QLabel('Material:')
        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_14)
        self.materialWasher = QLineEdit()
        self.materialWasher.setReadOnly(False)
        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.materialWasher)

        self.label_11 = QLabel('Yield (Re):')
        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_11)
        self.yieldWasher = QLineEdit()
        self.yieldWasher.setReadOnly(False)
        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.yieldWasher)

        self.label_12 = QLabel('Ultimate (Rm):')
        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_12)
        self.ultiWasher = QLineEdit()
        self.ultiWasher.setReadOnly(False)
        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.ultiWasher)

        self.label_13 = QLabel("Young's modulus (E):")
        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_13)
        self.eModulus = QLineEdit()
        self.eModulus.setReadOnly(False)
        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.eModulus)

        self.label_9.hide()
        self.uEdit.hide()
        self.label_10.hide()
        self.rectThickness.hide()
        self.label_15.hide()
        self.label_16.hide()
        self.holeLength.hide()
        self.holeDia.hide()

        self.formLayout.setWidget(16, QFormLayout.FieldRole, QLabel("  "))
        self.setLayout(self.formLayout)

        self.populatePartCombo()
        self.populateWasher()
        self.partComboBox.currentTextChanged.connect(self.populateWasher)
        self.washerComboBox.currentTextChanged.connect(self.populateWashStd)
        self.typeComboBox.currentTextChanged.connect(self.fetchWasherInfo)

    def populatePartCombo(self):
        self.partComboBox.clear()
        self.partComboBox.addItems(['Washer', 'Non-Standard Part'])

    def populateWasher(self):
        self.washerComboBox.clear()
        if(self.partComboBox.currentText()=='Washer'):
            self.label_15.hide()
            self.label_16.hide()
            self.holeLength.hide()
            self.holeDia.hide()
            self.uEdit.hide()
            self.label_9.hide()
            self.label_4.show()
            self.label_5.show()
            self.standardComboBox.show()
            self.typeComboBox.show()
            self.label_6.setText('Inside Diameter:')
            self.label_7.setText('Outside Diameter:')
            self.label_8.setText('Thickness:')
            self.insdialineEdit.setReadOnly(True)
            self.outdialineEdit.setReadOnly(True)
            self.thicklineEdit.setReadOnly(True)
            washertable = self.db.table('washernames')
            l = []
            for i in washertable:
                type = str(i['type'])
                if not(type in l):
                    l.append(type)
            self.washerComboBox.addItems(l)
            self.populateWashStd()

        else:
            self.label_3.setText('Part type:')
            self.washerComboBox.addItems(['Circular', 'Rectangular'])
            self.label_4.hide()
            self.label_5.hide()
            self.standardComboBox.hide()
            self.typeComboBox.hide()
            self.label_6.setText('Inside Diameter:')
            self.label_7.setText('Outside Diameter:')
            self.label_8.setText('Thickness:')
            self.populateWashStd()

    def populateWashStd(self):
        global bolt_size
        self.standardComboBox.clear()
        if self.partComboBox.currentText() == 'Washer':
            self.label_15.hide()
            self.label_16.hide()
            self.holeLength.hide()
            self.holeDia.hide()
            self.label_9.hide()
            self.label_10.hide()
            self.uEdit.hide()
            self.rectThickness.hide()
            type = self.washerComboBox.currentText()
            l = []
            y = []
            washertable = self.db.table('washernames')

            for i in washertable:
                if(str(i['type']) == type):
                    l.append(str(i['std']))

            for item in l:
                x = self.db.table(str(item))
                sizeList = []
                for size in x:
                    sizeList.append(size['size'])
                if float(bolt_size) in sizeList:
                    y.append(item)
            self.standardComboBox.addItems(y)
            self.populateWasherTypes()
        else:
            self.typeComboBox.hide()
            self.label_5.hide()
            self.label_9.hide()
            self.uEdit.hide()
            self.rectThickness.hide()
            self.label_10.hide()
            self.insdialineEdit.setReadOnly(False)
            self.outdialineEdit.setReadOnly(False)
            self.thicklineEdit.setReadOnly(False)
            if self.washerComboBox.currentText() == 'Circular':
                self.label_15.hide()
                self.label_16.hide()
                self.holeLength.hide()
                self.holeDia.hide()
                self.label_6.setText('Inside Diameter:')
                self.label_7.setText('Outside Diameter:')
                self.label_8.setText('Thickness:')
            else:
                self.label_15.hide()
                self.label_16.hide()
                self.holeLength.hide()
                self.holeDia.hide()
                self.typeComboBox.show()
                self.populateWasherTypes()
                self.label_5.show()
                self.uEdit.show()
                self.uEdit.setText('')
                self.label_9.show()
                self.label_10.show()
                self.rectThickness.show()
                self.rectThickness.clear()
                self.label_6.setText('r:')
                self.label_7.setText('s:')
                self.label_8.setText('t:')
                self.label_9.setText('u:')
                self.thicklineEdit.setText('')
                self.insdialineEdit.setText('')
                self.outdialineEdit.setText('')

    def populateWasherTypes(self):
        self.typeComboBox.clear()
        l = []
        if(self.partComboBox.currentText() == 'Washer'):
            global bolt_size
            std = self.standardComboBox.currentText()
            washertab = self.db.table(std)
            for item in washertab:
                if(item['type'] not in l and item['size'] == float(bolt_size)):
                    l.append(item['type'])
            self.typeComboBox.addItems(l)
            self.fetchWasherInfo()

        else:
            l = ['Circular hole', 'Oblong hole']
            self.typeComboBox.addItems(l)

    def fetchWasherInfo(self):
        global bolt_size
        if self.typeComboBox.currentText() == 'Oblong hole':
            self.label_15.show()
            self.label_16.show()
            self.label_16.setText('Hole height (d):')
            self.holeLength.show()
            self.holeDia.show()
        elif self.typeComboBox.currentText()=='Circular hole':
            self.label_15.hide()
            self.label_16.show()
            self.holeLength.hide()
            self.holeDia.show()
            self.label_16.setText('Hole Diameter (d):')
        else:
            self.label_15.hide()
            self.label_16.hide()
            self.holeLength.hide()
            self.holeDia.hide()
            std = self.standardComboBox.currentText()
            type = self.typeComboBox.currentText()
            washertab = self.db.table(std)
            for item in washertab:
                print(item)
                if(item['type'] == type and item['size'] == float(bolt_size)):
                    self.insdialineEdit.setText(str(item['dimin']))
                    self.outdialineEdit.setText(str(item['domin']))
                    self.thicklineEdit.setText(str(item['thnom']))


app = QApplication(sys.argv)
dial = UX()
dial.show()
app.exec_()
