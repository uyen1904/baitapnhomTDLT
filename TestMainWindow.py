from PyQt6.QtWidgets import QApplication, QMainWindow
from MainWindowEx import MainWindowEx
app=QApplication([])
MainWindow=QMainWindow()
myui=MainWindowEx()
myui.setupUi(MainWindow)
myui.show()
app.exec()