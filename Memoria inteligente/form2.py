# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created: jue feb 27 21:51:11 2014
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from qt import *
from qttable import QTable
import sys
import numpy as np

entradat = open("db.data", "r")
dbanimales = np.array([ map( int, linea.split() ) for linea in entradat ])
z = len(dbanimales) 
print z
entrada1 = open("xy1.data", "r")
xy1 = np.array([ map( int, linea.split() ) for linea in entrada1 ])

entrada2 = open("xy2.data", "r")
xy2 = np.array([ map( int, linea.split() ) for linea in entrada2 ])

entrada3 = open("xy3.data", "r")
xy3 = np.array([ map( int, linea.split() ) for linea in entrada3 ])

entrada4 = open("xy4.data", "r")
xy4 = np.array([ map( int, linea.split() ) for linea in entrada4 ])

entrada5 = open("xy5.data", "r")
xy5 = np.array([ map( int, linea.split() ) for linea in entrada5 ])

entrada6 = open("xy6.data", "r")
xy6 = np.array([ map( int, linea.split() ) for linea in entrada6 ])

entrada7 = open("xy7.data", "r")
xy7 = np.array([ map( int, linea.split() ) for linea in entrada7 ])

y1 = np.r_[1, 0, 0, 0, 0, 0, 0]
y2 = np.r_[0, 1, 0, 0, 0, 0, 0]
y3 = np.r_[0, 0, 1, 0, 0, 0, 0]
y4 = np.r_[0, 0, 0, 1, 0, 0, 0]
y5 = np.r_[0, 0, 0, 0, 1, 0, 0]
y6 = np.r_[0, 0, 0, 0, 0, 1, 0]
y7 = np.r_[0, 0, 0, 0, 0, 0, 1]

entradam = open("memoria.data", "r")
memoria = np.array([ map( int, linea.split() ) for linea in entradam ]) 
for i in xrange(0, 41):
 for j in xrange(0, 15): 
  if xy1[i][j] == 1: 
   memoria [0][j] = 1 + memoria [0][j]
  elif  xy1[i][j] == 0:
   memoria [0][j] = -1 + memoria [0][j]   
for i in xrange(0, 20):
 for j in xrange(0, 15): 
  if xy2[i][j] == 1: 
   memoria [1][j] = 1 + memoria [1][j]
  elif  xy2[i][j] == 0:
   memoria [1][j] = -1 + memoria [1][j]
for i in xrange(0, 5):
 for j in xrange(0, 15): 
  if xy3[i][j] == 1: 
   memoria [2][j] = 1 + memoria [2][j]
  elif  xy3[i][j] == 0:
   memoria [2][j] = -1 + memoria [2][j]
for i in xrange(0, 13):
 for j in xrange(0, 15): 
  if xy4[i][j] == 1: 
   memoria [3][j] = 1 + memoria [3][j]
  elif  xy4[i][j] == 0:
   memoria [3][j] = -1 + memoria [3][j]
for i in xrange(0, 4):
 for j in xrange(0, 15): 
  if xy5[i][j] == 1: 
   memoria [4][j] = 1 + memoria [4][j]
  elif  xy5[i][j] == 0:
   memoria [4][j] = -1 + memoria [4][j]
for i in xrange(0, 8):
 for j in xrange(0, 15): 
  if xy6[i][j] == 1: 
   memoria [5][j] = 1 + memoria [5][j]
  elif  xy6[i][j] == 0:
   memoria [5][j] = -1 + memoria [5][j]
for i in xrange(0, 10):
 for j in xrange(0, 15): 
  if xy7[i][j] == 1: 
   memoria [6][j] = 1 + memoria [6][j]
  elif  xy7[i][j] == 0:
   memoria [6][j] = -1 + memoria [6][j]
print memoria
cont = 0
cony1 = 0
cony2 = 0 
cony3 = 0
cony4 = 0
cony5 = 0
cony6 = 0
cony7 = 0
entradat = open("xy1.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y1) == True:
  cont += 1
  cony1 += 1
entradat = open("xy2.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y2) == True:
  cont += 1
  cony2 += 1
entradat = open("xy3.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y3) == True:
  cont += 1
  cony3 += 1
entradat = open("xy4.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y4) == True:
  cont += 1
  cony4 += 1  
entradat = open("xy5.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y5) == True:
  cont += 1
  cony5 += 1
entradat = open("xy6.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == y6) == True:
  cont += 1
  cony6 += 1
entradat = open("xy5.data", "r")  
for linea in entradat:
 db = np.array( [ map( int, linea.split() ) ] ) 
 db = db.transpose()
 clase = np.dot(memoria,db)
 aux= clase.max()
 for i in xrange(0, 7):
  if clase[i][0] == aux:
   clase [i][0] = 1
  elif clase[i][0] < aux:
   clase [i][0] = 0
 clase = clase.transpose()
 if np.all(clase == 7) == True:
  cont += 1
  cony7 += 1  

class Form2(QDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        QDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form2")



        self.lineEdit2 = QLineEdit(self,"lineEdit2")
        self.lineEdit2.setGeometry(QRect(40,420,310,21))

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(30,340,181,31))
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

        self.pushButton2 = QPushButton(self,"pushButton2")
        self.pushButton2.setGeometry(QRect(620,330,141,31))

        self.pushButton3 = QPushButton(self,"pushButton3")
        self.pushButton3.setGeometry(QRect(620,370,141,31))

        self.table1 = QTable(self,"table1")
        self.table1.setGeometry(QRect(30,20,800,310))
        self.table1.setLineWidth(1)
        self.table1.setNumRows(101)
        self.table1.setNumCols(15)

        self.languageChange()

        self.resize(QSize(866,656).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.pushButton2,SIGNAL("clicked()"),self.addMatrix)
        self.connect(self.pushButton3,SIGNAL("clicked()"),self.addMem)


    def languageChange(self):
        self.setCaption(self.__tr("Form2"))
        self.textLabel1.setText(QString.null)
        self.pushButton2.setText(self.__tr("Generar BD"))
        self.pushButton3.setText(self.__tr("Memoria"))


    def addMatrix(self):
		filas = self.table1.numRows()
		col = self.table1.numCols()
		for i in range(0, filas):
			for j in range(0, col):
				val = str(dbanimales[i][j])
				self.table1.setText(i,j,val)
        

    def addMem(self):
	filas = self.table1.numRows()
	col = self.table1.numCols()
	for i in range(0, filas):
		for j in range(0, col):
			self.table1.clearCell(i,j)
        for i in range(0, 7):
		for j in range(0, 15):
			v = str(memoria[i][j])
			self.table1.setText(i,j,v)			

    def __tr(self,s,c = None):
        return qApp.translate("Form2",s,c)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    f = Form2()
    f.show()
    app.setMainWidget(f)
    app.exec_loop()
