import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gui import Ui_MainWindow
from Playfair import Playfair


class PlayfairGUI(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.textEdit_Key.textChanged.connect(self.update_table)
        self.pushButton.clicked.connect(self.run_slot)
        self.update_table()

    def update_table(self):
        self.playfair = Playfair(key=self.textEdit_Key.toPlainText())
        for idx in range(25):
            label_table = getattr(self, 'label_table_{}'.format(idx))
            label_table.setText('<html><body><p><span style=\" color:#0055ff;\">{}</span></p></body></html>'.format(self.playfair.table[idx]))

    def run_slot(self):
        text = self.plainTextEdit.toPlainText()
        if self.radioButton_encrypt.isChecked():
            result = self.playfair.encrypt(text)
        else:
            result = self.playfair.decrypt(text)
        self.statusbar.showMessage('Original text: {}'.format(text))
        self.plainTextEdit.setPlainText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PlayfairGUI()
    form.show()
    sys.exit(app.exec_())
