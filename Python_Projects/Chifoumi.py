import tkinter as tk
import random

# Choix possibles
CHOICES = ["Pierre", "Feuille", "Ciseaux"]

# Variables de score
player_score = 0
rounds_played = 0
total_rounds = 0

# Fonction pour jouer un coup
def play(player_choice):
    global player_score, rounds_played, total_rounds

    if rounds_played >= total_rounds:
        result_label.config(text="La partie est terminée !")
        return

    bot_choice = random.choice(CHOICES)

    # Affichage des choix
    choice_label.config(text=f"Toi : {player_choice} | Bot : {bot_choice}")

    # Détermination du gagnant
    if player_choice == bot_choice:
        result = "Égalité !"
    elif (player_choice == "Pierre" and bot_choice == "Ciseaux") or \
         (player_choice == "Feuille" and bot_choice == "Pierre") or \
         (player_choice == "Ciseaux" and bot_choice == "Feuille"):
        result = "Gagné !"
        player_score += 1
    else:
        result = "Perdu !"

    rounds_played += 1
    result_label.config(text=result)
    score_label.config(text=f"Score : {player_score}/{total_rounds}")

    if rounds_played == total_rounds:
        if player_score > total_rounds // 2:
            result_label.config(text="🎉 Victoire finale ! 🎉")
        elif player_score == total_rounds // 2:
            result_label.config(text="😐 Match nul !")
        else:
            result_label.config(text="💀 Défaite finale ! 💀")

# Fonction pour lancer une partie
def start_game():
    global player_score, rounds_played, total_rounds
    try:
        total_rounds = int(rounds_entry.get())
        player_score = 0
        rounds_played = 0
        score_label.config(text=f"Score : 0/{total_rounds}")
        result_label.config(text="La partie commence ! Choisis ton coup 👇")
        choice_label.config(text="")
    except ValueError:
        result_label.config(text="⚠️ Entre un nombre valide de rounds !")

# --- Interface graphique ---
window = tk.Tk()
window.title("Pierre Feuille Ciseaux ✂️")
window.geometry("400x400")
window.config(bg="#2c3e50")

# Zone pour entrer le nombre de rounds
rounds_label = tk.Label(window, text="Nombre de rounds :", font=("Arial", 12), bg="#2c3e50", fg="white")
rounds_label.pack(pady=5)

rounds_entry = tk.Entry(window, font=("Arial", 12))
rounds_entry.pack(pady=5)

start_button = tk.Button(window, text="Démarrer la partie", command=start_game, bg="#27ae60", fg="white", font=("Arial", 12, "bold"))
start_button.pack(pady=10)

# Labels d'affichage
choice_label = tk.Label(window, text="", font=("Arial", 12), bg="#2c3e50", fg="white")
choice_label.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#2c3e50", fg="yellow")
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score : 0/0", font=("Arial", 12), bg="#2c3e50", fg="white")
score_label.pack(pady=5)

# Boutons de choix
buttons_frame = tk.Frame(window, bg="#2c3e50")
buttons_frame.pack(pady=20)

btn_pierre = tk.Button(buttons_frame, text="🪨 Pierre", command=lambda: play("Pierre"), width=10, height=2, bg="#3498db", fg="white")
btn_pierre.grid(row=0, column=0, padx=5)

btn_feuille = tk.Button(buttons_frame, text="📜 Feuille", command=lambda: play("Feuille"), width=10, height=2, bg="#e67e22", fg="white")
btn_feuille.grid(row=0, column=1, padx=5)

btn_ciseaux = tk.Button(buttons_frame, text="✂️ Ciseaux", command=lambda: play("Ciseaux"), width=10, height=2, bg="#9b59b6", fg="white")
btn_ciseaux.grid(row=0, column=2, padx=5)

# Lancement de la fenêtre
window.mainloop()
