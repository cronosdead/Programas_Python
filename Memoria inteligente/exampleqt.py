# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form1.ui'
#
# Created: jue feb 27 17:46:30 2014
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from form1 import *
import sys


class Form1(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form1")



        self.listBox1 = QListBox(self,"listBox1")
        self.listBox1.setGeometry(QRect(60,20,451,281))

        self.lineEdit1 = QLineEdit(self,"lineEdit1")
        self.lineEdit1.setGeometry(QRect(60,310,330,31))

        self.pushButton1 = QPushButton(self,"pushButton1")
        self.pushButton1.setGeometry(QRect(390,310,121,41))
        self.pushButton1.setAutoDefault(0)

        self.languageChange()

        self.resize(QSize(600,480).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton1,SIGNAL("clicked()"),self.listBox1.clear)
        self.connect(self.lineEdit1,SIGNAL("returnPressed()"),self.addText)


    def languageChange(self):
        self.setCaption(self.__tr("Form1"))
        self.pushButton1.setText(self.__tr("Borrar"))


    def addText(self):
            e = self.lineEdit1.text().ascii()
            self.listBox1.insertItem(e)
            self.lineEdit1.clear()
        

    def __tr(self,s,c = None):
        return qApp.translate("Form1",s,c)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Form1()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()
