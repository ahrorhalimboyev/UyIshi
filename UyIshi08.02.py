#   1-masala
# RadioButtondan foydalanib 5ta test tuzing. Agar to'g'ri javob belgilansa +1 ball qo'shilsin 
# va agar noto'g'ri bo'lsa ball qo'shilmasin va oxirida umumiy bali chiqsin.
'''
from PyQt5. QtWidgets import QApplication, QWidget, QPushButton 
from PyQt5. QtWidgets import QRadioButton, QLabel, QMessageBox,QButtonGroup
from PyQt5. QtGui import QFont 
import sys 
import random
ls=[
    ['1. Undan qanchalik ko’p olaversangiz, u shunchalik kattalashib boraveradi. U nima?','xazina','chuqur','qarz'],
    ['2. Qaysi yegulikni pishirishda qancha tuz solsa ham, u sho’r bo’lib ketmaydi?','tuxum','kartoshka','piyoz'],
    ['3. Kim o’tirgan holda yuradi?','kenguru','shaxmatchi','yosh bola'],
    ['4. Men suvman va suv yuzasida suzib yuribman. Men kimman?','muz','cho’kkan odam','baliq'],
    ['5. Ular qanchalik ko’p bo’lsa, vazni shunchalik kamayib ketaveradi?','qor','pul','g’ovaklar']
]
count=0
app=QApplication( sys.argv) 
class Window(QWidget ):
    def __init__(self):
        super().__init__()
        self.setWindowTitle( "TEST" )
        self.setGeometry(100, 50,750,900) 
        self.start1() 
    
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",10))
        obj.move(x,y)

    def start1(self):
        self.kirish=QLabel("QUYIDAGI 5 TA QIZIQARLI SAVOLLARGA JAVOB BERING!",self )
        self.font(self.kirish,10,20)
    
        self.savol1=QLabel(ls[0][0],self )
        self.font(self.savol1,20,80)
        self.savol1v1=QRadioButton(ls[0][1],self) 
        self.font(self.savol1v1,40,110)
        self.savol1v2=QRadioButton(ls[0][2],self) 
        self.font(self.savol1v2,40,140)
        self.savol1v3=QRadioButton(ls[0][3] ,self) 
        self.font(self.savol1v3,40,170)
        self.gr1=QButtonGroup(self)
        self.gr1.addButton(self.savol1v1)
        self.gr1.addButton(self.savol1v2)
        self.gr1.addButton(self.savol1v3)

        self.savol2=QLabel(ls[1][0],self )
        self.font(self.savol2,20,220)
        self.savol2v1=QRadioButton(ls[1][1],self) 
        self.font(self.savol2v1,40,250)
        self.savol2v2=QRadioButton(ls[1][2],self) 
        self.font(self.savol2v2,40,280)
        self.savol2v3=QRadioButton(ls[1][3] ,self) 
        self.font(self.savol2v3,40,310)
        self.gr2=QButtonGroup(self)
        self.gr2.addButton(self.savol2v1)
        self.gr2.addButton(self.savol2v2)
        self.gr2.addButton(self.savol2v3)

        self.savol3=QLabel(ls[2][0],self )
        self.font(self.savol3,20,360)
        self.savol3v1=QRadioButton(ls[2][1],self) 
        self.font(self.savol3v1,40,390)
        self.savol3v2=QRadioButton(ls[2][2],self) 
        self.font(self.savol3v2,40,420)
        self.savol3v3=QRadioButton(ls[2][3] ,self) 
        self.font(self.savol3v3,40,450)
        self.gr3=QButtonGroup(self)
        self.gr3.addButton(self.savol3v1)
        self.gr3.addButton(self.savol3v2)
        self.gr3.addButton(self.savol3v3)

        self.savol4=QLabel(ls[3][0],self )
        self.font(self.savol4,20,500)
        self.savol4v1=QRadioButton(ls[3][1],self) 
        self.font(self.savol4v1,40,530)
        self.savol4v2=QRadioButton(ls[3][2],self) 
        self.font(self.savol4v2,40,560)
        self.savol4v3=QRadioButton(ls[3][3] ,self) 
        self.font(self.savol4v3,40,590)
        self.gr4=QButtonGroup(self)
        self.gr4.addButton(self.savol4v1)
        self.gr4.addButton(self.savol4v2)
        self.gr4.addButton(self.savol4v3)

        self.savol5=QLabel(ls[4][0],self )
        self.font(self.savol5,20,640)
        self.savol5v1=QRadioButton(ls[4][1],self) 
        self.font(self.savol5v1,40,670)
        self.savol5v2=QRadioButton(ls[4][2],self) 
        self.font(self.savol5v2,40,700)
        self.savol5v3=QRadioButton(ls[4][3] ,self) 
        self.font(self.savol5v3,40,730)
        self.gr5=QButtonGroup(self)
        self.gr5.addButton(self.savol5v1)
        self.gr5.addButton(self.savol5v2)
        self.gr5.addButton(self.savol5v3)

        button=QPushButton("DONE",self)
        button.setFont(QFont("Times",18))
        button.setGeometry(600,800,100,50)
        button.clicked.connect(self.check)
        
    def check(self):
        self.count=0
        if self.savol1v2.isChecked():
            self.count+=1
        if self.savol2v1.isChecked():
            self.count+=1
        if self.savol3v2.isChecked():
            self.count+=1
        if self.savol4v1.isChecked():
            self.count+=1
        if self.savol5v3.isChecked():
            self.count+=1
        result=QMessageBox(self)
        result.setWindowTitle("RESULT")
        result.setText("You found " + str(self.count) + " out of 5 questions")
        result.show()
     
win=Window()
win.show()
sys.exit(app.exec_())
'''
#   2-masala
# Restoran menyusini tuzuvchi dastur tuzing. Unda 1-taomlar ro'yhati, 2-taomlar ro'yhati, ichimliklar va desert 
# ro'yhatidagi kamida 5tadan ma'lumotlarni CheckBox orqali tanlaydi va oxirida Chek ro'yhati chiqarilsin. 
# Chek quyidagi ko'rinishda bo'lishi kerak:
# 1-taomlar: tanlanganlar ro'yhati (narxlari bilan)
# 2-taomlar: tanlanganlar ro'yhati (narxlari bilan)
# Ichimliklar: tanlanganlar ro'yhati (narxlari bilan)
# Desert: tanlanganlar ro'yhati (narxlari bilan)

