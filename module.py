from PyQt5.QtWidgets import QMessageBox


class MathCalculate():
    def __init__(
        self,
    ):
        print('Ready to work')

    def function_calculation_maximum_admissible_intensity(
        self,
        inputfirstval,
        inputsecondval,
        inputthirdval,
        inputfourthval,
        inputfifthval
    ):

        pot = 2

        try:
            var_resistividad = float(inputfirstval.text())
            var_L = float(inputsecondval.text())
            var_s = float(inputthirdval.text())
            var_t = float(inputfourthval.text())
            var_I = float(inputfifthval.text())
            R = (var_resistividad) * (var_L/var_s)

            Q = (0.24*R*var_t*var_I**pot) / 1000

            print("El calor generado para la seccion elegida es de = ",
                  Q, "kcal", round(Q, 2), "kcal")
            result_text = "El calor generado para la sección elegida es de/The heat generated for the selected section is = {:.8f} kcal".format(
                Q)
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText(result_text)
            message_box.exec_()
        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText("Error, please verify the values")
            message_box.exec_()

    def function_calculation_singlephase_voltage_drop(
            self,
            inputfirstval,
            inputsecondval,
            inputthirdval,
            inputfourthval,
            inputfifthval,
    ):

        try:
            var_P = float(inputfirstval.text())
            var_L = float(inputsecondval.text())
            var_cond = float(inputthirdval.text())
            var_e = float(inputfourthval.text())
            var_V = float(inputfifthval.text())

            S = (2*var_P*var_L) / (var_cond*var_e*var_V)

            result_text = "Su sección deberá ser/Your section should be: {:.2f} mm2. Es recomendable que la sección comercial elegida sea inmediatamente superior a la calculada/It is recommended that the chosen commercial section be slightly larger than the calculated one.".format(
                S)
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText(result_text)
            message_box.exec_()
            print("Su seccion debera ser = ", S, "mm2", round(S, 2), "mm2")
            print(
                "\n Es recomendable que la seccion comercial elegida sea inmediata superior a la calculada.")

        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText("Error, please verify the values")
            message_box.exec_()

    def function_calculation_threephase_voltage_drop(
            self,
            inputfirstval,
            inputsecondval,
            inputthirdval,
            inputfourthval,
            inputfifthval,
    ):

        try:
            var_P = float(inputfirstval.text())
            var_L = float(inputsecondval.text())
            var_cond = float(inputthirdval.text())
            var_e = float(inputfourthval.text())
            var_V = float(inputfifthval.text())

            S = (var_P*var_L) / (var_cond*var_e*var_V)

            result_text = "Su sección deberá ser/Your section should be: {:.2f} mm2.Es recomendable que la sección comercial elegida sea inmediatamente superior a la calculada/It is recommended that the chosen commercial section be slightly larger than the calculated one. ".format(
                S)
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText(result_text)
            message_box.exec_()

            print("Su seccion debera ser = ", S, "mm2", round(S, 2), "mm2")
            print(
                "\n Es recomendable que la seccion comercial elegida sea inmediata superior a la calculada.")

        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText("Error, please verify the values")
            message_box.exec_()

    def function_shortcircuit(self,
                              inputfirstval,
                              inputsecondval,
                              inputthirdval,
                              inputfourthval,):

        try:
            var_L = float(inputfirstval.text())
            var_resistividad = float(inputsecondval.text())
            var_s = float(inputthirdval.text())
            var_U = float(inputfourthval.text())

            R = (var_resistividad*var_L) / var_s

            Icc = (0.8 * var_U) / R

            result_text = "El valor de corriente de cortocircuito mínimo es / The minimum short-circuit current value is: {:.2f} Amper".format(
                Icc)
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText(result_text)
            message_box.exec_()
            print("El valor de corriente de corto circuito minimo es ",
                  Icc, "A", "=", round(Icc, 2), "Amper")

        except:
            message_box = QMessageBox()
            message_box.setWindowTitle("Result")
            message_box.setText("Error, please verify the values")
            message_box.exec_()
