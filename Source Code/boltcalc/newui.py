# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rapon\PycharmProjects\boltcalc\production_ui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bolt_ui(object):
    def setupUi(self, bolt_ui):
        bolt_ui.setObjectName("bolt_ui")
        bolt_ui.resize(714, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bolt_ui.sizePolicy().hasHeightForWidth())
        bolt_ui.setSizePolicy(sizePolicy)
        bolt_ui.setSizeGripEnabled(True)
        bolt_ui.setModal(False)
        self.gridLayout_4 = QtWidgets.QGridLayout(bolt_ui)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(bolt_ui)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.pitchlabel = QtWidgets.QLabel(self.tab)
        self.pitchlabel.setObjectName("pitchlabel")
        self.gridLayout.addWidget(self.pitchlabel, 5, 1, 1, 1)
        self.thicklineEdit = QtWidgets.QLineEdit(self.tab)
        self.thicklineEdit.setObjectName("thicklineEdit")
        self.gridLayout.addWidget(self.thicklineEdit, 6, 2, 1, 7)
        self.nutCombo = QtWidgets.QComboBox(self.tab)
        self.nutCombo.setObjectName("nutCombo")
        self.gridLayout.addWidget(self.nutCombo, 20, 2, 1, 7)
        self.renutlineEdit = QtWidgets.QLineEdit(self.tab)
        self.renutlineEdit.setObjectName("renutlineEdit")
        self.gridLayout.addWidget(self.renutlineEdit, 25, 2, 1, 7)
        self.rmnutlineEdit = QtWidgets.QLineEdit(self.tab)
        self.rmnutlineEdit.setObjectName("rmnutlineEdit")
        self.gridLayout.addWidget(self.rmnutlineEdit, 26, 2, 1, 7)
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 20, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 23, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 25, 1, 1, 1)
        self.gradeNutCombo = QtWidgets.QComboBox(self.tab)
        self.gradeNutCombo.setObjectName("gradeNutCombo")
        self.gridLayout.addWidget(self.gradeNutCombo, 23, 2, 1, 7)
        self.tBlock = QtWidgets.QLineEdit(self.tab)
        self.tBlock.setObjectName("tBlock")
        self.gridLayout.addWidget(self.tBlock, 21, 6, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 26, 1, 1, 1)
        self.resetInput = QtWidgets.QPushButton(self.tab)
        self.resetInput.setMinimumSize(QtCore.QSize(0, 40))
        self.resetInput.setObjectName("resetInput")
        self.gridLayout.addWidget(self.resetInput, 28, 6, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.tab)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 24, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 27, 1, 1, 1)
        self.uBlock = QtWidgets.QLineEdit(self.tab)
        self.uBlock.setObjectName("uBlock")
        self.gridLayout.addWidget(self.uBlock, 21, 8, 1, 1)
        self.recnutlineEdit = QtWidgets.QLineEdit(self.tab)
        self.recnutlineEdit.setObjectName("recnutlineEdit")
        self.gridLayout.addWidget(self.recnutlineEdit, 27, 2, 1, 7)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 15, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 13, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 21, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.tab)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 22, 1, 1, 1)
        self.nutHeight = QtWidgets.QLineEdit(self.tab)
        self.nutHeight.setObjectName("nutHeight")
        self.gridLayout.addWidget(self.nutHeight, 22, 2, 1, 7)
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 14, 1, 1, 1)
        self.relineedit = QtWidgets.QLineEdit(self.tab)
        self.relineedit.setEnabled(True)
        self.relineedit.setReadOnly(True)
        self.relineedit.setObjectName("relineedit")
        self.gridLayout.addWidget(self.relineedit, 13, 2, 1, 7)
        self.lengthText = QtWidgets.QLineEdit(self.tab)
        self.lengthText.setObjectName("lengthText")
        self.gridLayout.addWidget(self.lengthText, 8, 2, 1, 7)
        self.nClampedPartsText = QtWidgets.QLineEdit(self.tab)
        self.nClampedPartsText.setObjectName("nClampedPartsText")
        self.gridLayout.addWidget(self.nClampedPartsText, 0, 2, 1, 7)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.gradeCombo = QtWidgets.QComboBox(self.tab)
        self.gradeCombo.setObjectName("gradeCombo")
        self.gridLayout.addWidget(self.gradeCombo, 11, 2, 1, 7)
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 21, 3, 1, 1)
        self.saveInput = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveInput.sizePolicy().hasHeightForWidth())
        self.saveInput.setSizePolicy(sizePolicy)
        self.saveInput.setMinimumSize(QtCore.QSize(0, 40))
        self.saveInput.setObjectName("saveInput")
        self.gridLayout.addWidget(self.saveInput, 28, 8, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.tab)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 21, 5, 1, 1)
        self.rBlock = QtWidgets.QLineEdit(self.tab)
        self.rBlock.setObjectName("rBlock")
        self.gridLayout.addWidget(self.rBlock, 21, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.tab)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 21, 7, 1, 1)
        self.sBlock = QtWidgets.QLineEdit(self.tab)
        self.sBlock.setObjectName("sBlock")
        self.gridLayout.addWidget(self.sBlock, 21, 4, 1, 1)
        self.sizeCombo = QtWidgets.QComboBox(self.tab)
        self.sizeCombo.setObjectName("sizeCombo")
        self.gridLayout.addWidget(self.sizeCombo, 3, 2, 1, 7)
        self.rmlineedit = QtWidgets.QLineEdit(self.tab)
        self.rmlineedit.setEnabled(True)
        self.rmlineedit.setReadOnly(True)
        self.rmlineedit.setObjectName("rmlineedit")
        self.gridLayout.addWidget(self.rmlineedit, 14, 2, 1, 7)
        self.reclineedit = QtWidgets.QLineEdit(self.tab)
        self.reclineedit.setEnabled(True)
        self.reclineedit.setReadOnly(True)
        self.reclineedit.setObjectName("reclineedit")
        self.gridLayout.addWidget(self.reclineedit, 15, 2, 1, 7)
        self.partCombo = QtWidgets.QComboBox(self.tab)
        self.partCombo.setObjectName("partCombo")
        self.gridLayout.addWidget(self.partCombo, 19, 2, 1, 7)
        self.matBlock = QtWidgets.QLineEdit(self.tab)
        self.matBlock.setObjectName("matBlock")
        self.gridLayout.addWidget(self.matBlock, 24, 2, 1, 7)
        self.typeCombo = QtWidgets.QComboBox(self.tab)
        self.typeCombo.setObjectName("typeCombo")
        self.gridLayout.addWidget(self.typeCombo, 2, 2, 1, 7)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 19, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 18, 0, 1, 2)
        self.pitchlineEdit = QtWidgets.QLineEdit(self.tab)
        self.pitchlineEdit.setObjectName("pitchlineEdit")
        self.gridLayout.addWidget(self.pitchlineEdit, 5, 2, 1, 7)
        self.thicklabel = QtWidgets.QLabel(self.tab)
        self.thicklabel.setObjectName("thicklabel")
        self.gridLayout.addWidget(self.thicklabel, 6, 1, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(self.tab)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 4, 1, 1, 1)
        self.sizelineEdit = QtWidgets.QLineEdit(self.tab)
        self.sizelineEdit.setObjectName("sizelineEdit")
        self.gridLayout.addWidget(self.sizelineEdit, 4, 2, 1, 7)
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setObjectName("label_42")
        self.gridLayout.addWidget(self.label_42, 7, 3, 1, 1)
        self.sBlock_2 = QtWidgets.QLineEdit(self.tab)
        self.sBlock_2.setObjectName("sBlock_2")
        self.gridLayout.addWidget(self.sBlock_2, 7, 4, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.tab)
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 7, 1, 1, 1)
        self.rBlock_2 = QtWidgets.QLineEdit(self.tab)
        self.rBlock_2.setObjectName("rBlock_2")
        self.gridLayout.addWidget(self.rBlock_2, 7, 2, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setObjectName("label_43")
        self.gridLayout.addWidget(self.label_43, 7, 5, 1, 1)
        self.tBlock_2 = QtWidgets.QLineEdit(self.tab)
        self.tBlock_2.setObjectName("tBlock_2")
        self.gridLayout.addWidget(self.tBlock_2, 7, 6, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setObjectName("label_44")
        self.gridLayout.addWidget(self.label_44, 7, 7, 1, 1)
        self.uBlock_2 = QtWidgets.QLineEdit(self.tab)
        self.uBlock_2.setObjectName("uBlock_2")
        self.gridLayout.addWidget(self.uBlock_2, 7, 8, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 500, 158, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.resetClamp = QtWidgets.QPushButton(self.layoutWidget)
        self.resetClamp.setObjectName("resetClamp")
        self.horizontalLayout.addWidget(self.resetClamp)
        self.saveClamp = QtWidgets.QPushButton(self.layoutWidget)
        self.saveClamp.setObjectName("saveClamp")
        self.horizontalLayout.addWidget(self.saveClamp)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ublineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.ublineEdit.setObjectName("ublineEdit")
        self.gridLayout_3.addWidget(self.ublineEdit, 7, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.tab_3)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 7, 2, 1, 1)
        self.delublineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.delublineEdit.setObjectName("delublineEdit")
        self.gridLayout_3.addWidget(self.delublineEdit, 7, 3, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.tab_3)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 8, 0, 1, 1)
        self.yelineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.yelineEdit.setObjectName("yelineEdit")
        self.gridLayout_3.addWidget(self.yelineEdit, 8, 1, 1, 2)
        self.calculateEL = QtWidgets.QPushButton(self.tab_3)
        self.calculateEL.setObjectName("calculateEL")
        self.gridLayout_3.addWidget(self.calculateEL, 11, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 0, 0, 1, 1)
        self.axialForcelineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.axialForcelineEdit.setObjectName("axialForcelineEdit")
        self.gridLayout_3.addWidget(self.axialForcelineEdit, 0, 1, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 1, 0, 1, 1)
        self.shearForcelineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.shearForcelineEdit.setObjectName("shearForcelineEdit")
        self.gridLayout_3.addWidget(self.shearForcelineEdit, 1, 1, 1, 2)
        self.label_19 = QtWidgets.QLabel(self.tab_3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 2, 0, 1, 1)
        self.betalineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.betalineEdit.setObjectName("betalineEdit")
        self.gridLayout_3.addWidget(self.betalineEdit, 2, 1, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 3, 0, 1, 1)
        self.uminlineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.uminlineEdit.setObjectName("uminlineEdit")
        self.gridLayout_3.addWidget(self.uminlineEdit, 3, 1, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 0, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.tab_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 1, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 4, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_3)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 8, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 4, 0, 1, 1)
        self.torquelineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.torquelineEdit.setObjectName("torquelineEdit")
        self.gridLayout_3.addWidget(self.torquelineEdit, 4, 1, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 5, 0, 1, 1)
        self.tightAccuracylineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.tightAccuracylineEdit.setObjectName("tightAccuracylineEdit")
        self.gridLayout_3.addWidget(self.tightAccuracylineEdit, 5, 1, 1, 2)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 6, 0, 1, 1)
        self.utlineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.utlineEdit.setObjectName("utlineEdit")
        self.gridLayout_3.addWidget(self.utlineEdit, 6, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 6, 2, 1, 1)
        self.resetEL = QtWidgets.QPushButton(self.tab_3)
        self.resetEL.setObjectName("resetEL")
        self.gridLayout_3.addWidget(self.resetEL, 11, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.tab_3)
        self.label_38.setObjectName("label_38")
        self.gridLayout_3.addWidget(self.label_38, 5, 3, 1, 1)
        self.delutlineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.delutlineEdit.setObjectName("delutlineEdit")
        self.gridLayout_3.addWidget(self.delutlineEdit, 6, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 7, 0, 1, 1)
        self.thetalineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.thetalineEdit.setObjectName("thetalineEdit")
        self.gridLayout_3.addWidget(self.thetalineEdit, 9, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.tab_3)
        self.label_39.setObjectName("label_39")
        self.gridLayout_3.addWidget(self.label_39, 9, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab_3)
        self.label_40.setObjectName("label_40")
        self.gridLayout_3.addWidget(self.label_40, 9, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.table = QtWidgets.QTableWidget(self.tab_4)
        self.table.setObjectName("table")
        self.table.setRowCount(60)
        self.table.setColumnCount(5)
        self.exportPDF = QtWidgets.QPushButton(self.tab_4)
        self.exportPDF.setObjectName("exportPDF")
        self.gridLayout_5.addWidget(self.table)
        self.gridLayout_5.addWidget(self.exportPDF)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.scrollLayout = QtWidgets.QFormLayout()
        self.scrollWidget = QtWidgets.QWidget()
        self.scrollWidget.setLayout(self.scrollLayout)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)

        self.mainLayout = QtWidgets.QVBoxLayout(self.tab_2)

        self.mainLayout.addWidget(self.scrollArea)
        self.mainLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(bolt_ui)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bolt_ui)
        bolt_ui.setTabOrder(self.tabWidget, self.nClampedPartsText)
        bolt_ui.setTabOrder(self.nClampedPartsText, self.typeCombo)
        bolt_ui.setTabOrder(self.typeCombo, self.sizeCombo)
        bolt_ui.setTabOrder(self.sizeCombo, self.sizelineEdit)
        bolt_ui.setTabOrder(self.sizelineEdit, self.pitchlineEdit)
        bolt_ui.setTabOrder(self.pitchlineEdit, self.thicklineEdit)
        bolt_ui.setTabOrder(self.thicklineEdit, self.rBlock_2)
        bolt_ui.setTabOrder(self.rBlock_2, self.sBlock_2)
        bolt_ui.setTabOrder(self.sBlock_2, self.tBlock_2)
        bolt_ui.setTabOrder(self.tBlock_2, self.uBlock_2)
        bolt_ui.setTabOrder(self.uBlock_2, self.lengthText)
        bolt_ui.setTabOrder(self.lengthText, self.gradeCombo)
        bolt_ui.setTabOrder(self.gradeCombo, self.relineedit)
        bolt_ui.setTabOrder(self.relineedit, self.rmlineedit)
        bolt_ui.setTabOrder(self.rmlineedit, self.reclineedit)
        bolt_ui.setTabOrder(self.reclineedit, self.partCombo)
        bolt_ui.setTabOrder(self.partCombo, self.nutCombo)
        bolt_ui.setTabOrder(self.nutCombo, self.rBlock)
        bolt_ui.setTabOrder(self.rBlock, self.sBlock)
        bolt_ui.setTabOrder(self.sBlock, self.tBlock)
        bolt_ui.setTabOrder(self.tBlock, self.uBlock)
        bolt_ui.setTabOrder(self.uBlock, self.nutHeight)
        bolt_ui.setTabOrder(self.nutHeight, self.gradeNutCombo)
        bolt_ui.setTabOrder(self.gradeNutCombo, self.matBlock)
        bolt_ui.setTabOrder(self.matBlock, self.renutlineEdit)
        bolt_ui.setTabOrder(self.renutlineEdit, self.rmnutlineEdit)
        bolt_ui.setTabOrder(self.rmnutlineEdit, self.recnutlineEdit)
        bolt_ui.setTabOrder(self.recnutlineEdit, self.saveInput)
        bolt_ui.setTabOrder(self.saveInput, self.resetInput)
        bolt_ui.setTabOrder(self.resetInput, self.saveClamp)
        bolt_ui.setTabOrder(self.saveClamp, self.resetClamp)
        bolt_ui.setTabOrder(self.resetClamp, self.axialForcelineEdit)
        bolt_ui.setTabOrder(self.axialForcelineEdit, self.shearForcelineEdit)
        bolt_ui.setTabOrder(self.shearForcelineEdit, self.betalineEdit)
        bolt_ui.setTabOrder(self.betalineEdit, self.uminlineEdit)
        bolt_ui.setTabOrder(self.uminlineEdit, self.torquelineEdit)
        bolt_ui.setTabOrder(self.torquelineEdit, self.tightAccuracylineEdit)
        bolt_ui.setTabOrder(self.tightAccuracylineEdit, self.utlineEdit)
        bolt_ui.setTabOrder(self.utlineEdit, self.delutlineEdit)
        bolt_ui.setTabOrder(self.delutlineEdit, self.ublineEdit)
        bolt_ui.setTabOrder(self.ublineEdit, self.delublineEdit)
        bolt_ui.setTabOrder(self.delublineEdit, self.yelineEdit)
        bolt_ui.setTabOrder(self.yelineEdit, self.thetalineEdit)
        bolt_ui.setTabOrder(self.thetalineEdit, self.calculateEL)
        bolt_ui.setTabOrder(self.calculateEL, self.resetEL)
        bolt_ui.setTabOrder(self.resetEL, self.exportPDF)

    def retranslateUi(self, bolt_ui):
        _translate = QtCore.QCoreApplication.translate
        bolt_ui.setWindowTitle(_translate("bolt_ui", "Bolt Calculation UX"))
        self.pitchlabel.setText(_translate("bolt_ui", "Pitch:"))
        self.label_9.setText(_translate("bolt_ui", "Type of nut:"))
        self.label_10.setText(_translate("bolt_ui", "Grade:"))
        self.label_14.setText(_translate("bolt_ui", "Yield (Re):"))
        self.label_15.setText(_translate("bolt_ui", "Ultimate (Rw):"))
        self.resetInput.setText(_translate("bolt_ui", "Reset"))
        self.label_36.setText(_translate("bolt_ui", "Material:"))
        self.label_3.setText(_translate("bolt_ui", "Length:"))
        self.label.setText(_translate("bolt_ui", "<html><head/><body><p><span style=\" font-weight:600;\">Number of clamped parts:</span></p></body></html>"))
        self.label_16.setText(_translate("bolt_ui", "Rec:"))
        self.label_4.setText(_translate("bolt_ui", "Grade:"))
        self.label_13.setText(_translate("bolt_ui", "Rec:"))
        self.label_11.setText(_translate("bolt_ui", "Yield (Re):"))
        self.label_32.setText(_translate("bolt_ui", "<html><head/><body><p align=\"right\">r:</p></body></html>"))
        self.label_37.setText(_translate("bolt_ui", "Height:"))
        self.label_12.setText(_translate("bolt_ui", "Ultimate (Rw):"))
        self.nClampedPartsText.setPlaceholderText(_translate("bolt_ui", "Enter values between 2-10"))
        self.label_6.setText(_translate("bolt_ui", "Type:"))
        self.label_33.setText(_translate("bolt_ui", "s:"))
        self.saveInput.setText(_translate("bolt_ui", "Save"))
        self.label_34.setText(_translate("bolt_ui", "t:"))
        self.label_35.setText(_translate("bolt_ui", "u:"))
        self.label_5.setText(_translate("bolt_ui", "Size:"))
        self.label_2.setText(_translate("bolt_ui", "<html><head/><body><p><span style=\" font-weight:600;\">Bolt</span></p></body></html>"))
        self.label_8.setText(_translate("bolt_ui", "Type of part:"))
        self.label_7.setText(_translate("bolt_ui", "<html><head/><body><p><span style=\" font-weight:600;\">Threaded Part</span></p></body></html>"))
        self.thicklabel.setText(_translate("bolt_ui", "Thickness:"))
        self.sizeLabel.setText(_translate("bolt_ui", "Size:"))
        self.label_42.setText(_translate("bolt_ui", "s:"))
        self.label_41.setText(_translate("bolt_ui", "<html><head/><body><p align=\"right\">r:</p></body></html>"))
        self.label_43.setText(_translate("bolt_ui", "t:"))
        self.label_44.setText(_translate("bolt_ui", "u:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("bolt_ui", "Inputs"))
        self.resetClamp.setText(_translate("bolt_ui", "Reset"))
        self.saveClamp.setText(_translate("bolt_ui", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("bolt_ui", "Clamped Parts"))
        self.ublineEdit.setPlaceholderText(_translate("bolt_ui", "µb"))
        self.label_26.setText(_translate("bolt_ui", "<html><head/><body><p align=\"center\">±</p></body></html>"))
        self.delublineEdit.setPlaceholderText(_translate("bolt_ui", "Δµb"))
        self.label_27.setText(_translate("bolt_ui", "Equivalent stress tightening ratio (γE):"))
        self.calculateEL.setText(_translate("bolt_ui", "Calculate"))
        self.label_17.setText(_translate("bolt_ui", "Axial Force (Fa):"))
        self.label_18.setText(_translate("bolt_ui", "Shear Force (Ft):"))
        self.label_19.setText(_translate("bolt_ui", "Load Introduction Factor(β):"))
        self.label_20.setText(_translate("bolt_ui", "Co-efficient of friction (sliding faces) (µmin):"))
        self.label_28.setText(_translate("bolt_ui", "N"))
        self.label_29.setText(_translate("bolt_ui", "N"))
        self.label_30.setText(_translate("bolt_ui", "Nm"))
        self.label_31.setText(_translate("bolt_ui", "% Re"))
        self.label_21.setText(_translate("bolt_ui", "Applied torque (T):"))
        self.label_22.setText(_translate("bolt_ui", "Tightening torque accuracy (ΔT/T):"))
        self.label_23.setText(_translate("bolt_ui", "Thread coefficient of friction (µt ± Δµt):"))
        self.utlineEdit.setPlaceholderText(_translate("bolt_ui", "µt"))
        self.label_24.setText(_translate("bolt_ui", "<html><head/><body><p align=\"center\">±</p></body></html>"))
        self.resetEL.setText(_translate("bolt_ui", "Reset"))
        self.label_38.setText(_translate("bolt_ui", "%"))
        self.delutlineEdit.setPlaceholderText(_translate("bolt_ui", "Δµt"))
        self.label_25.setText(_translate("bolt_ui", "Friction co-efficient under the driven element (µb ± Δµb):"))
        self.thetalineEdit.setPlaceholderText(_translate("bolt_ui", "for oblong hole calculation only"))
        self.label_39.setText(_translate("bolt_ui", "Cone Angle (Ɵ):"))
        self.label_40.setText(_translate("bolt_ui", "degrees"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("bolt_ui", "External Loading"))
        self.exportPDF.setText(_translate("bolt_ui", "Export to PDF"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("bolt_ui", "Results"))

