from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import requests
import json
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.transcription_path = ''
        self.audio_path = ''
        self.background_path = ''
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

        self.label_json = QLabel(self.gridLayoutWidget)
        self.label_json.setObjectName("label_json")
        self.gridLayout.addWidget(self.label_json, 5, 0, 1, 1)

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

        self.json_path_button = QPushButton()
        self.json_path_button.setCheckable(False)
        self.json_path_button.setAutoExclusive(False)
        self.json_path_button.setObjectName("json_path_button")
        self.gridLayout.addWidget(self.json_path_button, 5, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.audio_path_button.clicked.connect(self.audio_path_dialog)
        self.transcription_path_button.clicked.connect(self.transcription_path_dialog)
        self.json_path_button.clicked.connect(self.json_path_dialog)
        self.animate_button.clicked.connect(self.animate)
        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "animation maker"))
        self.animate_button.setText(_translate("MainWindow", "Animate"))
        self.label_json.setText(_translate("MainWindow", "Choose test json file (.json) file:"))
        self.transcription_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.label_transcription.setText(_translate("MainWindow", "Choose test transcription (.txt) file:"))
        self.audio_path_button.setText(_translate("MainWindow", "Choose files..."))
        self.label_audio.setText(_translate("MainWindow", "Choose test audio (.mp3 .wav) file:"))
        self.json_path_button.setText(_translate("MainWindow", "Choose files..."))

    def transcription_path_dialog(self):
        self.transcription_path = QFileDialog.getOpenFileName(MainWindow, 'Open file',
                                                              'c:\\', "Text files (*.txt)")

    def audio_path_dialog(self):
        self.audio_path = QFileDialog.getOpenFileName(MainWindow, 'Open file',
                                                      'c:\\', "Audio (*.wav *.mp3)")

    def json_path_dialog(self):
        self.json_path = QFileDialog.getOpenFileName(MainWindow, 'Open file',
                                                           'c:\\', "Json (*.json)")

    def animate(self):
        os.system(f'main.py True {self.audio_path[0]} {self.transcription_path[0]} {self.json_path[0]}')

json_path = ''

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())