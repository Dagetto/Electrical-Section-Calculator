controller module
=================

:synopsis: The controller module manages access to the Calculation of Electrical Cross-Sections app. In its initial section, it imports the **pyqt5 functions, widgets, etc.** and the **view** module, followed by the Ui_MainWindow class. We are going to describe only the parts modified with python. We highly reccomend read Pyqt5´s official documentation

Initial Section: Pyqt5 y view Module.
-------------------------------------
.. note::
   **from PyQt5 import QtWidgets**
.. note::
   **PyQt5**
.. note::
   **from PyQt5.QtWidgets import QApplication, QMainWindow**
.. note::
   **import view** # It imports the module that runs our interface.
.. note::
   **from view import Ui_MainWindow** 

Class *MainWindow(QMainWindow, Ui_MainWindow)*
----------------------------------------------

.. py:class:: MainWindow

   .. py:method:: def __init__(self,):

        QtWidgets.QMainWindow.__init__(self,)
        Ui_MainWindow.__init__(self,)
        self.setupUi(self,)

if __name__ == "__main__":
    dirname = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dirname, "plugins", "platforms")
    QtWidgets.QApplication.addLibraryPath(plugin_path)

    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle("Calculadora de secciones eléctricas / Electrical section calculator")
    widget.setFixedWidth(500)
    widget.setFixedHeight(184)
    widget.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Window...")

.. automodule:: controller
   :members:
   :undoc-members:
   :show-inheritance:
