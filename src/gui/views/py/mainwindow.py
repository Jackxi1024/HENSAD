# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Felipe\hensad\src\gui\views\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 5, 0, 1, 2)
        self.dtApproachLineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.dtApproachLineEdit.setInputMask("")
        self.dtApproachLineEdit.setMaxLength(3)
        self.dtApproachLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dtApproachLineEdit.setClearButtonEnabled(False)
        self.dtApproachLineEdit.setObjectName("dtApproachLineEdit")
        self.gridLayout_4.addWidget(self.dtApproachLineEdit, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 9, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.groupBox_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 4, 0, 1, 2)
        self.unitsComboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.unitsComboBox.setObjectName("unitsComboBox")
        self.unitsComboBox.addItem("")
        self.unitsComboBox.addItem("")
        self.gridLayout_4.addWidget(self.unitsComboBox, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.tiDiagramPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.tiDiagramPushButton.setEnabled(False)
        self.tiDiagramPushButton.setObjectName("tiDiagramPushButton")
        self.gridLayout_4.addWidget(self.tiDiagramPushButton, 6, 0, 1, 2)
        self.cascadeDiagramPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.cascadeDiagramPushButton.setEnabled(False)
        self.cascadeDiagramPushButton.setObjectName("cascadeDiagramPushButton")
        self.gridLayout_4.addWidget(self.cascadeDiagramPushButton, 7, 0, 1, 2)
        self.tqDiagramPushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.tqDiagramPushButton.setEnabled(False)
        self.tqDiagramPushButton.setObjectName("tqDiagramPushButton")
        self.gridLayout_4.addWidget(self.tqDiagramPushButton, 8, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_5 = QtWidgets.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 4, 2, 3, 1)
        self.hotFilmCoefTableView = QtWidgets.QTableView(self.groupBox)
        self.hotFilmCoefTableView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.hotFilmCoefTableView.setObjectName("hotFilmCoefTableView")
        self.gridLayout_2.addWidget(self.hotFilmCoefTableView, 6, 3, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.groupBox)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 5, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 4)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 4, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 3, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.groupBox)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_2.addWidget(self.line_7, 5, 0, 1, 2)
        self.hotStreamTableView = QtWidgets.QTableView(self.groupBox)
        self.hotStreamTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.hotStreamTableView.setObjectName("hotStreamTableView")
        self.gridLayout_2.addWidget(self.hotStreamTableView, 6, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addHotStreamPushButton = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/streams/add_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addHotStreamPushButton.setIcon(icon)
        self.addHotStreamPushButton.setObjectName("addHotStreamPushButton")
        self.horizontalLayout_5.addWidget(self.addHotStreamPushButton)
        self.deleteHotStreamPushButton = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/streams/delete_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteHotStreamPushButton.setIcon(icon1)
        self.deleteHotStreamPushButton.setObjectName("deleteHotStreamPushButton")
        self.horizontalLayout_5.addWidget(self.deleteHotStreamPushButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 2, 0, 1, 4)
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 3, 0, 1, 4)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)
        self.coldFilmCoefTableView = QtWidgets.QTableView(self.groupBox_2)
        self.coldFilmCoefTableView.setMaximumSize(QtCore.QSize(200, 16777215))
        self.coldFilmCoefTableView.setObjectName("coldFilmCoefTableView")
        self.gridLayout_3.addWidget(self.coldFilmCoefTableView, 6, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addColdStreamPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.addColdStreamPushButton.setIcon(icon)
        self.addColdStreamPushButton.setObjectName("addColdStreamPushButton")
        self.horizontalLayout_6.addWidget(self.addColdStreamPushButton)
        self.deleteColdStreamPushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.deleteColdStreamPushButton.setIcon(icon1)
        self.deleteColdStreamPushButton.setObjectName("deleteColdStreamPushButton")
        self.horizontalLayout_6.addWidget(self.deleteColdStreamPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 0, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.groupBox_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 3, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 4, 2, 1, 1)
        self.coldStreamTableView = QtWidgets.QTableView(self.groupBox_2)
        self.coldStreamTableView.setObjectName("coldStreamTableView")
        self.gridLayout_3.addWidget(self.coldStreamTableView, 6, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.groupBox_2)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 5, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.groupBox_2)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 5, 2, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.groupBox_2)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_3.addWidget(self.line_8, 4, 1, 3, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.groupBox_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_5.addWidget(self.line_4, 1, 0, 1, 1)
        self.summaryTableView = QtWidgets.QTableView(self.groupBox_4)
        self.summaryTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.summaryTableView.setObjectName("summaryTableView")
        self.gridLayout_5.addWidget(self.summaryTableView, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.hotUtilLabel = QtWidgets.QLabel(self.groupBox_5)
        self.hotUtilLabel.setText("")
        self.hotUtilLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hotUtilLabel.setObjectName("hotUtilLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.hotUtilLabel)
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.coldUtilLabel = QtWidgets.QLabel(self.groupBox_5)
        self.coldUtilLabel.setText("")
        self.coldUtilLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.coldUtilLabel.setObjectName("coldUtilLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.coldUtilLabel)
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.minExLabel = QtWidgets.QLabel(self.groupBox_5)
        self.minExLabel.setText("")
        self.minExLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.minExLabel.setObjectName("minExLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.minExLabel)
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.pinchLabel = QtWidgets.QLabel(self.groupBox_5)
        self.pinchLabel.setText("")
        self.pinchLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pinchLabel.setObjectName("pinchLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pinchLabel)
        self.gridLayout_6.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_5, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/files/open_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon2)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/files/save_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Diagrams"))
        self.dtApproachLineEdit.setPlaceholderText(_translate("MainWindow", "Type value here"))
        self.label_2.setText(_translate("MainWindow", "Units:"))
        self.unitsComboBox.setItemText(0, _translate("MainWindow", "SI"))
        self.unitsComboBox.setItemText(1, _translate("MainWindow", "US"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Minimum ΔT and Units</p></body></html>"))
        self.label.setText(_translate("MainWindow", "Minimum Temperature Approach:"))
        self.tiDiagramPushButton.setText(_translate("MainWindow", "Temperature Interval Diagram"))
        self.cascadeDiagramPushButton.setText(_translate("MainWindow", "Cascade Diagram"))
        self.tqDiagramPushButton.setText(_translate("MainWindow", "Composite Temperature-Enthalpy Diagram"))
        self.label_5.setText(_translate("MainWindow", "Hot Side (needs cooling)"))
        self.label_8.setText(_translate("MainWindow", "Stream Inputs"))
        self.label_9.setText(_translate("MainWindow", "Film Coefficients (Optional)"))
        self.addHotStreamPushButton.setText(_translate("MainWindow", "Add Stream"))
        self.deleteHotStreamPushButton.setText(_translate("MainWindow", "Remove Stream"))
        self.label_11.setText(_translate("MainWindow", "Stream Inputs"))
        self.label_6.setText(_translate("MainWindow", "Cold Side (needs heating)"))
        self.addColdStreamPushButton.setText(_translate("MainWindow", "Add Stream"))
        self.deleteColdStreamPushButton.setText(_translate("MainWindow", "Remove Stream"))
        self.label_10.setText(_translate("MainWindow", "Film Coefficients (Optional)"))
        self.label_7.setText(_translate("MainWindow", "Results Summary"))
        self.label_12.setText(_translate("MainWindow", "Hot Utility Requirement:"))
        self.label_14.setText(_translate("MainWindow", "Cold Utility Requirement:"))
        self.label_20.setText(_translate("MainWindow", "Minimal number of heat exchangers:"))
        self.label_22.setText(_translate("MainWindow", "Pinch temperature:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Opens a .hsd file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setToolTip(_translate("MainWindow", "New HENSAD case study."))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Saves the current case study into a .hsd file."))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
from gui.resources import icons_rc
