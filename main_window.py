import tkinter as tk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Reconhecimento Facial")

        self.buttons = {
            "sorriso": tk.Button(root, text="Ação Sorriso", state=tk.DISABLED),
            "piscando olho esquerdo": tk.Button(root, text="Ação Piscando Olho Esquerdo", state=tk.DISABLED),
            "piscando olho direito": tk.Button(root, text="Ação Piscando Olho Direito", state=tk.DISABLED),
            "franzindo testa": tk.Button(root, text="Ação Franzindo Testa", state=tk.DISABLED),
            "mostrando dentes": tk.Button(root, text="Ação Mostrando Dentes", state=tk.DISABLED)
        }

        for button in self.buttons.values():
            button.pack(pady=5)

    def update_buttons(self, expression):
        for key in self.buttons:
            if key == expression:
                self.buttons[key].config(state=tk.NORMAL)
            else:
                self.buttons[key].config(state=tk.DISABLED)

