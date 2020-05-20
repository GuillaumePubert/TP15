from PySide2.QtWidgets import *
import Part1
class LabeledTextField(QWidget):
    def __init__(self,txt):
        QWidget.__init__(self)
        self.layoutH=QHBoxLayout()
        self.obj1=QLabel(txt)
        self.obj2=QTextEdit("")
        self.layoutH.addWidget(self.obj1)
        self.layoutH.addWidget(self.obj2)
        self.setMaximumHeight(50)
        self.setLayout(self.layoutH)

class ConfigurationDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.layoutV=QVBoxLayout()
        Label1=LabeledTextField("IP adress")
        Label2=LabeledTextField("User")
        Label3=LabeledTextField("Password")
        self.layoutV.addWidget(Label1)
        self.layoutV.addWidget(Label2)
        self.layoutV.addWidget(Label3)
        self.setLayout(self.layoutV)

if __name__ == "__main__":
    app = QApplication([])
    win = Part1.Window()
    win.show()
    ConfDialog = ConfigurationDialog()
    ConfDialog.show()
    app.exec_()