from PyQt5.QtWidgets import QApplication,QWidget, QPushButton,QCheckBox,QLabel,QMessageBox
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restoran menyusi")
        self.setGeometry(100,100,600,600)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",10))
        obj.move(x,y)
    def start(self):
        self.welcome=QLabel("Hush kelibsiz! \n\n\tBizda bor: ",self)
        self.font(self.welcome,20,20)
        
        self.taom1=QLabel("1-taomlar: ",self)
        self.font(self.taom1,10,100)
        self.taom1v1=QCheckBox("Mastava 12,000 so'm",self)
        self.font(self.taom1v1,100,100)
        self.taom1v2=QCheckBox("Sho'rva 17,000so'm",self)
        self.font(self.taom1v2,300,100)
        self.taom1v3=QCheckBox("Chuchvara 22,000 so'm",self)
        self.font(self.taom1v3,100,130)
        self.taom1v4=QCheckBox("Xo'rda 11,000 so'm",self)
        self.font(self.taom1v4,300,130)
        self.taom1v5=QCheckBox("Moshxo'rda 16,000 so'm",self)
        self.font(self.taom1v5,100,160)
        
        self.taom2=QLabel("2-taomlar: ",self)
        self.font(self.taom2,10,200)
        self.taom2v1=QCheckBox("Palov 18,000 so'm",self)
        self.font(self.taom2v1,100,200)
        self.taom2v2=QCheckBox("Jarkob 24,000so'm",self)
        self.font(self.taom2v2,300,200)
        self.taom2v3=QCheckBox("Manti 11,000 so'm",self)
        self.font(self.taom2v3,100,230)
        self.taom2v4=QCheckBox("Shashlik 17,000 so'm",self)
        self.font(self.taom2v4,300,230)
        self.taom2v5=QCheckBox("Norin 32,000 so'm",self)
        self.font(self.taom2v5,100,260)

        self.drinks=QLabel("Ichimliklar: ",self)
        self.font(self.drinks,10,300)
        self.drinksv1=QCheckBox("CocoCola 11,990 so'm",self)
        self.font(self.drinksv1,100,300)
        self.drinksv2=QCheckBox("Pepsi 11,590so'm",self)
        self.font(self.drinksv2,300,300)
        self.drinksv3=QCheckBox("Fanta 11,990 so'm",self)
        self.font(self.drinksv3,100,330)
        self.drinksv4=QCheckBox("Sharbat 16,500 so'm",self)
        self.font(self.drinksv4,300,330)
        self.drinksv5=QCheckBox("Mineral suv 7,000 so'm",self)
        self.font(self.drinksv5,100,360)
        
        self.desserts=QLabel("Shirinliklar: ",self)
        self.font(self.desserts,10,400)
        self.dessertsv1=QCheckBox("Cake 17,000 so'm",self)
        self.font(self.dessertsv1,100,400)
        self.dessertsv2=QCheckBox("Vafli 11,590so'm",self)
        self.font(self.dessertsv2,300,400)
        self.dessertsv3=QCheckBox("Snickers 15,990 so'm",self)
        self.font(self.dessertsv3,100,430)
        self.dessertsv4=QCheckBox("Cheesecake 24,500 so'm",self)
        self.font(self.dessertsv4,300,430)
        self.dessertsv5=QCheckBox("Ferrero rocher 37,000 so'm",self)
        self.font(self.dessertsv5,100,460)

        self.ready=QPushButton("Tayyor",self)
        self.font(self.ready,450,520)
        self.ready.clicked.connect(self.run)
    
    def run(self):
        self.welcome.setText("====Sizning hisob-kitobingiz====\n\n")
        self.welcome.adjustSize()
        self.sum=0
        if self.taom1v1.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom1v1.text()+"\n")
            self.sum+=12000
        if self.taom1v2.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom1v2.text()+"\n")
            self.sum+=17000
        if self.taom1v3.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom1v3.text()+"\n")
            self.sum+=22000
        if self.taom1v4.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom1v4.text()+"\n")
            self.sum+=11000
        if self.taom1v5.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom1v5.text()+"\n")
            self.sum+=16000
        if self.taom2v1.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom2v1.text()+"\n")
            self.sum+=18000
        if self.taom2v2.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom2v2.text()+"\n")
            self.sum+=24000
        if self.taom2v3.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom2v3.text()+"\n")
            self.sum+=11000
        if self.taom2v4.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom2v4.text()+"\n")
            self.sum+=17000
        if self.taom2v5.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.taom2v5.text()+"\n")
            self.sum+=32000
        if self.drinksv1.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.drinksv1.text()+"\n")
            self.sum+=11990
        if self.drinksv2.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.drinksv2.text()+"\n")
            self.sum+=11590
        if self.drinksv3.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.drinksv3.text()+"\n")
            self.sum+=11990
        if self.drinksv4.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.drinksv4.text()+"\n")
            self.sum+=16500
        if self.drinksv5.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.drinksv5.text()+"\n")
            self.sum+=7000
        if self.dessertsv1.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.dessertsv1.text()+"\n")
            self.sum+=17000
        if self.dessertsv2.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.dessertsv2.text()+"\n")
            self.sum+=11590
        if self.dessertsv3.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.dessertsv3.text()+"\n")
            self.sum+=15990
        if self.dessertsv4.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.dessertsv4.text()+"\n")
            self.sum+=24500
        if self.dessertsv5.isChecked():
            self.welcome.setText(self.welcome.text()+" "+self.dessertsv5.text()+"\n")
            self.sum+=37000
        
        self.welcome.setText(self.welcome.text()+"\n======================\nJAMI: "+str(self.sum) +" so'm")
        

        self.welcome.adjustSize()
        self.taom1.hide()
        self.taom1v1.hide()
        self.taom1v2.hide()
        self.taom1v3.hide()
        self.taom1v4.hide()
        self.taom1v5.hide()
        self.taom2.hide()
        self.taom2v1.hide()
        self.taom2v2.hide()
        self.taom2v3.hide()
        self.taom2v4.hide()
        self.taom2v5.hide()
        self.drinks.hide()
        self.drinksv1.hide()
        self.drinksv2.hide()
        self.drinksv3.hide()
        self.drinksv4.hide()
        self.drinksv5.hide()
        self.desserts.hide()
        self.dessertsv1.hide()
        self.dessertsv2.hide()
        self.dessertsv3.hide()
        self.dessertsv4.hide()
        self.dessertsv5.hide()
        self.ready.hide()

