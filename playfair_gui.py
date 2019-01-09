import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from gui import Ui_MainWindow
from setting import Ui_Setting_Dialog
from Playfair import Playfair


class settingGUI(QMainWindow, Ui_Setting_Dialog):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)


class PlayfairGUI(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.playfair = Playfair(key='')
        self.fakeletter = self.playfair.letter
        self.setupUi(self)
        self.setting = settingGUI()
        self.setting.setupUi(self.setting)
        self.setting.pushButton_setting_ok.clicked.connect(self.setting_ok_button)
        self.setting.plainTextEdit_letter.textChanged.connect(self.setting_fake_letter_limit)
        self.setting.plainTextEdit_letter.setPlainText(self.fakeletter)
        self.setting.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setting.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.setting.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        self.textEdit_Key.textChanged.connect(self.update_table)
        self.pushButton.clicked.connect(self.run_slot)
        self.actionFake_Letter.triggered.connect(self.open_setting)
        self.update_table()

    def update_table(self):
        self.playfair = Playfair(key=self.textEdit_Key.toPlainText())
        for idx in range(25):
            label_table = getattr(self, 'label_table_{}'.format(idx))
            label_table.setText('<html><body><p><span style=\" color:#0055ff;\">{}</span></p></body></html>'.format(self.playfair.table[idx]))

    def run_slot(self):
        if self.playfair.letter != self.fakeletter:
            self.playfair = Playfair(key=self.textEdit_Key.toPlainText(), letter=self.fakeletter)
        text = self.plainTextEdit.toPlainText()
        if self.radioButton_encrypt.isChecked():
            result = self.playfair.encrypt(text)
        else:
            result = self.playfair.decrypt(text)
        self.statusbar.showMessage('Original text: {}'.format(text))
        self.plainTextEdit.setPlainText(result)

    def setting_ok_button(self):
        if len(self.setting.plainTextEdit_letter.toPlainText()) != 1 or \
                not self.setting.plainTextEdit_letter.toPlainText().isalpha():
            warning = QMessageBox.warning(self.setting, 'Warning', 'Only Can Input A Alphabet!!', QMessageBox.Ok)
            self.setting.plainTextEdit_letter.setPlainText(self.fakeletter)
        else:
            self.fakeletter = self.setting.plainTextEdit_letter.toPlainText()[:1]
            self.setting.close()

    def open_setting(self):
        self.setting.show()

    def setting_fake_letter_limit(self):
        if len(self.setting.plainTextEdit_letter.toPlainText()) != 1 or \
                not self.setting.plainTextEdit_letter.toPlainText().isalpha():
            warning = QMessageBox.warning(self.setting, 'Warning', 'Only Can Input A Alphabet!!', QMessageBox.Ok)
            self.setting.plainTextEdit_letter.setPlainText(self.fakeletter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = PlayfairGUI()
    form.show()
    sys.exit(app.exec_())
