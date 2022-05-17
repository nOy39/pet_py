from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import Slot
import sys


class MainWindow(QMainWindow):
    def __init__(self, parent=None, title_txt=None, qt_obj=None, update_log_method=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("My App")
        button = QPushButton("Press Me", self)
        button.clicked.connect(say_hello)
        button.show()
        self.centralWidget()


@Slot()
def say_hello():
    print("Button clicked, Hello!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
