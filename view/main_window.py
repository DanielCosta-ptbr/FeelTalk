import tkinter as tk
from view.guiExpressions import GuiExpressions
from view.guiHome import GuiHome

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("FeelTalk")

        self.gui_expressions = GuiExpressions(self.root)
        self.gui_home = GuiHome(self.root)

        self.buttons = {
            "sorriso": self.gui_expressions.button_smile,
            "piscando olho esquerdo": self.gui_expressions.button_left_wink,
            "piscando olho direito": self.gui_expressions.button_right_wink,
            "franzindo testa": self.gui_expressions.button_frown,
            "mostrando dentes": self.gui_expressions.button_teeth
        }

    def update_buttons(self, expression):
        for key, button in self.buttons.items():
            if key == expression:
                button.config(state=tk.NORMAL)
            else:
                button.config(state=tk.DISABLED)

