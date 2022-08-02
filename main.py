from lexic import LexicalAnalyzer
from typing import Iterable
from pyqtapp import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QTextBrowser
from PyQt5.QtGui import QTextCursor
import sys

la = LexicalAnalyzer('temp.txt')

##############################################################

class window(QtWidgets.QMainWindow):

    # Interface initialization
    def __init__(self): 
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.input_text)

    # Input Text Processing Method
    def input_text(self):
        texttof = self.ui.textEdit.toPlainText()

        with open("temp.txt",'w') as f:
            pass

        with open('temp.txt', 'a') as f:
            f.write(texttof)

        print(self.ui.textEdit.toPlainText())
        self.ui.textBrowser.clear()
        self.ui.textBrowser.moveCursor(QTextCursor.Start)

        self.ui.textBrowser_2.clear()
        self.ui.textBrowser_2.moveCursor(QTextCursor.Start)

        # Starts the parsing function
        lexeme_list = la.run_analysis()
        self.ui.textBrowser.append(str(lexeme_list))
        print("")
        self.loadLexemes()
        self.ui.textBrowser.append(str(lexeme_list))
        print("")

    def loadLexemes(self):
        la = LexicalAnalyzer('temp.txt') # Loading code from txt file
        lexeme_list = la.run_analysis()
        table = [la.TW, la.TD, la.TNUM, la.TID]
        lexeme_list.reverse()

        # ERRORS INSERT
        # Lex Error
        self.ui.textBrowser_2.append(str(la.status))
        print("\n")
        
        ### Table processing
        #
        # Keywords table
        self.ui.tableWidget_7.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_7.setRowCount(len(la.TW))
        self.ui.tableWidget_7.setColumnCount(1)
        self.ui.tableWidget_7.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Keywords"))

        row_index = 0
        for i in range (len(la.TW)):
            self.ui.tableWidget_7.setVerticalHeaderItem(row_index, QTableWidgetItem(str(i)))
            self.ui.tableWidget_7.setItem(row_index, 0, QTableWidgetItem((la.TW[i])))
            row_index += 1

        # Delimiter table
        self.ui.tableWidget_8.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_8.setRowCount(len(la.TD))
        self.ui.tableWidget_8.setColumnCount(1)
        self.ui.tableWidget_8.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Delimiters"))

        row_index = 0
        for i in range (len(la.TD)):
            self.ui.tableWidget_8.setVerticalHeaderItem(row_index, QTableWidgetItem(str(i)))
            self.ui.tableWidget_8.setItem(row_index, 0, QTableWidgetItem((la.TD[i])))
            row_index += 1

        # Numbers table
        self.ui.tableWidget_5.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_5.setRowCount(len(la.TNUM))
        self.ui.tableWidget_5.setColumnCount(1)
        self.ui.tableWidget_5.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("Numbers"))

        row_index = 0
        for i in range (len(la.TNUM)):
            self.ui.tableWidget_5.setVerticalHeaderItem(row_index, QTableWidgetItem(str(i)))
            self.ui.tableWidget_5.setItem(row_index, 0, QTableWidgetItem((str(la.TNUM[i]))))
            row_index += 1

        # Identifier table
        self.ui.tableWidget_6.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget_6.setRowCount(len(la.TID))
        self.ui.tableWidget_6.setColumnCount(1)
        self.ui.tableWidget_6.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem("IDs"))

        row_index = 0
        for i in range (len(la.TID)):
            self.ui.tableWidget_6.setVerticalHeaderItem(row_index, QTableWidgetItem(str(i)))
            self.ui.tableWidget_6.setItem(row_index, 0, QTableWidgetItem((str(la.TID[i]))))
            row_index += 1

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())

create_app()