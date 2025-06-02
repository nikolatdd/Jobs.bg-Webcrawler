import os
import sys

from PyQt6 import QtCore as qtc
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtGui as qtg

#Local imports
from lib.crawler import Crawler
from lib.constants import BASE_URL
from setup_app_ui import Ui_MainWindow
from lib.tableview_win import TableViewWidget
from lib.decorator import count_timer

class MainWindow(qtw.QMainWindow,Ui_MainWindow):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        #submain.py ui setup
        self.setupUi(self)

        #initialize crawler code
        self.crawler = Crawler(BASE_URL)

        self.btnRunCrawler.clicked.connect(self.runcrawler)
        self.btnShowData.clicked.connect(self.showdata)

        self.show()
        
    def runcrawler(self):
        "Run crawler on button click"
        print('Crawler started')

        # change cursor to wait icon:
        self.setCursor(qtc.Qt.CursorShape.WaitCursor)

        # needed to force processEvents
        qtw.QApplication.processEvents()

        # start crawler
        self.crawler.run()

        # if crawler ready:
        if self.crawler.status:
            self.lblStatus.setText('Ready!')
            self.btnShowData.setEnabled(True)

        self.setCursor(qtc.Qt.CursorShape.ArrowCursor)
    
    def showdata(self):
        "Show TableView table from db"
        self.tableViewWidget = TableViewWidget(parent=self)
        self.tableViewWidget.tableView.refresh_data()  # Ensure data is up-to-date
        self.tableViewWidget.show()
    

if __name__ == '__main__':

    app = qtw.QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec())