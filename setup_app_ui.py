from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 360)
        MainWindow.setMinimumSize(QtCore.QSize(422, 360))
        MainWindow.setMaximumSize(QtCore.QSize(422, 360))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(422, 360))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnRunCrawler = QtWidgets.QPushButton(self.centralwidget)
        self.btnRunCrawler.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.btnRunCrawler.setFont(font)
        self.btnRunCrawler.setObjectName("btnRunCrawler")
        self.btnShowData = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowData.setGeometry(QtCore.QRect(220, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(12)
        self.btnShowData.setFont(font)
        self.btnShowData.setObjectName("btnShowData")
        self.lblStatus = QtWidgets.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(10, 70, 405, 31))
        font = QtGui.QFont()
        font.setFamily("Gill Sans Ultra Bold")
        font.setPointSize(9)
        self.lblStatus.setFont(font)
        self.lblStatus.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.lblStatus.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.lblStatus.setLineWidth(1)
        self.lblStatus.setMidLineWidth(1)
        self.lblStatus.setObjectName("lblStatus")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 411, 221))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 409, 219))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents_2)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setInvertedAppearance(False)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout.addWidget(self.verticalScrollBar)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.lblStatus.setText("Crawler is waiting for input")
        self.btnShowData.setEnabled(False)
        self.lblStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jobs.bg Webcrawler - Main"))
        self.btnRunCrawler.setText(_translate("MainWindow", "Run Crawler"))
        self.btnShowData.setText(_translate("MainWindow", "Show data"))
        self.lblStatus.setWhatsThis(_translate("MainWindow", "Labels the crawlers status"))