from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 450)
        
        self.btnSimpan = QtWidgets.QPushButton(Dialog)
        self.btnSimpan.setGeometry(QtCore.QRect(20, 100, 100, 23))
        self.btnSimpan.setObjectName("btnSimpan")
        self.btnSimpan.clicked.connect(self.storeKategori)

        self.btnEdit = QtWidgets.QPushButton(Dialog)
        self.btnEdit.setGeometry(QtCore.QRect(140, 100, 100, 23))
        self.btnEdit.setObjectName("btnEdit")
        self.btnEdit.clicked.connect(self.updateKategori)

        self.btnDelete = QtWidgets.QPushButton(Dialog)
        self.btnDelete.setGeometry(QtCore.QRect(260, 100, 100, 23))
        self.btnDelete.setObjectName("btnDelete")
        self.btnDelete.clicked.connect(self.deleteKategori)

        self.lblOutput = QtWidgets.QLabel(Dialog)
        self.lblOutput.setGeometry(QtCore.QRect(20, 130, 400, 16))
        self.lblOutput.setObjectName("lblOutput")

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 20, 261, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.txtId = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txtId.setObjectName("txtId")
        self.verticalLayout.addWidget(self.txtId)
        self.txtNama = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txtNama.setObjectName("txtNama")
        self.verticalLayout.addWidget(self.txtNama)
        
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 91, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        
        self.btnGetData = QtWidgets.QPushButton(Dialog)
        self.btnGetData.setGeometry(QtCore.QRect(380, 100, 100, 23))
        self.btnGetData.setObjectName("btnGetData")
        self.btnGetData.clicked.connect(self.loadKategori)

        self.tblKategori = QtWidgets.QTableWidget(Dialog)
        self.tblKategori.setGeometry(QtCore.QRect(20, 160, 460, 270))
        self.tblKategori.setObjectName("tblKategori")
        self.tblKategori.setColumnCount(2)
        self.tblKategori.setRowCount(0)
        self.tblKategori.itemClicked.connect(self.selectRow)

        item = QtWidgets.QTableWidgetItem()
        self.tblKategori.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblKategori.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Form Kategori"))
        self.btnSimpan.setText(_translate("Dialog", "&Insert"))
        self.btnEdit.setText(_translate("Dialog", "&Edit"))
        self.btnDelete.setText(_translate("Dialog", "&Delete"))
        self.lblOutput.setText(_translate("Dialog", ""))
        self.label.setText(_translate("Dialog", "ID Kategori"))
        self.label_2.setText(_translate("Dialog", "Nama Kategori"))
        self.btnGetData.setText(_translate("Dialog", "&Get Data"))
        item = self.tblKategori.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tblKategori.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nama Kategori"))

    def storeKategori(self):
        try:
            myDB = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="py_visual3"
            )
            
            idKategori = self.txtId.text()
            namaKategori = self.txtNama.text()
            sql = "INSERT INTO kategori (id, nama) VALUES (%s, %s)"
            values = (idKategori, namaKategori)
            myCursor = myDB.cursor()
            myCursor.execute(sql, values)
            myDB.commit()
            
            self.lblOutput.setText("Berhasil menyimpan data")
            self.txtId.setText('')
            self.txtNama.setText('')
            self.loadKategori()
        except mysql.connector.Error as ex:
            self.lblOutput.setText("Gagal menyimpan data")

    def updateKategori(self):
        try:
            myDB = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="py_visual3"
            )

            idKategori = self.txtId.text()
            namaKategori = self.txtNama.text()
            sql = "UPDATE kategori SET nama = %s WHERE id = %s"
            values = (namaKategori, idKategori)
            myCursor = myDB.cursor()
            myCursor.execute(sql, values)
            myDB.commit()

            self.lblOutput.setText("Data berhasil diperbarui")
            self.txtId.setText('')
            self.txtNama.setText('')
            self.loadKategori()
        except mysql.connector.Error as ex:
            self.lblOutput.setText("Gagal memperbarui data")

    def deleteKategori(self):
        try:
            myDB = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="py_visual3"
            )

            idKategori = self.txtId.text()
            sql = "DELETE FROM kategori WHERE id = %s"
            values = (idKategori,)
            myCursor = myDB.cursor()
            myCursor.execute(sql, values)
            myDB.commit()

            self.lblOutput.setText("Data berhasil dihapus")
            self.txtId.setText('')
            self.txtNama.setText('')
            self.loadKategori()
        except mysql.connector.Error as ex:
            self.lblOutput.setText("Gagal menghapus data")

    def loadKategori(self):
        try:
            myDB = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="py_visual3"
            )

            myCursor = myDB.cursor()
            myCursor.execute("SELECT * FROM kategori ORDER BY id ASC")
            result = myCursor.fetchall()

            self.tblKategori.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tblKategori.insertRow(row_number)

                for column_number, data in enumerate(row_data):
                    self.tblKategori.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.lblOutput.setText("Kategori berhasil ditampilkan")
        except mysql.connector.Error as err:
            self.lblOutput.setText("Kategori gagal ditampilkan")

    def selectRow(self, item):
        row = item.row()
        self.txtId.setText(self.tblKategori.item(row, 0).text())
        self.txtNama.setText(self.tblKategori.item(row, 1).text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.show()
    sys.exit(app.exec_())
