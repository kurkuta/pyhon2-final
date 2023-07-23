from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Shop"]
mycol = mydb["Products"]
prd = {"_id":1,"chick":2, "click":4, "agony":10}
mycol.insert_one(prd)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Increase = QtWidgets.QPushButton(self.centralwidget)
        self.Increase.setGeometry(QtCore.QRect(180, 260, 93, 28))
        self.Increase.setObjectName("Increase")
        self.Change = QtWidgets.QPushButton(self.centralwidget)
        self.Change.setGeometry(QtCore.QRect(310, 260, 93, 28))
        self.Change.setObjectName("Change")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(10, 350, 741, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Result.setFont(font)
        self.Result.setText("")
        self.Result.setObjectName("Result")
        self.ProductText = QtWidgets.QLineEdit(self.centralwidget)
        self.ProductText.setGeometry(QtCore.QRect(170, 80, 251, 41))
        self.ProductText.setObjectName("ProductText")
        self.PriceText = QtWidgets.QLineEdit(self.centralwidget)
        self.PriceText.setGeometry(QtCore.QRect(170, 160, 251, 41))
        self.PriceText.setObjectName("PriceText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Increase.setText(_translate("MainWindow", "Increase"))
        self.Change.setText(_translate("MainWindow", "Change"))
        self.label.setText(_translate("MainWindow", "Product:"))
        self.label_2.setText(_translate("MainWindow", "Price:"))
        self.Increase.clicked.connect(self.increase)
        self.Change.clicked.connect(self.change)

    def increase(self):
        try:
            if mycol.find_one({},{self.ProductText.text():1,"_id":0}) == {}:
                mycol.insert_one({self.ProductText.text():int(self.PriceText.text())})
            else:
                myquery = {self.ProductText.text():mycol.distinct(self.ProductText.text())[0]}
                newquery ={"$set":{self.ProductText.text():(mycol.distinct(self.ProductText.text())[0] + int(self.PriceText.text()))}}
                mycol.update_one(myquery,newquery)
        except pymongo.errors.OperationFailure or ValueError:
            QMessageBox().setWindowTitle("Field Error")
            QMessageBox().setText("Fill in all the fields with valid data")
            QMessageBox().setIcon(QMessageBox.Warning)
            QMessageBox().exec_()

    def change(self):
        try:
            if mycol.find_one({},{self.ProductText.text():1,"_id":0}) == {}:
                mycol.insert_one({self.ProductText.text():int(self.PriceText.text())})
            else:
                myquery = {self.ProductText.text():mycol.distinct(self.ProductText.text())[0]}
                newquery ={"$set":{self.ProductText.text():int(self.PriceText.text())}}
                mycol.update_one(myquery,newquery)
        except pymongo.errors.OperationFailure or ValueError:
            QMessageBox().setWindowTitle("Field Error")
            QMessageBox().setText("Fill in all the fields with valid data")
            QMessageBox().setIcon(QMessageBox.Warning)
            QMessageBox().exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
