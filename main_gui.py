# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PneumoniaDetector.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from DetectorCore import Pneumonia_Detector
import pandas as pd
from pyqtspinner.spinner import WaitingSpinner
import math

class VisionThread(QtCore.QThread):
    def __init__(self, img_dir):
        QtCore.QThread.__init__(self)
        self.img_dir = img_dir
    
    def run(self):
        print(self.img_dir)
        detector = Pneumonia_Detector(8, self.img_dir)
        detector.runs()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1266, 709)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        self.Index = 0
        self.folderName = None
        self.df = pd.read_csv('patients_info.data')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setItemsExpandable(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.itemClicked.connect(self.clickedTreeItem)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.menuContextTree)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.gridLayout_5.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.ImageTab = QtWidgets.QWidget()
        self.ImageTab.setObjectName("ImageTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ImageTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.ImageTab)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        
        #Slider Zoom GUI Section Begin
        self.horizontalSlider = QtWidgets.QSlider(self.ImageTab)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setMinimum(20)
        self.horizontalSlider.setMaximum(80)
        self.horizontalSlider.valueChanged[int].connect(self.scaleImage)
        #Slider Zoom GUI Section End

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PneumoniaPercent = QtWidgets.QLabel(self.ImageTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PneumoniaPercent.sizePolicy().hasHeightForWidth())
        self.PneumoniaPercent.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.PneumoniaPercent.setFont(font)
        self.PneumoniaPercent.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.PneumoniaPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.PneumoniaPercent.setWordWrap(False)
        self.PneumoniaPercent.setObjectName("PneumoniaPercent")
        self.horizontalLayout_2.addWidget(self.PneumoniaPercent)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.ImageTab)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1154, 672))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.ChestImg = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChestImg.sizePolicy().hasHeightForWidth())
        self.ChestImg.setSizePolicy(sizePolicy)
        self.ChestImg.setText("")

        self.ChestImg.setScaledContents(True)
        self.ChestImg.setAlignment(QtCore.Qt.AlignCenter)
        self.ChestImg.setObjectName("ChestImg")

        self.gridLayout_3.addWidget(self.ChestImg, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.ImageTab, "")
        self.InfoTab = QtWidgets.QWidget()
        self.InfoTab.setObjectName("InfoTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.InfoTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(100, 50, 100, -1)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nameLabel.setFont(font)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameEdit = QtWidgets.QLineEdit(self.InfoTab)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameEdit)

        self.iDLabel = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.iDLabel.setFont(font)
        self.iDLabel.setObjectName("iDLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.iDLabel)
        self.iDLineEdit = QtWidgets.QLineEdit(self.InfoTab)
        self.iDLineEdit.setObjectName("iDLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.iDLineEdit)

        self.dateLabel = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dateLabel)
        self.dateDateTimeEdit = QtWidgets.QDateTimeEdit(self.InfoTab)
        self.dateDateTimeEdit.setObjectName("dateDateTimeEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateDateTimeEdit)

        self.birthLabel = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.birthLabel.setFont(font)
        self.birthLabel.setObjectName("birthLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.birthLabel)
        self.birthDateTimeEdit = QtWidgets.QDateTimeEdit(self.InfoTab)
        self.birthDateTimeEdit.setObjectName("birthDateTimeEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.birthDateTimeEdit)

        self.label_2 = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.radioButton = QtWidgets.QRadioButton(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.radioButton_2)
        self.label_3 = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.InfoTab)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.textEdit)

        #CANCEL AND SAVE BUTTON BEGIN

        self.DialogButton = QtWidgets.QDialogButtonBox(self.InfoTab)
        self.CancelButton = QtWidgets.QDialogButtonBox.Cancel
        self.SaveButton   = QtWidgets.QDialogButtonBox.Save
        self.DialogButton.setStandardButtons(self.CancelButton|self.SaveButton)
        self.DialogButton.accepted.connect(self.save)
        self.DialogButton.rejected.connect(self.cancel)
        
        #CANCEL AND SAVE BUTTON END
        
        
        
        
        self.DialogButton.setObjectName("DialogButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.DialogButton)
        self.gridLayout_4.addLayout(self.formLayout, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.InfoTab)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.InfoTab, "")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        #PREVIOUS BUTTON GUI BEGIN
        self.Previous = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Previous.sizePolicy().hasHeightForWidth())
        self.Previous.setSizePolicy(sizePolicy)
        self.Previous.setObjectName("Previous")
        self.Previous.clicked.connect(self.clickedPrevious)
        self.horizontalLayout.addWidget(self.Previous)
        #PREVIOUS BUTTON GUI END

        self.Next = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Next.sizePolicy().hasHeightForWidth())
        self.Next.setSizePolicy(sizePolicy)
        self.Next.setObjectName("Next")
        self.Next.clicked.connect(self.clickedNext)
        self.horizontalLayout.addWidget(self.Next)


        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 22))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #IMPORT GUI BEGIN
        self.Import = QtWidgets.QAction(MainWindow, shortcut="Ctrl+I", triggered = self.import_file)
        self.Import.setObjectName("Import")
        self.File.addAction(self.Import)
        #IMPORT GUI END

        #EXPORT GUI BEGIN
        self.Export = QtWidgets.QAction(MainWindow, shortcut="Ctrl+E", triggered = self.export)
        self.Import.setObjectName("Export")
        self.File.addAction(self.Export)
        #EXPORT GUI END
        self.menubar.addAction(self.File.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        if len(self.df.index) > 0:
            self.showTable()
            self.highlight_row(True)
            self.showData()

        self.spinner = WaitingSpinner(self.treeWidget,
                                        roundness=70.0, opacity=15.0,
                                        fade=70.0, radius=10.0, lines=12,
                                        line_length=10.0, line_width=5.0,
                                        speed=1.0, color=(78, 154, 6))
        self.gridLayout_5.addWidget(self.spinner)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PneumoniaDetector"))
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "ID"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Prediction"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(3, _translate("MainWindow", "Birth"))
        self.treeWidget.headerItem().setText(4, _translate("MainWindow", "Gender"))
        self.treeWidget.headerItem().setText(5, _translate("MainWindow", "Description"))
        self.treeWidget.headerItem().setText(6, _translate("MainWindow", "Date"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Patients List"))
        self.label.setText(_translate("MainWindow", "Zoom Slider: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ImageTab), _translate("MainWindow", "Xray Image"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.iDLabel.setText(_translate("MainWindow", "ID"))
        self.dateLabel.setText(_translate("MainWindow", "Date"))
        self.dateDateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.birthLabel.setText(_translate("MainWindow", "Birth"))
        self.birthDateTimeEdit.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.label_2.setText(_translate("MainWindow", "Gender"))
        self.radioButton.setText(_translate("MainWindow", "Male"))
        self.radioButton_2.setText(_translate("MainWindow", "Female"))
        self.label_3.setText(_translate("MainWindow", "Description"))
        self.label_4.setText(_translate("MainWindow", "PATIENT\'S PERSONAL INFORMATION"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InfoTab), _translate("MainWindow", "Patient Info"))
        self.Previous.setText(_translate("MainWindow", "Previous"))
        self.Next.setText(_translate("MainWindow", "Next"))
        self.File.setTitle(_translate("MainWindow", "File"))
        self.Import.setText(_translate("MainWindow", "Import"))
        self.Export.setText(_translate("MainWindow", "Export"))

    def scaleImage(self, value):
        scale_factor = value / 50
        self.ChestImg.resize(scale_factor * self.ChestImg.pixmap().size())
        self.ChestImg.setAlignment(QtCore.Qt.AlignCenter)
        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), scale_factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), scale_factor)
    
    #TO-DO ADJUST SCROLL BAR
    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value() + ((factor - 1) * scrollBar.pageStep() / 2)))

    def open(self):
        self.folderName = str(QtWidgets.QFileDialog.getExistingDirectory())
        if self.folderName:
            self.spinner.start()
            self.CVThread = VisionThread(self.folderName)
            self.CVThread.finished.connect(self.showAll)
            self.CVThread.start()

    
    def showAll(self):
        self.showData()
        self.clearQTreeWidget(self.treeWidget)
        self.showTable()
        self.highlight_row(True)
        self.spinner.stop()



    def import_file(self):
        self.open()

    def export(self):
        self.saveFileName = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QWidget(), "Save file", "patients_info_exp.xlsx", "Excel file (*.xlsx)")
        fileName , _ = self.saveFileName
        if fileName:
            self.df.iloc[:, :-1].to_excel(fileName, index = False)

        
    def showTable(self):
        print(len(self.df.index))
        for index in range(0, len(self.df.index)):
            row = self.dataIter(index)
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(row[0]))
            item.setText(1, str(row[1]))
            item.setText(2, str(row[2]))
            item.setText(3, str(row[3]))
            item.setText(4, str(row[4]))
            item.setText(5, str(row[5]))
            item.setText(6, str(row[6]))
            self.setColor(item, row[1])


    def setColor(self, item, percent):
        rgb = self.numberToColorHsl(percent)
        G = rgb[0]
        R = rgb[1]
        B = rgb[2]
        brush = QtGui.QBrush(QtGui.QColor(R, G, B))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(1, brush)


    def hslToRgb(self, h, s, l):
        if s == 0:
            r = g = b = l
        else:
            if l < 0.5:
                q = l * (1 + s)
            else:
                q = l + s - l * s
            p = 2 * l - q
            r = self.hue2rgb(p, q, h + 1/3)
            g = self.hue2rgb(p, q, h)
            b = self.hue2rgb(p, q, h - 1/3)

        return [math.floor(r * 255), math.floor(g * 255), math.floor(b * 255)]


    def hue2rgb(self, p, q, t):
        if(t < 0): t += 1
        if(t > 1): t -= 1
        if(t < 1/6): return p + (q - p) * 6 * t
        if(t < 1/2): return q
        if(t < 2/3): return p + (q - p) * (2/3 - t) * 6
        return p
    

    def numberToColorHsl(self, i):
        hue = i * 1.2 / 360
        rgb = self.hslToRgb(hue, 1, .5)
        return rgb


    def showData(self):
        print(self.Index)
        self.horizontalSlider.setValue(50)
        data_list = self.dataIter(self.Index)
        full_path = data_list[-1]
        id_label = data_list[0]
        percent = data_list[1]
        name = data_list[2]
        gender = data_list[4]
        description = data_list[5]
        self.ChestImg.setPixmap(QtGui.QPixmap(full_path))
        self.ChestImg.setAlignment(QtCore.Qt.AlignCenter)
        self.iDLineEdit.setText(id_label)
        self.PneumoniaPercent.setText(QtCore.QCoreApplication.translate("MainWindow", "<html><head/><body><p>PNEUMONIA PERCENTAGE: <span style=\" color:#ef2929;\">{}%</span></p></body></html>".format(percent)))
        try:
            self.nameEdit.setText(name)
        except:
            self.nameEdit.setText("")
        try:
            birth = data_list[3]
            QBirthDate = QtCore.QDate.fromString(birth, "dd/MM/yyyy")
            self.birthDateTimeEdit.setDate(QBirthDate)
        except:
            pass
        try:
            if gender == "Male":
                self.radioButton.setChecked(True)
            else:
                self.radioButton_2.setChecked(True)
        except:
            pass
        try:
            self.textEdit.setText(description)
        except:
            self.textEdit.setText("")
        try:
            date = data_list[6]
            QTestDate = QtCore.QDate.fromString(date, "dd/MM/yyyy")
            self.dateDateTimeEdit.setDate(QTestDate)
        except:
            pass


    def highlight_row(self, boolean):
        index = self.treeWidget.model().index(self.Index, 0)
        self.treeWidget.itemFromIndex(index).setSelected(boolean)


    def clickedNext(self):
        if self.Index != len(self.df.index) - 1 and self.ChestImg.pixmap() != None:
            self.highlight_row(False)
            self.Index += 1
            self.highlight_row(True)
            self.showData()
            

    def clickedPrevious(self):
        if self.Index != 0:
            self.highlight_row(False)
            self.Index -= 1
            self.highlight_row(True)
            self.showData()


    def clickedTreeItem(self):
        item = self.treeWidget.currentIndex()
        index = item.row()
        self.Index = index
        self.showData()


    def dataIter(self, indx):
        self.df = pd.read_csv('patients_info.data')
        row = self.df.iloc[indx, :].values.tolist()
        #print(row)
        return row

    def save(self):
        self.clearQTreeWidget(self.treeWidget)
        id_text = self.iDLineEdit.text()
        name_text = self.nameEdit.text()
        birth_text = self.birthDateTimeEdit.dateTime().toString(self.birthDateTimeEdit.displayFormat())
        if self.radioButton.isChecked():
            gender = "Male"
        else:
            gender = "Female"
        description_text = self.textEdit.toPlainText()
        date_text = self.dateDateTimeEdit.dateTime().toString(self.dateDateTimeEdit.displayFormat())
        self.update_csv(id_text, 'ID')
        self.update_csv(name_text, 'Name')
        self.update_csv(birth_text, 'Birth')
        self.update_csv(gender, 'Gender')
        self.update_csv(description_text, 'Description')
        self.update_csv(date_text, 'Date')
        self.showTable()
        self.highlight_row(True)
        
    def update_csv(self, value, column):
        self.df.at[self.Index, column] = value
        self.df.to_csv('patients_info.data', index = False)

    def cancel(self):
        self.showData()

    def menuContextTree(self, point):
        # Infos about the node selected.
        index = self.treeWidget.indexAt(point)

        if not index.isValid():
            return

        item = self.treeWidget.itemAt(point)
        name = item.text(0)  # The text of the node.

        # We build the menu.
        menu = QtWidgets.QMenu()
        menu.addSeparator()
        RemoveAction = QtWidgets.QAction("Remove {}".format(name), self.treeWidget, triggered=self.item_remove)
        menu.addAction(RemoveAction)
        menu.exec_(self.treeWidget.mapToGlobal(point))

    def clearQTreeWidget(self, tree):
        iterator = QtWidgets.QTreeWidgetItemIterator(tree, QtWidgets.QTreeWidgetItemIterator.All)
        while iterator.value():
            iterator.value().takeChildren()
            iterator +=1
        i = tree.topLevelItemCount()
        while i > -1:
            tree.takeTopLevelItem(i)
            i -= 1

    def item_remove(self):
        index_remove = self.treeWidget.currentIndex().row()
        try:
            self.df.drop(index = index_remove, inplace = True)
            self.df.reset_index(drop = True, inplace = True)
            self.df.to_csv("patients_info.data", index = False)
        except:
            pass
        self.clearQTreeWidget(self.treeWidget)
        self.Index = 0
        self.showTable()
        try:
            self.showData()
        except:
            self.reInitialized()
        print("Removed index {}".format(index_remove))

    def reInitialized(self):
        self.ChestImg.clear()
        self.iDLineEdit.clear()
        self.PneumoniaPercent.clear()
        self.nameEdit.clear()
        self.birthDateTimeEdit.clear()
        self.textEdit.clear()
        self.dateDateTimeEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
