from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app.ui', self)
        self.show()

        self.btn.clicked.connect(self.write)

    def write(self):

        text = self.lineEdit.text()

        if text != "":
            self.label.setText(text)
            self.lineEdit.setText("")
        self.lineEdit.setFocus()

        # if self.lineEdit.text():
        #     text = self.lineEdit.text()
        #     self.label.setText(text)
        #     self.lineEdit.setText("")
        #     self.lineEdit.setFocus()
        #     print(text)


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()