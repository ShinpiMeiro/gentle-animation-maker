# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\am.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import requests
import json
import os


class Params_Window(QWidget):
    def __init__(self):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QSize(800, 600))
        self.centralwidget.setMaximumSize(QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QRect(9, 9, 781, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        self.label_background = QLabel(self.gridLayoutWidget)
        self.label_background.setObjectName("label_background")
        self.gridLayout.addWidget(self.label_background, 5, 0, 1, 1)
        self.transcription_path = QLineEdit(self.gridLayoutWidget)
        self.transcription_path.setInputMask("")
        self.transcription_path.setEchoMode(QLineEdit.Normal)
        self.transcription_path.setReadOnly(True)
        self.transcription_path.setObjectName("transcription_path")
        self.gridLayout.addWidget(self.transcription_path, 3, 2, 1, 2)
        self.animate_button = QPushButton(self.gridLayoutWidget)
        self.animate_button.setFlat(False)
        self.animate_button.setObjectName("animate_button")
        self.gridLayout.addWidget(self.animate_button, 7, 3, 1, 1)
        self.audio_path = QLineEdit(self.gridLayoutWidget)
        self.audio_path.setInputMask("")
        self.audio_path.setEchoMode(QLineEdit.Normal)
        self.audio_path.setReadOnly(True)
        self.audio_path.setObjectName("audio_path")
        self.gridLayout.addWidget(self.audio_path, 1, 2, 1, 2)
        self.transcription_path_button = QPushButton(self.gridLayoutWidget)
        self.transcription_path_button.setCheckable(False)
        self.transcription_path_button.setAutoExclusive(False)
        self.transcription_path_button.setObjectName("transcription_path_button")
        self.gridLayout.addWidget(self.transcription_path_button, 3, 1, 1, 1)
        self.label_transcription = QLabel(self.gridLayoutWidget)
        self.label_transcription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_transcription.setObjectName("label_transcription")
        self.gridLayout.addWidget(self.label_transcription, 3, 0, 1, 1)
        self.audio_path_button = QPushButton(self.gridLayoutWidget)
        self.audio_path_button.setCheckable(False)
        self.audio_path_button.setAutoExclusive(False)
        self.audio_path_button.setObjectName("audio_path_button")
        self.gridLayout.addWidget(self.audio_path_button, 1, 1, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        self.label_audio = QLabel(self.gridLayoutWidget)
        self.label_audio.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_audio.setObjectName("label_audio")
        self.gridLayout.addWidget(self.label_audio, 1, 0, 1, 1)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        self.background_path_button = QPushButton(self.gridLayoutWidget)
        self.background_path_button.setCheckable(False)
        self.background_path_button.setAutoExclusive(False)
        self.background_path_button.setObjectName("background_path_button")
        self.gridLayout.addWidget(self.background_path_button, 5, 1, 1, 1)
        self.background_path = QLineEdit(self.gridLayoutWidget)
        self.background_path.setInputMask("")
        self.background_path.setEchoMode(QLineEdit.Normal)
        self.background_path.setReadOnly(True)
        self.background_path.setObjectName("background_path")
        self.gridLayout.addWidget(self.background_path, 5, 2, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "animation maker"))
        self.label_background.setText(_translate("MainWindow", "Choose your background (.png) file:"))
        self.transcription_path.setText(_translate("MainWindow", "your path will be here"))
        self.animate_button.setText(_translate("MainWindow", "Animate"))
        self.audio_path.setText(_translate("MainWindow", "your path will be here"))
        self.transcription_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.label_transcription.setText(_translate("MainWindow", "Choose your transcription (.txt) file:"))
        self.audio_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.label_audio.setText(_translate("MainWindow", "Choose your audio (.wav) file:"))
        self.background_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.background_path.setText(_translate("MainWindow", "your path will be here"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(1200, 900))
        MainWindow.setMaximumSize(QSize(1200, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 1181, 841))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.browser = QWebEngineView(self.verticalLayoutWidget)
        self.browser.setUrl(QUrl("http://localhost:49153"))
        self.verticalLayout_2.addWidget(self.browser)
        self.browser.urlChanged.connect(self.printurl)

        self.link = ''
        self.link_flag = False
        self.run_button = QPushButton(self.verticalLayoutWidget)
        self.run_button.clicked.connect(self.run)

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_button.sizePolicy().hasHeightForWidth())

        self.run_button.setSizePolicy(sizePolicy)
        self.run_button.setObjectName("run_button")
        self.verticalLayout_2.addWidget(self.run_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Animation Maker"))
        self.run_button.setText(_translate("MainWindow", "Run"))

    def printurl(self):
        if 'transcriptions' in self.browser.url().url():
            self.link = str(self.browser.url().url()) + 'align.json'
            self.link_flag = True

    def run(self):
        if self.link_flag:
            if os.path.exists('current_test'):
                os.rmdir('current_test')
            os.mkdir('current_test')
            with open('current_test/a.json', 'w') as f:
                res = requests.get(self.link)
                json.dump(res.json(), f, indent=2)
            w = Params_Window()
            w.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())