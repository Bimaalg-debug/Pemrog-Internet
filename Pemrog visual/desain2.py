import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

class desain2 (QMainWindow):

    def __init__ (self):
        QMainWindow.__init__(self)
        loadUi ("desain2.ui", self)
        self.Mulai.clicked.connect (self. pesan)

    def pesan (self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle ('pesan')
        msgBox.setText ('Terima Kasih Sudah Berkunjung')
        msgBox.exec()

if __name__=='__main__':
    app=QApplication (sys.argv)
    form=desain2()
    form.show()
    sys.exit (app.exec_())
