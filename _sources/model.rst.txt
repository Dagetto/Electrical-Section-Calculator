model Module
=============

:synopsis: The module named *model* is responsible to do all the maths calculation on our app.


Initial Section:
----------------

.. note::
   **from PyQt5.QtWidgets import QMessageBox** # We only import the dialogbox of the Pyqt5


Calculation functions.
----------------------
:synopsis: We will describe one of the methods within this module. All of them are similar in their operation.

.. py:class:: MathCalculate(Model)

   .. py:method:: __init__(self,):
      print('Ready to work')

   .. py:method:: function_calculation_maximum_admissible_intensity(self, inputfirstval, inputsecondval, inputthirdval, inputfourthval, inputfifthval): 
                  var_resistividad = float(inputfirstval.text())
                  var_L = float(inputsecondval.text())
                  var_s = float(inputthirdval.text())
                  var_t = float(inputfourthval.text())
                  var_I = float(inputfifthval.text())
                  R = (var_resistividad) * (var_L/var_s)
                  Q = (0.24*R*var_t*var_I**pot) / 1000 # this line will do all the work
.. note:: 
   When one of the methods is called, a calculation and a dialog box will be displayed that will show the requested result with the established format. The operation of the method is based on a simple try/else block that returns a positive result or invites you to review the values ​​in case the data entered is incorrect.

.. automodule:: model
   :members:
   :undoc-members:
   :show-inheritance:
