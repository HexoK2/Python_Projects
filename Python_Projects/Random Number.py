import customtkinter
import random

# On configure l'apparence
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de devinette")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variables du jeu
        self.secret_number = random.randint(1, 10)
        self.attempts = 0

        # Création des widgets
        self.label_info = customtkinter.CTkLabel(
            master=self.root,
            text="Devine le nombre secret (entre 1 et 10)",
            font=("Arial", 16)
        )
        self.label_info.pack(pady=20)

        self.entry_guess = customtkinter.CTkEntry(
            master=self.root,
            placeholder_text="Entrez votre nombre...",
            width=200
        )
        self.entry_guess.pack(pady=10)

        self.button_guess = customtkinter.CTkButton(
            master=self.root,
            text="Deviner",
            command=self.check_guess
        )
        self.button_guess.pack(pady=10)

        self.label_feedback = customtkinter.CTkLabel(
            master=self.root,
            text="",
            font=("Arial", 14),
            text_color="yellow"
        )
        self.label_feedback.pack(pady=10)

    def check_guess(self):
        """Vérifie le nombre entré par l'utilisateur."""
        try:
            user_guess = int(self.entry_guess.get())
            self.attempts += 1

            if user_guess < 1 or user_guess > 10:
                self.label_feedback.configure(text="Entre un nombre entre 1 et 10.", text_color="red")
            elif user_guess < self.secret_number:
                self.label_feedback.configure(text="C'est plus grand !", text_color="orange")
            elif user_guess > self.secret_number:
                self.label_feedback.configure(text="C'est plus petit !", text_color="orange")
            else:
                self.label_feedback.configure(text=f"Bravo ! Trouvé en {self.attempts} essais.", text_color="green")
                # Désactiver les widgets pour éviter de continuer le jeu
                self.entry_guess.configure(state="disabled")
                self.button_guess.configure(state="disabled")

        except ValueError:
            self.label_feedback.configure(text="Ceci n'est pas un nombre.", text_color="red")


def main():
    root = customtkinter.CTk()
    game = GuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
