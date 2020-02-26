from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_load(object):
    def setupUi(self, load):
        load.setObjectName("load")
        load.resize(614, 288)
        self.gridLayout = QtWidgets.QGridLayout(load)
        self.gridLayout.setObjectName("gridLayout")
        self.browseExcel = QtWidgets.QPushButton(load)
        self.browseExcel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseExcel.setObjectName("browseExcel")
        self.gridLayout.addWidget(self.browseExcel, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(load)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
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
        self.browseTCL = QtWidgets.QPushButton(load)
        self.browseTCL.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseTCL.setObjectName("browseTCL")
        self.gridLayout.addWidget(self.browseTCL, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(load)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.generate = QtWidgets.QPushButton(load)
        self.generate.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 4, 1, 1, 1)
        self.errorLabel = QtWidgets.QLabel(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.errorLabel.sizePolicy().hasHeightForWidth())
        self.errorLabel.setSizePolicy(sizePolicy)
        self.errorLabel.setMinimumSize(QtCore.QSize(50, 100))
        self.errorLabel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.gridLayout.addWidget(self.errorLabel, 6, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
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
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 7, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(load)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 3)

        self.retranslateUi(load)
        QtCore.QMetaObject.connectSlotsByName(load)
        load.setTabOrder(self.excel_file, self.tcl_file)
        load.setTabOrder(self.tcl_file, self.pretSPC)
        load.setTabOrder(self.pretSPC, self.generate)
        load.setTabOrder(self.generate, self.browseExcel)
        load.setTabOrder(self.browseExcel, self.browseTCL)

    def retranslateUi(self, load):
        _translate = QtCore.QCoreApplication.translate
        load.setWindowTitle(_translate("load", "Loadcase and Loadstep Generator for Hypermesh"))
        self.browseExcel.setText(_translate("load", "Browse"))
        self.label.setText(_translate("load", "Path to Excel file:"))
        self.label_2.setText(_translate("load", "Path to save TCL file:"))
        self.pretSPC.setPlaceholderText(_translate("load", "Empty if no Pretension"))
        self.browseTCL.setText(_translate("load", "Browse"))
        self.label_5.setText(_translate("load", "SPC ID for Pretension:"))
        self.generate.setText(_translate("load", "Generate"))
        self.label_6.setText(_translate("load", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Activity Log</span></p></body></html>"))


