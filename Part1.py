from PySide2.QtWidgets import *

class ButtonsPanel(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layoutH=QHBoxLayout()
        self.b1=QPushButton("Configure")
        self.b2=QPushButton("Connect")
        self.b3=QPushButton("Disconnect")
        self.layoutH.addWidget(self.b1)
        self.layoutH.addWidget(self.b2)
        self.layoutH.addWidget(self.b3)
        self.setLayout(self.layoutH)
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.layoutV=QVBoxLayout()
        self.setMinimumSize(600,400)
        Bouton=ButtonsPanel()
        self.layoutV.addWidget(Bouton)
        self.notificationPanel=QTextEdit("")
        self.layoutV.addWidget(self.notificationPanel)
        self.resulTable=QTableWidget(5,3)
        self.resulTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layoutV.addWidget(self.resulTable)
        self.setLayout(self.layoutV)

#main dans Part2
