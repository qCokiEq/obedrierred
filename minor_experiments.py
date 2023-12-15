from PyQt5.QtWidgets import *

class ModelessDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Baseline")
        self.setGeometry(800, 275, 300, 200)

        label    = QLabel("Set time in minutes")
        self.label2 = QLabel("Time : {:,.2f}".format(0))

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

    def apply(self):
        print(f"{self.spinBox.value()}")

    def valueChang(self):
        self.label2.setText("TimeNew : {:,.1f}".format(self.spinBox.value()))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        label  = QLabel('Hello Dialog', self)
        button = QPushButton('Open Dialog', self)
        button.clicked.connect(self.showDialog)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def showDialog(self):
        self.dialog = ModelessDialog()
        self.dialog.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = Window()
    win.resize(300, 200)
    win.show()
    sys.exit(app.exec_())