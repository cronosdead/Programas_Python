# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created: jue feb 27 23:48:07 2014
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from qttable import QTable


class Form2(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form2")



        self.pushButton2 = QPushButton(self,"pushButton2")
        self.pushButton2.setGeometry(QRect(620,330,141,31))

        self.pushButton3 = QPushButton(self,"pushButton3")
        self.pushButton3.setGeometry(QRect(620,370,141,31))

        self.pushButton5 = QPushButton(self,"pushButton5")
        self.pushButton5.setGeometry(QRect(260,340,111,31))

        self.table1 = QTable(self,"table1")
        self.table1.setGeometry(QRect(30,20,800,310))
        self.table1.setLineWidth(1)
        self.table1.setNumRows(101)
        self.table1.setNumCols(15)

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(140,340,70,31))
        self.textLabel1.setPaletteBackgroundColor(QColor(0,255,255))
        pal = QPalette()
        cg = QColorGroup()
        cg.setColor(QColorGroup.Foreground,Qt.black)
        cg.setColor(QColorGroup.Button,QColor(192,192,192))
        cg.setColor(QColorGroup.Light,Qt.white)
        cg.setColor(QColorGroup.Midlight,QColor(223,223,223))
        cg.setColor(QColorGroup.Dark,QColor(96,96,96))
        cg.setColor(QColorGroup.Mid,QColor(128,128,128))
        cg.setColor(QColorGroup.Text,Qt.black)
        cg.setColor(QColorGroup.BrightText,Qt.white)
        cg.setColor(QColorGroup.ButtonText,Qt.black)
        cg.setColor(QColorGroup.Base,Qt.white)
        cg.setColor(QColorGroup.Background,QColor(0,255,255))
        cg.setColor(QColorGroup.Shadow,Qt.black)
        cg.setColor(QColorGroup.Highlight,QColor(0,0,128))
        cg.setColor(QColorGroup.HighlightedText,Qt.white)
        cg.setColor(QColorGroup.Link,Qt.black)
        cg.setColor(QColorGroup.LinkVisited,Qt.black)
        pal.setActive(cg)
        cg.setColor(QColorGroup.Foreground,Qt.black)
        cg.setColor(QColorGroup.Button,QColor(192,192,192))
        cg.setColor(QColorGroup.Light,Qt.white)
        cg.setColor(QColorGroup.Midlight,QColor(220,220,220))
        cg.setColor(QColorGroup.Dark,QColor(96,96,96))
        cg.setColor(QColorGroup.Mid,QColor(128,128,128))
        cg.setColor(QColorGroup.Text,Qt.black)
        cg.setColor(QColorGroup.BrightText,Qt.white)
        cg.setColor(QColorGroup.ButtonText,Qt.black)
        cg.setColor(QColorGroup.Base,Qt.white)
        cg.setColor(QColorGroup.Background,QColor(0,255,255))
        cg.setColor(QColorGroup.Shadow,Qt.black)
        cg.setColor(QColorGroup.Highlight,QColor(0,0,128))
        cg.setColor(QColorGroup.HighlightedText,Qt.white)
        cg.setColor(QColorGroup.Link,QColor(0,0,255))
        cg.setColor(QColorGroup.LinkVisited,QColor(255,0,255))
        pal.setInactive(cg)
        cg.setColor(QColorGroup.Foreground,QColor(128,128,128))
        cg.setColor(QColorGroup.Button,QColor(192,192,192))
        cg.setColor(QColorGroup.Light,Qt.white)
        cg.setColor(QColorGroup.Midlight,QColor(220,220,220))
        cg.setColor(QColorGroup.Dark,QColor(96,96,96))
        cg.setColor(QColorGroup.Mid,QColor(128,128,128))
        cg.setColor(QColorGroup.Text,QColor(128,128,128))
        cg.setColor(QColorGroup.BrightText,Qt.white)
        cg.setColor(QColorGroup.ButtonText,QColor(128,128,128))
        cg.setColor(QColorGroup.Base,Qt.white)
        cg.setColor(QColorGroup.Background,QColor(0,255,255))
        cg.setColor(QColorGroup.Shadow,Qt.black)
        cg.setColor(QColorGroup.Highlight,QColor(0,0,128))
        cg.setColor(QColorGroup.HighlightedText,Qt.white)
        cg.setColor(QColorGroup.Link,QColor(0,0,255))
        cg.setColor(QColorGroup.LinkVisited,QColor(255,0,255))
        pal.setDisabled(cg)
        self.textLabel1.setPalette(pal)

        self.lineEdit2 = QLineEdit(self,"lineEdit2")
        self.lineEdit2.setGeometry(QRect(40,420,310,21))

        self.languageChange()

        self.resize(QSize(866,656).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton2,SIGNAL("clicked()"),self.addMatrix)
        self.connect(self.pushButton3,SIGNAL("clicked()"),self.addMem)
        self.connect(self.pushButton5,SIGNAL("clicked()"),self.percent)
        self.connect(self.lineEdit2,SIGNAL("returnPressed()"),self.intvec)


    def languageChange(self):
        self.setCaption(self.__tr("Form2"))
        self.pushButton2.setText(self.__tr("Generar BD"))
        self.pushButton3.setText(self.__tr("Memoria"))
        self.pushButton5.setText(self.__tr("Porcentaje"))
        self.textLabel1.setText(QString.null)


    def addMatrix(self):
        print "Form2.addMatrix(): Not implemented yet"

    def addMem(self):
        print "Form2.addMem(): Not implemented yet"

    def percent(self):
        print "Form2.percent(): Not implemented yet"

    def intvec(self):
        print "Form2.intvec(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("Form2",s,c)
