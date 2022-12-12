from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

import sys

from data.dataframes import *
from functions.team_information import get_team_basic_information, get_team_results
from functions.add_widgets_to_layout import add_wigets_to_layout

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
        self.setWindowIcon(QIcon("/Users/ssotomayorba/Documents/Personal/projects/data-analysis-projects/european-soccer-database/assets/download.jpeg"))

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        
        self.team_picker = QComboBox()
        self.team_picker.addItems(teams_df.sort_values("team_long_name")["team_long_name"].tolist())
        self.team_picker.currentTextChanged.connect(self.change_team_layout)

        #self.input = QLineEdit()

        self.button = PushButton("Press Me")
        self.button.clicked.connect(self.button.button_clicked)

        layout = QVBoxLayout()
        #layout.addWidget(self.input)
        layout.addWidget(self.team_picker)
        #layout.addWidget(self.label)
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
        
        #First horizontal layout for basic team information titles
        team_title_label, league_title_label, country_title_label = QLabel(), QLabel(), QLabel()

        team_title_label.setText('Team Name')
        league_title_label.setText('League')
        country_title_label.setText('Country')

        first_h_layout = add_wigets_to_layout(QHBoxLayout(), [team_title_label, league_title_label, country_title_label])


        #Second horizontal layout for basic team information data
        team_country, team_league = get_team_basic_information(team_name)

        team_label, league_label, country_label = QLabel(), QLabel(), QLabel()

        team_label.setText(team_name)
        league_label.setText(team_league)
        country_label.setText(team_country)

        second_h_layout = add_wigets_to_layout(QHBoxLayout(), [team_label, league_label, country_label])


        #Third horizontal layout for team results titles
        team_matches_title_label, team_wins_title_label, team_draws_title_label, team_defeats_title_label = QLabel(), QLabel(), QLabel(), QLabel()

        team_matches_title_label.setText('Played Matches')
        team_wins_title_label.setText('Wins')
        team_draws_title_label.setText('Draws')
        team_defeats_title_label.setText('Defeats')

        third_h_layout = add_wigets_to_layout(QHBoxLayout(), [team_matches_title_label, team_wins_title_label, team_draws_title_label, team_defeats_title_label])
        
        
        #Fourth horizontal layout for team results data
        team_wins, team_draws, team_defeats = get_team_results(team_name)

        team_matches_label, team_wins_label, team_draws_label, team_defeats_label = QLabel(), QLabel(), QLabel(), QLabel()

        team_matches_label.setText(str(team_wins + team_draws + team_defeats))
        team_wins_label.setText(str(team_wins))
        team_draws_label.setText(str(team_draws))
        team_defeats_label.setText(str(team_defeats))
        
        fourth_h_layout = add_wigets_to_layout(QHBoxLayout(), [team_matches_label, team_wins_label, team_draws_label, team_defeats_label])

        team_v_layout = add_wigets_to_layout(QVBoxLayout(), [self.team_picker])
        team_v_layout = add_wigets_to_layout(team_v_layout, [first_h_layout, second_h_layout, third_h_layout, fourth_h_layout], False)

        container = QWidget()
        container.setLayout(team_v_layout)
        self.setCentralWidget(container)
        return

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("/Users/ssotomayorba/Documents/Personal/projects/data-analysis-projects/european-soccer-database/assets/football-icon-flat-style-vector-soccer-ball-transparent-background-sport-object-you-design-projects-140588179.jpg"))

window = MainWindow()
window.show()

app.exec()
