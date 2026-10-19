import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi

class desain1 (QMainWindow):

    def __init__ (self):
        QMainWindow.__init__(self)
        loadUi ("desain1.ui", self)
        self.Mulai.clicked.connect (self.Tampilpesan)

    def Tampilpesan (self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Informasi)
        msgBox.setWindowTitle ('pesan')
        msgBox.setText ('Terima Kasih Sudah Berkunjung')
        msgBox.exec()

if __name__=='__main__':
    app=QApplication (sys.argv)
    form=desain1()
    form.show()
    sys.exit (app.exec_())
