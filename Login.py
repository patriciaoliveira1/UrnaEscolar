from PyQt5 import QtCore, QtWidgets, QtGui
from LoginT import Ui_Login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
