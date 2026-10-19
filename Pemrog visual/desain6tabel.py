import sys
import PyQt5
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetitem
from PyQt5.uic import loadUi
import mysql.connector

class desain6 (QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('from_desain6.ui', self)
        self.setWindowTitle('PYTHON GUI & Mysql')
        self.buat_tabel_buku.clicked.connect(self.BuatTabelBuku)
        self.hapus_tabel_buku.clicked.connect(self.HapusTabelBuku)
        self.buat_tabel_anggota.clicked.connect(self.BuatTabelAnggota)
        self.hapus_tabel_anggota.clicked.connect(self.HapusTabelAnggota)
        self.buat_tabel_peminjaman.clicked.connect(self.BuatTabelPeminjaman)
        self.hapus_tabel_peminjaman.clicked.connect(self.HapusTabelPeminjaman)

    def tampilPesan(self, pesan):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Information)
        msgbox.setWindowTitle('PYTHON GUI & Mysql')
        msgbox.setText(pesan)
        msgbox.exec()

    def tampilTabel(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )
        query = "SHOW TABLES"
        cursor = con.cursor()
        cursor.execute(query)
        data_tabel = cursor.fetchall()

        
        con.close()


        n_tabel=len(data_tabel)
        self.tabelDatabase.setRowCount(n_tabel)
        baris=0
        for x in data_tabel:
            self.tabelDatabase.setItem(baris, 0, QTableWidgetItem(x[0]))
            baris=baris+1


    def BuatTabelBuku(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )

        query = "CREATE TABLE tbl_buku (isbn VARCHAR(15), judul VARCHAR(50), pengarang VARCHAR(30), penerbit VARCHAR(20), tahun INT, kategori VARCHAR(20), jumlah INT, PRIMARY KEY(isbn))"
        cursor = con.cursor()
        cursor.execute(query)

        con.close()

        self.tampilPesan("Tabel Buku telah berhasil dibuat !")

        self.tampilTabel()



    def BuatTabelAnggota(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )

        query = "CREATE TABLE anggota (nim VARCHAR(15), nama VARCHAR(50), jurusan VARCHAR(30), alamat VARCHAR(30), tempatlahir VARCHAR(30), tanggallahir DATE, PRIMARY KEY(nim))"
        cursor = con.cursor()
        cursor.execute(query)

        con.close()

        self.tampilPesan("Tabel Anggota telah berhasil dibuat !")
        
        self.tampilTabel()


        
    def BuatTabelPeminjaman(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )

        query = "CREATE TABLE pinjam (nim VARCHAR(15), nama VARCHAR(50), jurusan VARCHAR(30), isbn VARCHAR(15), judul VARCHAR(30), tanggalpinjam DATE, PRIMARY KEY(nim))"
        cursor = con.cursor()
        cursor.execute(query)

        con.close()

        self.tampilPesan("Tabel pinjam telah berhasil dibuat !")

        self.tampilTabel()



    def HapusTabelBuku(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )
        query = "DROP TABLE IF EXISTS tbl_buku"
        cursor = con.cursor()
        cursor.execute(query)
        
        con.close()
        
        self.tampilPesan("Tabel Buku telah berhasil dihapus !")
        
        self.tampilTabel()



    def HapusTabelAnggota(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )
        query = "DROP TABLE anggota"
        cursor = con.cursor()
        cursor.execute(query)
        con.close()
        self.tampilPesan("Tabel Aggota telah berhasil dihapus !")
        self.tampilTabel()



    def HapusTabelPeminjaman(self):
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="wein160166",
            database="perpustakaan_db"
        )
        query = "DROP TABLE pinjam"
        cursor = con.cursor()
        cursor.execute(query)
        
        con.close()
        
        self.tampilPesan("Tabel telah berhasil dihapus !")
        
        self.tampilTabel()
        

        if __name__ == "__main__":
    app=QApplication (sys.argv)
    form=desain6()
    form.show()
    sys.exit(app.exec_())
