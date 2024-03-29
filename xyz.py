# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from tkinter.filedialog import askdirectory
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QTextList
import os
import datetime
import shutil
import json

timeSet = 0

try:
    with open('various_settings.json', 'r') as fin:
        data = json.load(fin)
        timeSet = float(data['minutes_backed'])
        print(timeSet)
except FileNotFoundError as exc:
    pass


class ModelessDialog(QDialog):
    global timeSet
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Baseline")
        self.setGeometry(800, 275, 300, 200)

        label = QLabel("Set time in minutes")
        self.label2 = QLabel("Time : {:,.2f}".format(timeSet))

        self.spinBox = QDoubleSpinBox()
        self.spinBox.valueChanged.connect(self.valueChang)
        self.spinBox.setSingleStep(10.0)
        self.spinBox.setMaximum(100)
        buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.label2)
        layout.addWidget(self.spinBox)
        layout.addWidget(buttonBox)
        self.resize(300, 200)
        self.setLayout(layout)

        okBtn = buttonBox.button(QDialogButtonBox.Ok)
        okBtn.clicked.connect(self.apply)

        cancelBtn = buttonBox.button(QDialogButtonBox.Cancel)
        cancelBtn.clicked.connect(self.reject)

    def saveTo(self,data):
        with open('various_settings.json','w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return

    def apply(self):
        global timeSet
        print(f"{self.spinBox.value()}")
        timeSet = self.spinBox.value()
        obj = {'minutes_backed': f'{timeSet}'}
        self.saveTo(obj)

    def valueChang(self):
        self.label2.setText("TimeNew : {:,.1f}".format(self.spinBox.value()))


class Ui_MainWindow(object):

    def keyPressEvent(self, event):  # Reimplement the event here, in your case, do nothing
        return

    def setupUi(self, MainWindow):
        self.files = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.mainTitle.setGeometry(QtCore.QRect(10, 0, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Light")
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.mainTitle.setFont(font)
        self.mainTitle.setObjectName("mainTitle")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 241, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.filesviewlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.filesviewlayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.filesviewlayout.setContentsMargins(0, 0, 0, 0)
        self.filesviewlayout.setObjectName("filesviewlayout")
        self.directoryOpen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.directoryOpen.setObjectName("directoryOpen")
        self.filesviewlayout.addWidget(self.directoryOpen)

        self.listView = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listView.setObjectName("listView")
        self.filesviewlayout.addWidget(self.listView)

        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(300, 50, 161, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        self.menuMain = QtWidgets.QMenu(self.menubar)
        self.menuMain.setObjectName("menuMain")
        self.menuOthers = QtWidgets.QMenu(self.menubar)
        self.menuOthers.setObjectName("menuOthers")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuOthers.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.directoryOpen.clicked.connect(self.openDir)
        self.pushButton.clicked.connect(self.backup_files)
        self.pushButton_2.clicked.connect(self.setTimer)

        self.path = ""

    def checker(self):
        print("Oh Okay!")

    def setTimer(self):
        self.dialog = ModelessDialog()
        self.dialog.show()

        # QMessageBox.about(self, "My message box", "Text1 = %s, Text2 = %s" % (
        #     self.edit1.text(), self.edit2.text()))



    def openDir(self):
        # self.files.clear()
        self.model.clear()
        self.path = QtWidgets.QFileDialog.getExistingDirectory(caption="Open GD Files Folder",
                                                               directory=os.path.join(os.getenv("LOCALAPPDATA"),
                                                                                      "GeometryDash"))
        for f in os.listdir(self.path):
            self.files.append(self.path + '/' + f)

        print(self.files)
        for i in self.files:
            item = QtGui.QStandardItem(i)
            self.model.appendRow(item)

    def backup_files(self):
        print(self.files)
        print("BackupFiles Button Pushed!")
        if not self.files:
            return
        else:
            pth = r'C:/Users/Dell/Documents/gdbacks'
            date = str(datetime.datetime.now().date())
            print(date)
            if os.path.exists(fr'C:/Users/Dell/Documents/gdbacks/{date}'):
                n_dir = fr'C:/Users/Dell/Documents/gdbacks/{date}-{len(os.listdir(pth)) + 1}'
                print(n_dir)
                os.mkdir(n_dir)
                for file in self.files:
                    print("ok")
                    print(f"{self.path}file")  # [43:])
                    shutil.copyfile(file,
                                    fr"{n_dir}/{file.split('/')[-1]}")
            else:
                print(self.path)
                nw_dir = fr'C:/Users/Dell/Documents/gdbacks/{date}'
                os.mkdir(nw_dir)
                for file in self.files:
                    print(os.path.join(self.path, file[43:]))
                for file in self.files:
                    shutil.copyfile(file,
                                    fr"{nw_dir}/{file.split('/')[-1]}")



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainTitle.setText(_translate("MainWindow", "GD File Backup-er"))
        self.pushButton.setText(_translate("MainWindow", "Backup Files"))
        self.pushButton_2.setText(_translate("MainWindow", "Set Timer"))
        self.directoryOpen.setText(_translate("MainWindow", "Open Directory"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.menuOthers.setTitle(_translate("MainWindow", "Others"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
