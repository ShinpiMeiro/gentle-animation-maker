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
from shutil import rmtree
from pathlib import Path


class Params_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.transcription_path = ''
        self.audio_path = ''
        self.background_path = ''
        self.retranslateUi(MainWindow)
        self.audio_path_button.clicked.connect(self.audio_path_dialog)
        self.transcription_path_button.clicked.connect(self.transcription_path_dialog)
        self.background_path_button.clicked.connect(self.background_path_dialog)
        self.animate_button.clicked.connect(self.animate)

    def setupUi(self):
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

        self.label_transcription = QLabel(self.gridLayoutWidget)
        self.label_transcription.setObjectName("label_transcription")
        self.gridLayout.addWidget(self.label_transcription, 3, 0, 1, 1)

        self.label_audio = QLabel(self.gridLayoutWidget)
        self.label_audio.setObjectName("label_audio")
        self.gridLayout.addWidget(self.label_audio, 1, 0, 1, 1)

        self.animate_button = QPushButton(self.gridLayoutWidget)
        self.animate_button.setFlat(False)
        self.animate_button.setObjectName("animate_button")
        self.gridLayout.addWidget(self.animate_button, 7, 3, 1, 1)

        self.transcription_path_button = QPushButton()
        self.transcription_path_button.setCheckable(False)
        self.transcription_path_button.setAutoExclusive(False)
        self.transcription_path_button.setObjectName("transcription_path_button")
        self.gridLayout.addWidget(self.transcription_path_button, 3, 1, 1, 1)

        self.audio_path_button = QPushButton()
        self.audio_path_button.setCheckable(False)
        self.audio_path_button.setAutoExclusive(False)
        self.audio_path_button.setObjectName("audio_path_button")
        self.gridLayout.addWidget(self.audio_path_button, 1, 1, 1, 1)

        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        spacerItem4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)

        self.background_path_button = QPushButton()
        self.background_path_button.setCheckable(False)
        self.background_path_button.setAutoExclusive(False)
        self.background_path_button.setObjectName("background_path_button")
        self.gridLayout.addWidget(self.background_path_button, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "animation maker"))
        self.label_background.setText(_translate("MainWindow", "Choose your background (.png .jpg) file:"))
        self.animate_button.setText(_translate("MainWindow", "Animate"))
        self.transcription_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.label_transcription.setText(_translate("MainWindow", "Choose your transcription (.txt) file:"))
        self.audio_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.label_audio.setText(_translate("MainWindow", "Choose your audio (.mp3 .wav) file:"))
        self.background_path_button.setText(_translate("MainWindow", "Choose files..."))

    def transcription_path_dialog(self):
        self.transcription_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                              'c:\\', "Text files (*.txt)")

    def audio_path_dialog(self):
        self.audio_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                      'c:\\', "Audio (*.wav *.mp3)")

    def background_path_dialog(self):
        self.background_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                           'c:\\', "Picture (*.png *.jpg)")

    def animate(self):
        os.system(f'main.py {self.audio_path[0]} {self.transcription_path[0]} {json_path}')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(1200, 900))
        MainWindow.setMaximumSize(QSize(1200, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 1181, 841))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.browser = QWebEngineView(self.verticalLayoutWidget)
        self.browser.setUrl(QUrl("http://localhost:49154"))
        self.verticalLayout_2.addWidget(self.browser)
        self.browser.urlChanged.connect(self.printurl)

        self.link = ''
        self.link_flag = False
        self.run_button = QPushButton(self.verticalLayoutWidget)
        self.run_button.clicked.connect(self.run)
        self.run_button.setHidden(True)

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
            self.run_button.setHidden(False)
            self.link = str(self.browser.url().url()) + 'align.json'
            self.link_flag = True

    def run(self):
        global json_path
        if self.link_flag:
            if os.path.exists('current_test'):
                for file in os.listdir('current_test'):
                    os.remove(os.path.join('current_test', file))
            else:
                os.mkdir('current_test')
            with open('current_test/a.json', 'w') as f:
                res = requests.get(self.link)
                json.dump(res.json(), f, indent=2)
                json_path = os.path.abspath("current_test/a.json")
            self.w = Params_Window()
            self.w.show()
            self.w.hide()


json_path = ''
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
