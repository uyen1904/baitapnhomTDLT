from baitapnhomTDLT.Functions import solve_equation
from baitapnhomTDLT.ui.FirstDegreeEquation import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlot()
    def show(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        self.pushButtonSolution.clicked.connect(self.xuly_giai)
        self.pushButtonExit.clicked.connect(self.xuly_thoat)
        self.pushButtonClear.clicked.connect(self.xuly_xoa)
    def xuly_giai(self):
      try:
        a=float(self.lineEditcoefficient_a.text())
        b=float(self.lineEditcoefficient_b.text())
        result=solve_equation(a,b)
        self.lineEdit_result.setText(f"{result}")
      except:
          self.lineEdit_result.setText("invalid input")
    def xuly_thoat(self):
        self.MainWindow.close()
    def xuly_xoa(self):
        self.lineEditcoefficient_a.clear()
        self.lineEditcoefficient_b.clear()
        self.lineEdit_result.clear()

