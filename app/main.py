import tkinter as tk
from app.views.login_view import LoginView
from app.views.menu_view import MenuView

def iniciar_menu():
    MenuView()

if __name__ == "__main__":
    root = tk.Tk()
    LoginView(root, iniciar_menu)
    root.mainloop()
