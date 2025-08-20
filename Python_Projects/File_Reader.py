# On importe les librairies nécessaires
# customtkinter pour l'interface graphique stylée
import customtkinter
# tkinter pour la boîte de dialogue de sélection de fichier (filedialog)
import tkinter as tk
from tkinter import filedialog
# os pour vérifier l'existence du fichier
import os


# sys n'est plus utile dans cette version, mais on le laisse au cas où

# --- FONCTION D'ANALYSE ---
# Cette fonction fait tout le travail d'analyse du fichier
def analyze_file(file_path):
    """
    Analyse un fichier texte et retourne un dictionnaire avec les résultats.
    """
    # Étape 1 : Vérifier si le fichier existe réellement sur l'ordinateur
    if not os.path.exists(file_path):
        # Si le fichier n'existe pas, on retourne une erreur dans un dictionnaire
        return {"error": f"Le fichier '{file_path}' n'a pas été trouvé."}

    try:
        # Étape 2 : Ouvrir le fichier en mode lecture ('r') et le lire entièrement
        # 'with open(...)' est une bonne pratique pour s'assurer que le fichier est bien fermé
        # 'encoding='utf-8'' est important pour lire les caractères spéciaux (é, à, etc.)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Étape 3 : Gérer le cas où le fichier est vide
            if not content:
                return {"error": "Le fichier est vide."}

            # --- DÉBUT DES CALCULS ---
            # On utilise des méthodes simples de Python pour l'analyse

            # Compter les lignes en cherchant le caractère de saut de ligne '\n'
            number_of_lines = content.count('\n') + 1

            # Compter les caractères avec la fonction len()
            number_of_characters = len(content)

            # Diviser le contenu en une liste de mots
            # .split() sépare le texte à chaque espace par défaut
            words = content.split()
            number_of_words = len(words)

            # Étape 4 : Gérer le cas où le fichier ne contient pas de mots
            if not words:
                return {"error": "Le fichier ne contient aucun mot."}

            # --- TROUVER LE MOT LE PLUS LONG ET LE PLUS COURT ---
            # On initialise les variables avec le premier mot de la liste
            longest_word = words[0]
            shortest_word = words[0]

            # On parcourt chaque mot dans la liste
            for word in words:
                # Si le mot actuel est plus long que le mot le plus long trouvé jusqu'ici...
                if len(word) > len(longest_word):
                    # ...on le remplace
                    longest_word = word

                # Si le mot actuel est plus court que le mot le plus court trouvé jusqu'ici...
                if len(word) < len(shortest_word):
                    # ...on le remplace
                    shortest_word = word

            # Étape 5 : Retourner tous les résultats dans un dictionnaire
            return {
                "file_path": file_path,
                "number_of_lines": number_of_lines,
                "number_of_words": number_of_words,
                "number_of_characters": number_of_characters,
                "longest_word": longest_word,
                "shortest_word": shortest_word
            }

    except Exception as e:
        # En cas d'erreur inattendue (par exemple, problème de permission), on retourne le message d'erreur
        return {"error": f"Une erreur s'est produite : {e}"}


# --- CLASSE DE LA FENÊTRE DE RÉSULTATS ---
# Cette classe crée une nouvelle fenêtre pour afficher les résultats
class ResultWindow(customtkinter.CTkToplevel):
    def __init__(self, master, results):
        # On appelle le constructeur de la classe parente
        super().__init__(master)

        # On définit le titre et la taille de la fenêtre
        self.title("Résultats de l'analyse")
        self.geometry("600x300")
        self.resizable(True, True)  # On empêche de redimensionner la fenêtre

        # Si le dictionnaire de résultats contient une erreur...
        if "error" in results:
            # ...on affiche un message d'erreur
            label = customtkinter.CTkLabel(self, text=results["error"], font=("Arial", 16))
            label.pack(pady=20)
        else:
            # Sinon, on affiche tous les résultats
            label_title = customtkinter.CTkLabel(self, text="Analyse terminée !", font=("Arial", 20, "bold"))
            label_title.pack(pady=10)

            # On prépare le texte à afficher avec tous les résultats
            result_text = (
                f"Fichier : {os.path.basename(results['file_path'])}\n"  # os.path.basename() garde juste le nom du fichier
                f"Lignes : {results['number_of_lines']}\n"
                f"Mots : {results['number_of_words']}\n"
                f"Caractères : {results['number_of_characters']}\n"
                f"Mot le plus long : '{results['longest_word']}' ({len(results['longest_word'])} caractères)\n"
                f"Mot le plus court : '{results['shortest_word']}' ({len(results['shortest_word'])} caractères)"
            )
            # On crée un label pour afficher le texte
            result_label = customtkinter.CTkLabel(self, text=result_text, font=("Arial", 14), justify="left")
            result_label.pack(pady=10, padx=20)

            # On ajoute un bouton pour fermer la fenêtre
            button_close = customtkinter.CTkButton(self, text="Fermer", command=self.destroy)
            button_close.pack(pady=10)


# --- CLASSE DE LA FENÊTRE PRINCIPALE (MENU) ---
# C'est la première fenêtre que l'utilisateur voit
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # Configuration de la fenêtre
        self.title("Analyseur de Fichier")
        self.geometry("300x150")
        self.resizable(False, False)

        # Création d'un label avec la question
        self.label_question = customtkinter.CTkLabel(self, text="Voulez-vous analyser un fichier ?", font=("Arial", 16))
        self.label_question.pack(pady=10)

        # Création d'un cadre pour les boutons
        self.frame_buttons = customtkinter.CTkFrame(self)
        self.frame_buttons.pack()

        # Création des deux boutons "Oui" et "Non"
        self.btn_yes = customtkinter.CTkButton(self.frame_buttons, text="Oui", command=self.on_yes_click)
        self.btn_yes.pack(side="left", padx=10)  # side="left" pour placer le bouton à gauche

        self.btn_no = customtkinter.CTkButton(self.frame_buttons, text="Non", command=self.on_no_click)
        self.btn_no.pack(side="right", padx=10)  # side="right" pour placer le bouton à droite

    # --- MÉTHODES DES BOUTONS ---
    def on_yes_click(self):
        # Cette fonction s'exécute quand on clique sur "Oui"

        # Ouvre la boîte de dialogue de sélection de fichier
        file_path = filedialog.askopenfilename(
            title="Sélectionner le fichier à analyser",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )

        # Si un chemin de fichier a été sélectionné (file_path n'est pas vide)
        if file_path:
            # On lance l'analyse du fichier
            results = analyze_file(file_path)
            # On crée et on affiche la fenêtre de résultats
            result_window = ResultWindow(self, results)
        else:
            # Si aucun fichier n'a été sélectionné, on affiche un message dans le terminal
            print("Opération annulée.")

    def on_no_click(self):
        # Cette fonction s'exécute quand on clique sur "Non"
        print("Opération annulée.")
        # On ferme l'application
        self.destroy()


# --- POINT D'ENTRÉE DU PROGRAMME ---
# Ce code ne s'exécute que si le fichier est lancé directement
if __name__ == "__main__":
    # On définit l'apparence par défaut (couleurs)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    # On crée une instance de la classe App et on lance la boucle principale
    # .mainloop() permet de garder la fenêtre ouverte et d'attendre les actions de l'utilisateur
    app = App()
    app.mainloop()