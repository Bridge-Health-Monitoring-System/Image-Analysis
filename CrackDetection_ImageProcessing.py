import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageChops, ImageTk
from cv2 import *
from datetime import datetime
from firebase import Firebase
from email.message import EmailMessage
import smtplib
import config

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1280, 778)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 778))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 778))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: #121212;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frameFirstFile = QtWidgets.QFrame(self.centralwidget)
        self.frameFirstFile.setGeometry(QtCore.QRect(20, 80, 401, 681))
        self.frameFirstFile.setAutoFillBackground(False)
        self.frameFirstFile.setStyleSheet("background-color: #332940;border: 1px solid white;border-radius: 10px;")
        self.frameFirstFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFirstFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFirstFile.setObjectName("frameFirstFile")
        self.labelFirstFile = QtWidgets.QLabel(self.frameFirstFile)
        self.labelFirstFile.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.labelFirstFile.setStyleSheet("background-color: #121212;border-radius: 0px;border: 2px solid white;")
        self.labelFirstFile.setTextFormat(QtCore.Qt.RichText)
        self.labelFirstFile.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFirstFile.setObjectName("labelFirstFile")
        self.pushButtonChooseFirstImage = QtWidgets.QPushButton(self.frameFirstFile)
        self.pushButtonChooseFirstImage.setGeometry(QtCore.QRect(50, 120, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonChooseFirstImage.setFont(font)
        self.pushButtonChooseFirstImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChooseFirstImage.setMouseTracking(True)
        self.pushButtonChooseFirstImage.setTabletTracking(True)
        self.pushButtonChooseFirstImage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonChooseFirstImage.setAutoFillBackground(False)
        self.pushButtonChooseFirstImage.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonChooseFirstImage.setObjectName("pushButtonChooseFirstImage")
        self.pushButtonCaptureFirstImage = QtWidgets.QPushButton(self.frameFirstFile)
        self.pushButtonCaptureFirstImage.setGeometry(QtCore.QRect(50, 250, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCaptureFirstImage.setFont(font)
        self.pushButtonCaptureFirstImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonCaptureFirstImage.setMouseTracking(True)
        self.pushButtonCaptureFirstImage.setTabletTracking(True)
        self.pushButtonCaptureFirstImage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonCaptureFirstImage.setAutoFillBackground(False)
        self.pushButtonCaptureFirstImage.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonCaptureFirstImage.setObjectName("pushButtonCaptureFirstImage")
        self.labelFirstImage = QtWidgets.QLabel(self.frameFirstFile)
        self.labelFirstImage.setGeometry(QtCore.QRect(10, 460, 384, 216))
        self.labelFirstImage.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelFirstImage.setText("")
        self.labelFirstImage.setObjectName("labelFirstImage")
        self.frameSecondFile = QtWidgets.QFrame(self.centralwidget)
        self.frameSecondFile.setGeometry(QtCore.QRect(440, 80, 401, 681))
        self.frameSecondFile.setAutoFillBackground(False)
        self.frameSecondFile.setStyleSheet("background-color: #332940;border: 1px solid white;border-radius: 10px;")
        self.frameSecondFile.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSecondFile.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSecondFile.setObjectName("frameSecondFile")
        self.labelSecondFile = QtWidgets.QLabel(self.frameSecondFile)
        self.labelSecondFile.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.labelSecondFile.setStyleSheet("background-color: #121212;border-radius: 0px;border: 2px solid white;")
        self.labelSecondFile.setTextFormat(QtCore.Qt.RichText)
        self.labelSecondFile.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSecondFile.setObjectName("labelSecondFile")
        self.pushButtonChooseSecondImage = QtWidgets.QPushButton(self.frameSecondFile)
        self.pushButtonChooseSecondImage.setGeometry(QtCore.QRect(50, 120, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonChooseSecondImage.setFont(font)
        self.pushButtonChooseSecondImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonChooseSecondImage.setMouseTracking(True)
        self.pushButtonChooseSecondImage.setTabletTracking(True)
        self.pushButtonChooseSecondImage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonChooseSecondImage.setAutoFillBackground(False)
        self.pushButtonChooseSecondImage.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonChooseSecondImage.setObjectName("pushButtonChooseSecondImage")
        self.pushButtonCaptureSecondImage = QtWidgets.QPushButton(self.frameSecondFile)
        self.pushButtonCaptureSecondImage.setGeometry(QtCore.QRect(50, 250, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonCaptureSecondImage.setFont(font)
        self.pushButtonCaptureSecondImage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonCaptureSecondImage.setMouseTracking(True)
        self.pushButtonCaptureSecondImage.setTabletTracking(True)
        self.pushButtonCaptureSecondImage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonCaptureSecondImage.setAutoFillBackground(False)
        self.pushButtonCaptureSecondImage.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonCaptureSecondImage.setObjectName("pushButtonCaptureSecondImage")
        self.labelSecondImage = QtWidgets.QLabel(self.frameSecondFile)
        self.labelSecondImage.setGeometry(QtCore.QRect(10, 460, 384, 216))
        self.labelSecondImage.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelSecondImage.setText("")
        self.labelSecondImage.setObjectName("labelSecondImage")
        self.frameResult = QtWidgets.QFrame(self.centralwidget)
        self.frameResult.setGeometry(QtCore.QRect(860, 80, 401, 681))
        self.frameResult.setAutoFillBackground(False)
        self.frameResult.setStyleSheet("background-color: #332940;border: 1px solid white;border-radius: 10px;")
        self.frameResult.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameResult.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameResult.setObjectName("frameResult")
        self.labelResult = QtWidgets.QLabel(self.frameResult)
        self.labelResult.setGeometry(QtCore.QRect(120, 20, 161, 31))
        self.labelResult.setStyleSheet("background-color: #121212;border-radius: 0px;border: 2px solid white;")
        self.labelResult.setTextFormat(QtCore.Qt.RichText)
        self.labelResult.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResult.setObjectName("labelResult")
        self.pushButtonComputeResult = QtWidgets.QPushButton(self.frameResult)
        self.pushButtonComputeResult.setGeometry(QtCore.QRect(50, 120, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonComputeResult.setFont(font)
        self.pushButtonComputeResult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonComputeResult.setMouseTracking(True)
        self.pushButtonComputeResult.setTabletTracking(True)
        self.pushButtonComputeResult.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonComputeResult.setAutoFillBackground(False)
        self.pushButtonComputeResult.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonComputeResult.setObjectName("pushButtonComputeResult")
        self.labelResultWindow = QtWidgets.QLabel(self.frameResult)
        self.labelResultWindow.setGeometry(QtCore.QRect(50, 450, 301, 91))
        self.labelResultWindow.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelResultWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.labelResultWindow.setObjectName("labelResultWindow")
        self.pushButtonUpdateResult = QtWidgets.QPushButton(self.frameResult)
        self.pushButtonUpdateResult.setGeometry(QtCore.QRect(50, 600, 301, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonUpdateResult.setFont(font)
        self.pushButtonUpdateResult.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonUpdateResult.setMouseTracking(True)
        self.pushButtonUpdateResult.setTabletTracking(True)
        self.pushButtonUpdateResult.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButtonUpdateResult.setAutoFillBackground(False)
        self.pushButtonUpdateResult.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.pushButtonUpdateResult.setObjectName("pushButtonUpdateResult")
        self.labelResultImage = QtWidgets.QLabel(self.frameResult)
        self.labelResultImage.setGeometry(QtCore.QRect(10, 220, 384, 216))
        self.labelResultImage.setStyleSheet("background-color: #121212;border: 0.5px solid white;border-radius: 8px;")
        self.labelResultImage.setText("")
        self.labelResultImage.setObjectName("labelResultImage")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(20, 10, 700, 51))
        self.labelTitle.setObjectName("labelTitle")
        self.comboBoxBridge = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxBridge.setGeometry(QtCore.QRect(750, 20, 220, 30))
        self.comboBoxBridge.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        self.comboBoxSite = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSite.setGeometry(QtCore.QRect(1020, 20, 220, 30))
        self.comboBoxSite.setStyleSheet("background-color: #1f1a24;color: rgb(255, 255, 255);border: 0.5px solid white;border-radius: 5px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelFirstFile.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Initial File</span></p></body></html>"))
        self.pushButtonChooseFirstImage.setText(_translate("MainWindow", "Choose First Image"))
        self.pushButtonCaptureFirstImage.setText(_translate("MainWindow", "Capture First Image"))
        self.labelSecondFile.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Test File</span></p></body></html>"))
        self.pushButtonChooseSecondImage.setText(_translate("MainWindow", "Choose Second Image"))
        self.pushButtonCaptureSecondImage.setText(_translate("MainWindow", "Capture Second Image"))
        self.labelResult.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Results</span></p></body></html>"))
        self.pushButtonComputeResult.setText(_translate("MainWindow", "Compute Result"))
        self.pushButtonUpdateResult.setText(_translate("MainWindow", "EMail Result"))
        self.labelResultWindow.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Result will be displayed here</span></p></body></html>"))
        self.labelTitle.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Crack Detection using Image Processing</span></p></body></html>"))
        self.comboBoxBridge.addItems(["Airoli Bridge","Bandra-Worli Sea-Link","Mumbai Trans Harbour Link","Vashi Bridge"])
        self.comboBoxSite.addItems(["1","2","3","4","5","6","7","8","9","10"])
        self.pushButtonCaptureFirstImage.clicked.connect(self.captureFirstImage)
        self.pushButtonCaptureSecondImage.clicked.connect(self.captureSecondImage)
        self.pushButtonChooseFirstImage.clicked.connect(self.chooseFirstImage)
        self.pushButtonChooseSecondImage.clicked.connect(self.chooseSecondImage)
        self.pushButtonComputeResult.clicked.connect(self.computeResult)
        self.pushButtonUpdateResult.clicked.connect(self.updateResult)

    def chooseFirstImage(self):
        #Path for choosing First Image
        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select First Image", ".../Documents/Crack Detection using Image Processing/", "PNG Files (*.png)")
        self.labelFirstImage.setPixmap(QtGui.QPixmap(filename[0]).scaled(384, 216))
        self.firstImage = filename[0]
        file_name = str(filename[0])
        self.timestampFirstImage = file_name[len(file_name)-30 : len(file_name)-4]

    def chooseSecondImage(self):
        #Path for choosing Second Image
        filename = QtWidgets.QFileDialog.getOpenFileName(None, "Select Second Image", ".../Documents/Crack Detection using Image Processing/", "PNG Files (*.png)")
        self.labelSecondImage.setPixmap(QtGui.QPixmap(filename[0]).scaled(384, 216))
        self.secondImage = filename[0]
        file_name = str(filename[0])
        self.timestampSecondImage = file_name[len(file_name)-30 : len(file_name)-4]

    def captureFirstImage(self):
        cap = cv2.VideoCapture(0)
        self.timestampFirstImage = str(datetime.now())
        while True:
            ret, frame = cap.read()
            windowName = "View Finder"
            cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
            cv2.setWindowProperty(windowName, cv2.WND_PROP_TOPMOST, cv2.WINDOW_GUI_NORMAL)
            cv2.imshow(windowName,frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #Path for saving First Captured Image
                cv2.imwrite(".../Documents/Crack Detection using Image Processing/"+self.timestampFirstImage+".png",frame)
                #Path for opening First Captured Image
                self.firstImage = ".../Documents/Crack Detection using Image Processing/"+self.timestampFirstImage+".png"
                break
        cap.release()
        cv2.destroyAllWindows()
        self.labelFirstImage.setPixmap(QtGui.QPixmap(self.firstImage).scaled(384, 216))

    def captureSecondImage(self):
        cap = cv2.VideoCapture(0)
        self.timestampSecondImage = str(datetime.now())
        while True:
            ret, frame = cap.read()
            windowName = "View Finder"
            cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
            cv2.setWindowProperty(windowName, cv2.WND_PROP_TOPMOST, cv2.WINDOW_GUI_NORMAL)
            cv2.imshow(windowName,frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                #Path for saving Second Captured Image
                cv2.imwrite(".../Documents/Crack Detection using Image Processing/"+self.timestampSecondImage+".png",frame)
                #Path for opening Second Captured Image
                self.secondImage = ".../Documents/Crack Detection using Image Processing/"+self.timestampSecondImage+".png"
                break
        cap.release()
        cv2.destroyAllWindows()
        self.labelSecondImage.setPixmap(QtGui.QPixmap(self.secondImage).scaled(384, 216))
    
    def computeResult(self):
        self.timestampResultImage = str(datetime.now())
        differenceImage = ImageChops.difference(Image.open(self.firstImage), Image.open(self.secondImage))
        #Path for saving Result Image
        differenceImage.convert('L').save(".../Documents/Crack Detection using Image Processing/"+self.timestampResultImage+".png")
        #Path for opening Result Image
        self.resultImage = ".../Documents/Crack Detection using Image Processing/"+self.timestampResultImage+".png"
        self.labelResultImage.setPixmap(QtGui.QPixmap(self.resultImage).scaled(384, 216))
        blackComponent = 0
        blackThreshold = 32
        differenceImageComponents = differenceImage.convert('L').getdata()
        for i in differenceImageComponents:
            if i < blackThreshold:
                blackComponent += 1
        self.change = (1 - blackComponent / len(differenceImageComponents)) * 100
        result = str(round(self.change, 2))
        message = "Change over time is " + result + "%"
        self.labelResultWindow.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">" + message + "</span></p></body></html>")
        firebase = Firebase(config.FIREBASE_CONFIG)
        db = firebase.database()
        db.child(self.comboBoxBridge.currentText()).child(self.comboBoxSite.currentText()).push(result)

    def updateResult(self):
        msg = EmailMessage()
        msg['Subject'] = "Image Processing Result "+ self.timestampResultImage
        msg['From'] = config.EMAIL_ADDRESS
        msg['To'] = config.RESULT_EMAIL_ADDRESS
        message = "Change from " + self.timestampFirstImage + "\n to " + self.timestampSecondImage + "\n computed at " + self.timestampResultImage + "\n at " + self.comboBoxBridge.currentText() + " Site No.: " + self.comboBoxSite.currentText() + "\n is " + str(round(self.change, 2)) + "%"
        msg.set_content(message)
        attachments = [self.firstImage, self.secondImage, self.resultImage]
        for path in attachments:
            with open(path,'rb') as file:
                data = file.read()
                name = path.split("\\")[-1]
            msg.add_attachment(data, maintype = 'application', subtype = 'octet-stream', filename = name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(config.EMAIL_ADDRESS, config.PASSWORD)
            smtp.send_message(msg)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
