import requests
import sys
import os

from PyQt5 import QtWidgets

from Converter.requestapi import api_key


class Doviz(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.label1 = QtWidgets.QLabel("Amerikan Doları: ")
        self.line1 = QtWidgets.QLineEdit("")
        self.label2 = QtWidgets.QLabel("Euro: ")
        self.line2 = QtWidgets.QLineEdit("")
        self.label3 = QtWidgets.QLabel("Pound:")
        self.line3 = QtWidgets.QLineEdit("")
        self.buton = QtWidgets.QPushButton("Kur Bilgisini Göster")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.label1)
        v_box.addWidget(self.line1)
        v_box.addWidget(self.label2)
        v_box.addWidget(self.line2)
        v_box.addWidget(self.label3)
        v_box.addWidget(self.line3)
        v_box.addWidget(self.buton)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Döviz Hesaplama Programı")
        self.buton.clicked.connect(self.bilgiver)
        self.show()

    def bilgiver(self):

        self.line1.setText(format(self.bilgiusd))
        self.line2.setText(format(self.bilgieuro))
        self.line3.setText(format(self.bilgigbp))

    def dovizcev(self):
        self.api_key = "2aea0cd7887545a42810499fa7dea176"
        self.url = "http://data.fixer.io/api/latest?access_key=" + api_key

        self.dovizurl = "http://data.fixer.io/api/latest?access_key=eca01cf72474775bc5b1f3d519f1faa0&base=USD"
        self.responseusd = requests.get(self.dovizurl)
        self.jsonusd = self.responseusd.json()
        self.bilgiusd = self.jsonusd["rates"]["TRY"]
        self.eurourl = "http://data.fixer.io/api/latest?access_key=eca01cf72474775bc5b1f3d519f1faa0&base=EUR"

        self.responseeuro = requests.get(self.eurourl)
        self.jsoneuro = self.responseeuro.json()
        self.bilgieuro = self.jsoneuro["rates"]["TRY"]
        self.gbpurl = "http://data.fixer.io/api/latest?access_key=eca01cf72474775bc5b1f3d519f1faa0&base=GBP"

        self.responsegbp = requests.get(self.gbpurl)
        self.jsongbp = self.responsegbp.json()
        self.bilgigbp = self.jsongbp["rates"]["TRY"]




app = QtWidgets.QApplication(sys.argv)

doviz = Doviz()

sys.exit(app.exec_())









































