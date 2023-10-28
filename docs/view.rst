view Module
============

:synopsis: The module named *view* runs the graphical interface of our app through the 'electrical section calculator'. Inside you will find three buttons to perform three different calculations, after that only remains indicate all the parameters and click "calculate". A messagge dialog will show you the result. On the future we'll going to expand the functions of this app.

Initial Section: Pyqt5 and MathCalculate class.
-----------------------------------------------

.. note::
   **from PyQt5 import QtCore, QtGui, QtWidgets** # Call Pyqt5 libreries
.. note::
   **from module import MathCalculate** # import the class responsable to do all the calculations


Pyqt5 GUI Modeling
--------------------
.. note::
   Please check out the Pyqt5 official documentation.

.. py:class:: Ui_MainWindow(object)

   .. py:method:: setupUi(self, MainWindow)

      :param  MainWindow: It refers to the *mainwindow* and will be the variable that defines the main window of our app with all its elements.


   .. note:: 
      **MainWindow.** defines size, color, title, adn widgets.

   .. py:method:: open_max_intake_window(self):

   .. py:method:: open_max_volt_drop(self):

   .. py:method:: open_short_circuit_window(self):

  .. note:: 
      
      **self.objectmath = MathCalculate()** # Object that refers to the maths operations of the Model Module
      
      **all this methods works to display us three different calculation windows.**


.. py:class:: Ui_Max_Intake_Intensity_Window(object)

   .. py:method:: f_max_intake(self)

      :param  self.objectmath.function_calculation_maximum_admissible_intensity: It refers to the module and the method we need to use for each case. 

   .. note:: 
      **all the remain windows will be create on the same mode.**

.. automodule:: view
   :undoc-members:
   :show-inheritance:

