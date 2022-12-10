from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys

class PushButton(QPushButton):
    def __init__(self, text, checkable = False, enabled = True, *args, **kwargs):
        super(PushButton, self).__init__(*args, **kwargs)
        self.setText(text)
        self.setCheckable(checkable)
        self.setEnabled(enabled)
    
    def button_clicked(self):
        print("Button clicked!")


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.resize(QSize(800, 600))
        self.setWindowTitle("My awesome App")

        #label= QLabel("This is awesome")
        #label.setAlignment(Qt.AlignCenter)

        button = PushButton("Press Me")
        #button.setCheckable(True) 
        button.clicked.connect(button.button_clicked)
        #button.clicked.connect(self.the_button_was_toggled)
        
        #self.setCentralWidget(label)
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
