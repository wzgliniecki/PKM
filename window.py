import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PKM")
        #self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        btn1 = QtGui.QPushButton("Sprawdz pozycje", self)
        btn1.clicked.connect(self.close_application)
        btn1.resize(btn1.minimumSizeHint())
        btn1.move(10, self.height()-30)

        btn2 = QtGui.QPushButton("Ustaw pociagi", self)
        btn2.clicked.connect(self.close_application)
        btn2.resize(btn2.minimumSizeHint())
        btn2.move(120, self.height()-30)

        self.create_slider(210,self.height()-50)

        self.show()

    def create_slider(self, x, y):
        l1 = QtGui.QLabel("Predkosc", self)
        l1.setAlignment(QtCore.Qt.AlignCenter)
        l1.move(x, y)

        slider_speed = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        slider_speed.setMinimum(10)
        slider_speed.setMaximum(30)
        slider_speed.setValue(20)
        slider_speed.setTickPosition(QtGui.QSlider.TicksBelow)
        slider_speed.setTickInterval(5)
        slider_speed.move(x, y+20)

    def check_position(self):
        print("test")

    def close_application(self):
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())
    #app.exec_()

run()