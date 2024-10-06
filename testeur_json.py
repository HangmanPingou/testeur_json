from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QComboBox
from PySide6 import QtCore
from pathlib import Path
import json

class testeur_json(QMainWindow): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Testeur de fichier .JSON") # Titre de la fenêtre
        self.setFixedSize(600, 250) # Taille bloqué de la fenêtre
        self.zone_centrale = QWidget(self) # Définition de ma zone de travail où vont apparaitre mes widgets
        self.setCentralWidget(self.zone_centrale)
        self.zone_centrale.setStyleSheet("background: #E3F9F1") # Couleur de ma zone de travail
        
        self.presentation = QLabel("Le ou les fichiers à tester doivent se trouver dans le répertoire 'test'.", self.zone_centrale) # Le label du haut
        self.presentation.setGeometry(25, 20, 550, 40)
        self.presentation.setStyleSheet("font-size: 17px ; background: #E1F1D5 ; font-style: italic ; font-weight: bold")
        self.presentation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.liste_fichiers = [] # Création de la liste utilisé dans le ComboBox
        self.repertoire_test = Path.cwd() / "test" # Création de la variable Path qui contient l'adresse relative du script
        for i in self.repertoire_test.iterdir(): # Je créé un itérable et je boucle pour incrémenter ma liste
            self.liste_fichiers.append(i.name) # Le .name permet de n'afficher uniquement le fichier et son extension

        self.fichier_teste = QComboBox(self.zone_centrale) # Le menu déroullant
        self.fichier_teste.setGeometry(25, 80, 300, 60) # Coordonnées et taille
        self.fichier_teste.setEditable(True) # Permet d'exécuter setCurrentText, le setAlignement sur le ComboBox
        self.fichier_teste.lineEdit().setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fichier_teste.setStyleSheet("font-size: 17px ; font-weight: bold")
        self.fichier_teste.addItems(self.liste_fichiers) # Ajoute dans le ComboBox tout se qui se trouve dans ma
        self.fichier_teste.setCurrentText("Choisir le fichier : ") # Ce qui apparait de base dans le comboBox

        self.bouton = QPushButton("TESTER", self.zone_centrale) # Le bouton
        self.bouton.setGeometry(387.5, 90, 150, 40)
        self.bouton.setStyleSheet("background-color: blue ; border: 2px solid black ; border-radius: 75px 20px; font-size: 17px ; font-weight: bold")
        self.bouton.clicked.connect(self.test)

        self.resultat = QLabel("Le résultat sera afficher ici.", self.zone_centrale) # Le label "RESULTAT"
        self.resultat.setGeometry(25, 165, 550, 60)
        self.resultat.setStyleSheet("background: #E35CF1")
        self.resultat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.resultat.setStyleSheet("font-size: 17px ; background: #E1F1D5 ; font-style: italic ; font-weight: bold")

    def test(self):
        fichier = self.fichier_teste.currentText()
        try:
            with open(f"test/{fichier}", "r") as f: # J'ouvre mon fichier et créé une variable (dictionnaire), puis j'ajoute un nouveau sous-dictionnaire
                essai = json.load(f)
                f.close()
            self.resultat.setStyleSheet("font-size: 17px ; color: green ; font-style: italic ; font-weight: bold")
            self.resultat.setText("Le fichier est valide")
        except:
            self.resultat.setStyleSheet("font-size: 17px ; color: red ; font-style: italic ; font-weight: bold")
            self.resultat.setText("Le fichier n'est pas valide")





app = QApplication()
fenetre = testeur_json()
fenetre.show()
app.exec()
