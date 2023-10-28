import sys
from PyQt5 import QtWidgets
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
import os
from view import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(
        self,
    ):

        QtWidgets.QMainWindow.__init__(
            self,
        )
        Ui_MainWindow.__init__(
            self,
        )
        self.setupUi(
            self,
        )


if __name__ == "__main__":
    dirname = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dirname, "plugins", "platforms")
    QtWidgets.QApplication.addLibraryPath(plugin_path)

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle(
        "Calculadora de secciones eléctricas / Electrical section calculator")
    widget.setFixedWidth(500)
    widget.setFixedHeight(184)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")
