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
        
        self.lb_presentation = QLabel("Le ou les fichiers à tester doivent se trouver dans le répertoire 'test'.", self.zone_centrale) # Le label du haut
        self.lb_presentation.setGeometry(25, 20, 550, 40)
        self.lb_presentation.setStyleSheet("font-size: 17px ; font-style: italic ; font-weight: bold")
        self.lb_presentation.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.liste_fichiers = [] # Création de la liste utilisé dans le ComboBox
        self.repertoire_test = Path.cwd() / "test" # Création de la variable Path qui contient l'adresse relative du script
        for i in self.repertoire_test.iterdir(): # Je créé un itérable et je boucle pour incrémenter ma liste
            self.liste_fichiers.append(i.name) # Le .name permet de n'afficher uniquement le fichier et son extension

        self.cbb_fichier_teste = QComboBox(self.zone_centrale) # Le menu déroullant
        self.cbb_fichier_teste.setGeometry(25, 80, 300, 60) # Coordonnées et taille
        self.cbb_fichier_teste.setEditable(True) # Permet d'exécuter setCurrentText, le setAlignement sur le ComboBox
        self.cbb_fichier_teste.lineEdit().setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.cbb_fichier_teste.setStyleSheet("font-size: 17px ; font-weight: bold; border: 2px solid black")
        self.cbb_fichier_teste.addItems(self.liste_fichiers) # Ajoute dans le ComboBox tout se qui se trouve dans ma
        self.cbb_fichier_teste.setCurrentText("Choisir le fichier : ") # Ce qui apparait de base dans le comboBox

        self.btn_tester = QPushButton("TESTER", self.zone_centrale) # Le bouton
        self.btn_tester.setGeometry(387.5, 90, 150, 40)
        self.btn_tester.setStyleSheet("""background-color: #FFE65A ; border: 1px solid black ; border-top-left-radius: 40px;
                                    border-bottom-right-radius: 40px ; font-size: 17px ; font-weight: bold""")
        self.btn_tester.clicked.connect(self.test)

        self.lb_resultat = QLabel("Le résultat sera afficher ici.", self.zone_centrale) # Le label "RESULTAT"
        self.lb_resultat.setGeometry(25, 165, 550, 60)
        self.lb_resultat.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lb_resultat.setStyleSheet("""font-size: 22px ; background: #E1F1D5 ; border-radius: 75px 20px ;
                                    font-style: italic ; font-weight: bold ; border: 2px solid black""")

    def test(self): # Méthode qui test la validité du fichier.
        fichier = self.cbb_fichier_teste.currentText() # Récupère la valeur du comboBox donc le nom du fichier.
        if fichier == "Choisir le fichier : ": # Si aucun choix n'est fait dans le comboBox
            self.lb_resultat.setStyleSheet("""font-size: 22px ; background: #E1F1D5 ; border-radius: 75px 20px ; 
                                    font-style: italic ; font-weight: bold ; border: 2px solid black ; color: blue""")
            self.lb_resultat.setText("Vous n'avez pas sélectionné de fichier.")
        else:    
            try:
                with open(f"test/{fichier}", "r") as f: # J'ouvre le fichier dans le TRY. Si ça fonctionne le fichier est valide.
                    essai = json.load(f)
                    f.close()
                self.lb_resultat.setStyleSheet("""font-size: 22px ; background: #E1F1D5 ; border-radius: 75px 20px ;
                                    font-style: italic ; font-weight: bold ; border: 2px solid black ; color: green""")
                self.lb_resultat.setText("Le fichier est valide")
            except: # Sinon le fichier est invalide.
                self.lb_resultat.setStyleSheet("""font-size: 22px ; background: #E1F1D5 ; border-radius: 75px 20px ; 
                                    font-style: italic ; font-weight: bold ; border: 2px solid black ; color: red""")
                self.lb_resultat.setText("Le fichier n'est pas valide")


app = QApplication()
fenetre = testeur_json()
fenetre.show()
app.exec()
