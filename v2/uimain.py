#coding:gbk
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from requests import get
from json import loads
from urllib.parse import quote
from PyQt5.QtWidgets import QMessageBox
# Form implementation generated from reading ui file 'ȥ�Ķ���Ʊ.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(535, 859)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 341, 101))
        font = QtGui.QFont()
        font.setFamily("��������")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 51, 21))
        font = QtGui.QFont()
        font.setFamily("����ϸ��")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 140, 171, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 51, 31))
        font = QtGui.QFont()
        font.setFamily("����ϸ��")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 190, 171, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 260, 101, 41))
        font = QtGui.QFont()
        font.setFamily("����ϸ��")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(140, 270, 141, 22))
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 10, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 340, 151, 81))
        font = QtGui.QFont()
        font.setFamily("��������")
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 500, 481, 331))
        font = QtGui.QFont()
        font.setFamily("΢���ź�")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(65)

        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(297, 200, 241, 201))
        self.calendarWidget.setObjectName("calendarWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ȥ�Ķ���Ʊv2"))
        MainWindow.setStatusTip(_translate("MainWindow", "OK"))
        self.label.setText(_translate("MainWindow", "��Ʊ��ѯ"))
        self.label_2.setText(_translate("MainWindow", "���"))
        self.label_3.setText(_translate("MainWindow", "�յ�"))
        self.label_4.setText(_translate("MainWindow", "��������"))
        self.pushButton.setText(_translate("MainWindow", "��ѯ"))




import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_)
        self.calendarWidget.selectionChanged.connect(self.calW)
        self.times=1

        QMessageBox.information(self,"WELCOME",
                                "��ӭ������",
                                QMessageBox.Open)
    def calW(self):
        date=self.calendarWidget.selectedDate()
        # date=date
        self.dateEdit.setDate(date)
    def click_(self):
        if(self.times == 3):
            #Ͷ�Ź��
            QMessageBox.aboutQt(self)
            self.times=1
        self.times+=1
        s=self.lineEdit.text()
        e=self.lineEdit_2.text()
        d=self.dateEdit.text().replace("/","-")

        myd=d.split("-")
        d = "-"
        if(len(myd[1]) < 2):
            myd[1]="0"+myd[1]
        if (len(myd[2]) < 2):
            myd[2] = "0" + myd[2]
        d=d.join(myd)
        s = quote(s)
        e = quote(e)
        d = quote(d)

        # print(s,e,d
        #       )
        url = "https://train.qunar.com/dict/open/s2s.do?&dptStation=%s&arrStation=%s&date=%s&user=neibu" % (
            s, e, d
        )
        json = loads(get(url=url).text)

        # print(json)
        if (json["errcode"] != 0 or json["data"]["s2sBeanList"] == []):
            str_=""
            str_+="�鲻����\n"
            str_+=json["errmsg"]
            a=QMessageBox.critical(self,
                                "����",
                                str_,
                                QMessageBox.Yes|
                                QMessageBox.Cancel
                                )
            # self.textEdit.setPlainText(str_)\
            if(a == QMessageBox.Cancel):
                exit(-1)
            return 1
            # __import__("sys").exit(0)
        json = json["data"]["s2sBeanList"]
        str_=""

        for j in json:
            str_+="-" * 100
            str_+="\n"
            i = j["extraBeanMap"]

            str_+="���Σ�%s" % j["trainNo"]
            str_ += "\n"
            str_+="���г�ʼ��վ��%s" % j["startStationName"]
            str_ += "\n"
            str_+="���г��յ�վ��%s" % j["endStationName"]
            str_ += "\n"
            str_ +="�ϳ�վ����%s" % j["dptStationName"]
            str_ += "\n"
            str_ +="�³�վ����%s" % j["arrStationName"]
            str_ += "\n"
            str_ +="����ʱ�䣺%s" % j["dptTime"]
            str_ += "\n"
            str_ +="�³�ʱ�䣺%s" % j["arrTime"]
            str_ += "\n"
            str_ +="����ʱ�䣺%s" % i["startSaleTime"]
            str_ += "\n"
            str_ +="�г����ͣ�%s" % i["trainType"]
            str_ += "\n"
            str_ +="ȫ�̣�%s" % i["interval"]
            str_ += "\n"
            str_ +="Ʊ����Ϣ��"
            str_ += "\n"
            seats = j["seats"]

            def ticket(count):
                if (count < 0):
                    return "<�鲻��>"
                else:
                    return count


            for k in seats:
                msg = "%s���۸񣺣�%s��Ʊ����%s��" % (
                    k, seats[k]["price"], ticket(seats[k]["count"])
                )
                str_ +=msg
                str_ += "\n"

        self.textEdit.setPlainText(str_)
        QMessageBox.information(self,
                                "��ʾ",
                                "���",
                                QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())