win=Window()
win.show()
sys.exit(app.exec_())

#   3-masala
# ComboBox orqali Tug'ilgan viloyatini, Tuman yoki shaharni, Jinsini va Millatini tanlasin va 
# Barcha tanlangan haqida ma'lumot chiqarilsin.
'''
from PyQt5.QtWidgets import QApplication,QWidget, QPushButton,QComboBox,QLabel
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Get_info_table")
        self.setGeometry(100,100,600,600)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",13))
        obj.move(x,y)
    def start(self):
        self.welcome=QLabel("O'zingiz haqingizdagi ma'lumotlarni to'ldiring!",self)
        self.font(self.welcome,20,20)
        self.viloyat=QLabel("Viloyat: ",self)
        self.font(self.viloyat,20,100)
        self.viloyats=QComboBox(self)
        self.viloyats.addItems(["---Tanlang---","Toshkent shahri","Andijon","Buxoro","Farg'ona","Jizzax","Xorazm","Namangan","Navoiy","Qashqadaryo","Qoraqalpog'iston R","Samarqand","Sirdaryo","Surxondaryo","Toshkent"])
        self.font(self.viloyats,20,140)
        self.tuman=QLabel("Tuman yoki shahar:",self)
        self.font(self.tuman,20,200)
        #self.tumans=QComboBox(self)
        #self.font(self.tumans,20,240)
        #self.tumans.addItems(["---Tanlang---"])
        if self.viloyats.currentText()!="":
            self.tumans=QComboBox(self)
            self.font(self.tumans,20,240)
            self.tumans.addItems(["---Tanlang---"])
            self.tumans.addItems(["Chortoq","Chust","Kosonsoy","Mingbuloq","Namangan shahri","Namangan tumani","Norin","Pop","To'raqo'rg'on","Uchqo'rg'on","Uychi","Yamgiqo'rg'on"])
        self.jins=QLabel("Jinsingiz:",self)
        self.font(self.jins,20,300)
        self.jinss=QComboBox(self)
        self.font(self.jinss,20,340)
        self.jinss.addItems(["---Tanlang---","Erkak","Ayol"])
        self.millat=QLabel("Millat:",self)
        self.font(self.millat,20,400)
        self.millats=QComboBox(self)
        self.font(self.millats,20,440)
        self.millats.addItems(["---Tanlang---","O'zbek","Tojik","Qoraqalpoq","Rus","Turk","Ingliz","Qozoq","Qirg'iz","Turkman","Afg'on"])
        self.button=QPushButton(self)
        self.button.setText("Saqlash")
        self.font(self.button,400,500)
        self.tt=QLabel("Tuman: ",self)
        self.font(self.tt,20,60)
        self.tt.hide()
        self.jj=QLabel("Jins: ",self)
        self.font(self.jj,20,100)
        self.jj.hide()
        self.mm=QLabel("Millat: ",self)
        self.font(self.mm,20,140)
        self.mm.hide()
        self.button.clicked.connect(self.run)
    def run(self):
        self.welcome.setText("Viloyat: "+self.viloyats.currentText())
        self.tt.show()
        self.tt.setText(self.tt.text()+" "+self.tumans.currentText())
        self.jj.show()
        self.jj.setText(self.jj.text()+" "+self.jinss.currentText())
        self.mm.show()
        self.mm.setText(self.mm.text()+" "+self.millats.currentText())
        
        self.tt.adjustSize()
        self.jj.adjustSize()
        self.mm.adjustSize()
        self.viloyat.hide()
        self.viloyats.hide()
        self.tuman.hide()
        self.tumans.hide()
        self.jins.hide()
        self.jinss.hide()
        self.millat.hide()
        self.millats.hide()
        self.button.hide()
win=Window()
win.show()
sys.exit(app.exec_())
'''