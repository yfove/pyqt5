import sys

from PyQt.QtWidgets import QApplication,QLabel, QWidget 

# create an instance of QApplication
app = QApplication([])

# create the application GUI
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello,World!</h1>", parent=window)
helloMsg.move(60, 15)

# show applications GUI
window.show()

# runthe application event loop
sys.exit(app.exec())