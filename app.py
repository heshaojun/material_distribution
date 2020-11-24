import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self) -> None:
        self.setWindowTitle(u"物料分配")
        self.setWindowIcon(QIcon("./images/distribution.png"))
        desk = QApplication.desktop().screenGeometry()
        self.resize(desk.width() / 4, desk.height() / 4)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(./images/background_2.jpg);}")
        self.show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        msg_logout = QMessageBox.question(self, u"退出程序", u"是否确定退出？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg_logout == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    sys.exit(app.exec_())
