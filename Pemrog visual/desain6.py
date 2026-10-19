import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow,  QApplication, QMessageBox, QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.uic import loadUi
import mysql.connector

class desain6 (QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi ("desain6.ui", self)
        print("DESAIN BERHASIL DIBUAT")
        self.show()

        for t in self. findChildren(QPushButton):
            
            if "Buat Database" in t.text():
                t.clicked.connect(self.BuatDatabase)

    def BuatDatabase(self):
        print("TOMBOL DATABASE DIKLIK")
        print("FUNGSI BUAT DATABASE DIJALANKAN")

        try:
            con = mysql.connector.connect (
                host='localhost',
                user='root',
                password='wein160166',
                use_pure=True
            )

            print("KONEKSI MYSQL BERHASIL")

            cursor = con.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS perpustakaan_db")

            print("DATABASE BERHASIL DIBUAT")
            con.close()
            self.TampilPesan("Database Berhasil dibuat")

        except Exception as e:
            print("EROR:", e)


    def TampilPesan(self, Pesan):
        QMessageBox.information(self, "informasi", pesan)
        

if __name__ == "__main__":
    app=QApplication (sys.argv)
    form=desain6()
    sys.exit(app.exec_())
