from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys

from data.dataframes import *
from functions.team_information import get_team_basic_information

class PushButton(QPushButton):
    def __init__(self, text, checkable = False, enabled = True, *args, **kwargs):
        super(PushButton, self).__init__(*args, **kwargs)
        self.setText(text)
        self.setCheckable(checkable)
        self.setEnabled(enabled)
    
    def button_clicked(self):
        print("Button clicked!")

class Picker(QComboBox):
    def __init__(self, *args, **kwargs):
        super(Picker, self).__init__(*args, **kwargs)
    
    def text_changed(self, text):
        print(text, "changed")

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.resize(QSize(800, 600))
        self.setWindowTitle("European Football & Analytics App")

        self.label = QLabel()

        #self.team_picker = Picker()
        self.team_picker = QComboBox()
        self.team_picker.addItems(teams_df.sort_values("team_long_name")["team_long_name"].tolist())
        self.team_picker.currentTextChanged.connect(self.change_team_layout)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.button = PushButton("Press Me")
        self.button.clicked.connect(self.button.button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.team_picker)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)


        #button.setCheckable(True) 
        
        #button.clicked.connect(self.the_button_was_toggled)
        
        #self.setCentralWidget(label)
        #self.setCentralWidget(button)
    
    def text_changed(self, text):
        print(text)

    def index_changed(self, text):
        print(text)

    def change_team_layout(self, team_name):
        
        team_country, team_league = get_team_basic_information(team_name)
        
        team_label, league_label, country_label = QLabel(), QLabel(), QLabel()

        team_label.setText(team_name)
        league_label.setText(team_league)
        country_label.setText(team_country)

        labels_list = [self.team_picker, team_label, league_label, country_label]
        
        team_layout = QVBoxLayout()
        for label in labels_list:
            team_layout.addWidget(label)
        container = QWidget()
        container.setLayout(team_layout)
        self.setCentralWidget(container)
        return

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
